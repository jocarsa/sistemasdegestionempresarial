<?php
header('Content-Type: application/json; charset=utf-8');

$mensaje = trim($_GET['mensaje'] ?? '');

if ($mensaje === '') {
    echo json_encode([
        'ok' => false,
        'error' => 'No se ha recibido ninguna consulta.'
    ], JSON_UNESCAPED_UNICODE);
    exit;
}

$ollama_url = "http://localhost:11434/api/generate";
$modelo_sql = "qwen2.5-coder:7b";
$modelo_resumen = "qwen2.5-coder:7b";

function llamarOllama(string $url, array $data): array {
    $ch = curl_init($url);

    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        "Content-Type: application/json"
    ]);
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));

    $response = curl_exec($ch);

    if ($response === false) {
        $error = curl_error($ch);
        curl_close($ch);
        return [
            'ok' => false,
            'error' => 'Error conectando con Ollama: ' . $error
        ];
    }

    curl_close($ch);

    $json = json_decode($response, true);

    if (!is_array($json)) {
        return [
            'ok' => false,
            'error' => 'Respuesta JSON no válida desde Ollama.'
        ];
    }

    return [
        'ok' => true,
        'json' => $json
    ];
}

function limpiarSql(string $sql): string {
    $sql = preg_replace('/```sql|```/i', '', $sql);
    $sql = trim($sql);
    $sql = rtrim($sql, "; \t\n\r\0\x0B");
    return $sql;
}

function validarSqlSelect(string $sql): ?string {
    if (strpos($sql, ';') !== false) {
        return 'La consulta contiene más de una sentencia.';
    }

    if (!preg_match('/^\s*select\s+/i', $sql)) {
        return 'Solo se permiten consultas SELECT.';
    }

    $sqlLower = mb_strtolower($sql, 'UTF-8');

    $bloqueadas = [
        'insert ', 'update ', 'delete ', 'drop ', 'alter ', 'create ',
        'pragma ', 'attach ', 'detach ', 'replace ', 'truncate ',
        'vacuum ', 'begin ', 'commit ', 'rollback '
    ];

    foreach ($bloqueadas as $palabra) {
        if (strpos($sqlLower, $palabra) !== false) {
            return 'La consulta contiene instrucciones no permitidas.';
        }
    }

    return null;
}

function escapar(string $texto): string {
    return htmlspecialchars($texto, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
}

function generarTablaHtml(array $rows): string {
    if (count($rows) === 0) {
        return '<div class="panel-seccion"><div class="ok">Consulta ejecutada correctamente, pero no hay resultados.</div></div>';
    }

    $html = '<div class="panel-seccion">';
    $html .= '<div class="ok" style="margin-bottom:12px;">Consulta ejecutada correctamente. Filas devueltas: ' . count($rows) . '</div>';
    $html .= '<div class="tabla-wrap">';
    $html .= '<table>';
    $html .= '<thead><tr>';

    foreach (array_keys($rows[0]) as $columna) {
        $html .= '<th>' . escapar((string)$columna) . '</th>';
    }

    $html .= '</tr></thead><tbody>';

    foreach ($rows as $fila) {
        $html .= '<tr>';
        foreach ($fila as $valor) {
            if ($valor === null) {
                $valor = '';
            }
            $html .= '<td>' . escapar((string)$valor) . '</td>';
        }
        $html .= '</tr>';
    }

    $html .= '</tbody></table>';
    $html .= '</div>';
    $html .= '</div>';

    return $html;
}

$prompt_sql = <<<PROMPT
Eres un generador de consultas SQL para SQLite.

Reglas obligatorias:
- Devuelve una única sentencia SQL.
- Solo se permite SELECT.
- No uses INSERT, UPDATE, DELETE, DROP, ALTER, CREATE, PRAGMA, ATTACH, DETACH, REPLACE.
- No pongas explicaciones.
- No pongas comentarios.
- No pongas fences.
- No pongas varias sentencias.
- Usa únicamente esta tabla y estas columnas:

CREATE TABLE clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    apellidos TEXT,
    email TEXT,
    telefono TEXT,
    ciudad TEXT,
    edad INTEGER,
    fecha_registro DATE,
    activo INTEGER
);

Convierte esta petición en una consulta SQLite:
PROMPT;

$resSql = llamarOllama($ollama_url, [
    "model" => $modelo_sql,
    "prompt" => $prompt_sql . "\n" . $mensaje,
    "stream" => false
]);

if (!$resSql['ok']) {
    echo json_encode([
        'ok' => false,
        'error' => $resSql['error']
    ], JSON_UNESCAPED_UNICODE);
    exit;
}

$sql = trim($resSql['json']['response'] ?? '');
$sql = limpiarSql($sql);

if ($sql === '') {
    echo json_encode([
        'ok' => false,
        'error' => 'El modelo no devolvió ninguna consulta SQL.'
    ], JSON_UNESCAPED_UNICODE);
    exit;
}

$errorSql = validarSqlSelect($sql);
if ($errorSql !== null) {
    echo json_encode([
        'ok' => false,
        'sql' => $sql,
        'error' => $errorSql
    ], JSON_UNESCAPED_UNICODE);
    exit;
}

try {
    $pdo = new PDO('sqlite:empresa.db');
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    $stmt = $pdo->query($sql);
    $rows = $stmt->fetchAll(PDO::FETCH_ASSOC);

} catch (PDOException $e) {
    echo json_encode([
        'ok' => false,
        'sql' => $sql,
        'error' => 'Error al ejecutar la consulta SQLite: ' . $e->getMessage()
    ], JSON_UNESCAPED_UNICODE);
    exit;
}

$max_filas_resumen = 20;
$filas_para_resumen = array_slice($rows, 0, $max_filas_resumen);

$datos_para_ia = [
    'consulta_usuario' => $mensaje,
    'sql_generado' => $sql,
    'total_filas' => count($rows),
    'muestra_resultados' => $filas_para_resumen
];

$json_datos = json_encode($datos_para_ia, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);

$prompt_resumen = <<<PROMPT
Eres un asistente que resume resultados de consultas SQL para un usuario no técnico.

Reglas:
- Responde en español.
- Responde en un párrafo breve.
- Indica cuántas filas se han encontrado.
- Resume lo más relevante del resultado.
- Si no hay filas, dilo claramente.
- No menciones JSON.
- No pongas markdown.
- No pongas listas.
- No pongas fences.

Datos de entrada:
$json_datos
PROMPT;

$resResumen = llamarOllama($ollama_url, [
    "model" => $modelo_resumen,
    "prompt" => $prompt_resumen,
    "stream" => false
]);

$summary = 'No se pudo generar el resumen.';
if ($resResumen['ok']) {
    $summary = trim($resResumen['json']['response'] ?? $summary);
}

$table_html = generarTablaHtml($rows);
$summary_html = '<div class="ok">' . escapar($summary) . '</div>';

echo json_encode([
    'ok' => true,
    'sql' => $sql,
    'summary' => $summary,
    'summary_html' => $summary_html,
    'table_html' => $table_html,
    'rows' => $rows
], JSON_UNESCAPED_UNICODE);
?>