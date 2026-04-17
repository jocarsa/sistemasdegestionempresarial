<?php

$url = "http://localhost:11434/api/generate";

$data = [
    "model" => "qwen3.5:0.8b",
    "prompt" => $_POST['mensaje'],
    "stream" => false
];

$ch = curl_init($url);

curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    "Content-Type: application/json"
]);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));

$response = curl_exec($ch);

curl_close($ch);

// Decode JSON
$json = json_decode($response, true);

// Print only the "response" field
echo $json['response'] ?? 'No response';
?>


