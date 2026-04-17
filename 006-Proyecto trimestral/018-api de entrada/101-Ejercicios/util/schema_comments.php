<?php
// util/schema_comments.php
declare(strict_types=1);

require_once __DIR__ . "/db.php";

/**
 * Returns the comment for a table (or empty string).
 */
function schema_table_comment(string $table): string {
  $pdo = db();
  $st = $pdo->prepare("
    SELECT comment
    FROM schema_comments
    WHERE object_type='table' AND table_name=:t AND column_name IS NULL
    LIMIT 1
  ");
  $st->execute([":t" => $table]);
  $r = $st->fetchColumn();
  return $r ? (string)$r : "";
}

/**
 * Returns the comment for a column (or empty string).
 */
function schema_column_comment(string $table, string $column): string {
  $pdo = db();
  $st = $pdo->prepare("
    SELECT comment
    FROM schema_comments
    WHERE object_type='column' AND table_name=:t AND column_name=:c
    LIMIT 1
  ");
  $st->execute([":t" => $table, ":c" => $column]);
  $r = $st->fetchColumn();
  return $r ? (string)$r : "";
}

/**
 * Returns comments for all columns of a table as [col => comment].
 * Useful to avoid querying per-field in forms.
 */
function schema_columns_comments(string $table): array {
  $pdo = db();
  $st = $pdo->prepare("
    SELECT column_name, comment
    FROM schema_comments
    WHERE object_type='column' AND table_name=:t AND column_name IS NOT NULL
  ");
  $st->execute([":t" => $table]);
  $out = [];
  foreach ($st->fetchAll() as $r) {
    $cn = (string)($r["column_name"] ?? "");
    if ($cn !== "") $out[$cn] = (string)($r["comment"] ?? "");
  }
  return $out;
}
