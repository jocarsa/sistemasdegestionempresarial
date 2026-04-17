<?php
$respuesta = "";

if (isset($_POST['mensaje']) && trim($_POST['mensaje']) !== "") {

    $url = "http://localhost:11434/api/generate";

    $sistema = "Responde en español. Responde en un solo párrafo.";

    $data = [
        "model" => "phi4-mini:latest",
        "prompt" => $_POST['mensaje'] . "\n" . $sistema,
        "stream" => false
    ];

    $ch = curl_init($url);

    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST => true,
        CURLOPT_HTTPHEADER => ["Content-Type: application/json"],
        CURLOPT_POSTFIELDS => json_encode($data),
        CURLOPT_TIMEOUT => 60
    ]);

    $response = curl_exec($ch);

    if ($response === false) {
        $respuesta = "Error de conexión con el modelo.";
    } else {
        $json = json_decode($response, true);
        $respuesta = $json['response'] ?? "Sin respuesta del modelo.";
    }

    curl_close($ch);
}
?>

<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Chat simple con Ollama</title>

<style>
body {
    font-family: Arial, sans-serif;
    background: #f5f5f5;
    display: flex;
    justify-content: center;
    padding-top: 50px;
}

.container {
    width: 500px;
    background: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
}

h1 {
    font-size: 18px;
    margin-bottom: 15px;
    text-align: center;
}

form {
    display: flex;
}

input[type="text"] {
    flex: 1;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 6px 0 0 6px;
    outline: none;
}

button {
    padding: 10px 15px;
    border: none;
    background: #007BFF;
    color: white;
    border-radius: 0 6px 6px 0;
    cursor: pointer;
}

button:hover {
    background: #0056b3;
}

.respuesta {
    margin-top: 20px;
    padding: 10px;
    background: #f0f0f0;
    border-radius: 6px;
    min-height: 40px;
}
</style>
</head>

<body>

<div class="container">
    <h1>Chat con IA</h1>

    <form method="POST">
        <input type="text" name="mensaje" placeholder="Escribe tu mensaje..." required>
        <button type="submit">Enviar</button>
    </form>

    <?php if ($respuesta): ?>
        <div class="respuesta">
            <?= htmlspecialchars($respuesta) ?>
        </div>
    <?php endif; ?>
</div>

</body>
</html>