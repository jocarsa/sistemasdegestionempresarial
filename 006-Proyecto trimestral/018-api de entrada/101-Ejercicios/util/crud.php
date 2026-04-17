<?php
// util/crud.php
require_once __DIR__ . "/db.php";

function table_columns(string $tabla): array {
  $pdo = db();
  $st = $pdo->prepare("PRAGMA table_info($tabla)");
  $st->execute();
  return $st->fetchAll(); // [{cid,name,type,notnull,dflt_value,pk}, ...]
}

function table_pk(string $tabla): string {
  $cols = table_columns($tabla);
  foreach ($cols as $c) if ((int)$c["pk"] === 1) return $c["name"];
  return "id";
}

function list_rows(string $tabla): array {
  $pdo = db();
  $st = $pdo->query("SELECT * FROM $tabla ORDER BY 1 DESC");
  return $st->fetchAll();
}

function get_row(string $tabla, $id): ?array {
  $pdo = db();
  $pk = table_pk($tabla);
  $st = $pdo->prepare("SELECT * FROM $tabla WHERE $pk = :id LIMIT 1");
  $st->execute([":id" => $id]);
  $r = $st->fetch();
  return $r ?: null;
}

function insert_row(string $tabla, array $data): void {
  $pdo = db();
  $cols = array_keys($data);
  $place = array_map(fn($c)=>":$c", $cols);

  $sql = "INSERT INTO $tabla (" . implode(",", $cols) . ")
          VALUES (" . implode(",", $place) . ")";
  $st = $pdo->prepare($sql);

  $params = [];
  foreach ($data as $k=>$v) $params[":$k"] = $v;
  $st->execute($params);
}

function update_row(string $tabla, $id, array $data): void {
  $pdo = db();
  $pk = table_pk($tabla);
  $sets = [];
  foreach ($data as $k=>$v) $sets[] = "$k = :$k";

  $sql = "UPDATE $tabla SET " . implode(",", $sets) . " WHERE $pk = :__id";
  $st = $pdo->prepare($sql);

  $params = [":__id" => $id];
  foreach ($data as $k=>$v) $params[":$k"] = $v;
  $st->execute($params);
}

function delete_row(string $tabla, $id): void {
  $pdo = db();
  $pk = table_pk($tabla);
  $st = $pdo->prepare("DELETE FROM $tabla WHERE $pk = :id");
  $st->execute([":id" => $id]);
}