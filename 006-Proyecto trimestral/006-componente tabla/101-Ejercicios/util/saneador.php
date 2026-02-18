<?php

foreach ($_REQUEST as $key => $value) {
    // Solo procesar valores escalares (evita arrays maliciosos)
    if (is_array($value)) {
        http_response_code(400);
        exit('Bad input');
    }

    $val = trim((string)$value);
    $val = str_replace("\0", "", $val);

    if (preg_match('/\b(select|insert|update|delete|drop|union|truncate|alter)\b|(--|#|\/\*|\*\/)/i', $val)) {
        http_response_code(400);
        exit('Bad input');
    }

    // Reasignar el valor saneado
    $_REQUEST[$key] = $val;
}

?>
