<?php
  $url = "http://localhost:11434/api/generate";
  $sistema = "
    - Solo quiero código fuente
    - No abras explicación
    - No introduzcas fences
    - Que el contenido esté en español
  ";
  $data = [
      "model" => "phi4-mini:latest",
      "prompt" => "
      	Crea una web personal en HTML y CSS. 
        Que el CSS sea bonito. 
        Quiero una single page application.
        Quiero que tenga un banner, sobre mi, destacados, y formulario de contacto.
        ".$sistema,
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

