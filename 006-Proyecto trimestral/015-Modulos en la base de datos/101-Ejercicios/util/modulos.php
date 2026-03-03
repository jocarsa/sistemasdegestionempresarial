<?php
// util/modulos.php
require_once __DIR__ . "/db.php";

function modulos_listar_activos(): array {
  $pdo = db();
  $st = $pdo->query("
    SELECT id, slug, nombre, orden
    FROM modulos
    WHERE activo = 1
    ORDER BY orden ASC, nombre ASC
  ");
  return $st->fetchAll();
}

function modulos_obtener_por_slug(string $slug): ?array {
  $pdo = db();
  $st = $pdo->prepare("
    SELECT id, slug, nombre, orden, activo
    FROM modulos
    WHERE slug = :slug
    LIMIT 1
  ");
  $st->execute([":slug" => $slug]);
  $r = $st->fetch();
  return $r ?: null;
}

function modulos_entidades_por_slug(string $slug): array {
  $pdo = db();
  $st = $pdo->prepare("
    SELECT me.entidad
    FROM modulos m
    JOIN modulo_entidades me ON me.modulo_id = m.id
    WHERE m.slug = :slug AND m.activo = 1
    ORDER BY me.orden ASC, me.entidad ASC
  ");
  $st->execute([":slug" => $slug]);
  $rows = $st->fetchAll();

  return array_map(fn($r) => (string)$r["entidad"], $rows);
}
