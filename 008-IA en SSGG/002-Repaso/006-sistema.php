<?php
if(isset($_POST['mensaje'])){
  $url = "http://localhost:11434/api/generate";
  $sistema = "
    - Responde en español.
    - Responde en un párrafo.
  ";
  $data = [
      "model" => "phi4-mini:latest",
      "prompt" => $_POST['mensaje'].$sistema,
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
}
?>
<form action="?" method="POST">
	<input type="text" name="mensaje" placeholder="Introduce tu mensaje y pulsa ENTER">
</form>

