<?php
$db = new SQLite3(__DIR__ . '/empresa.db');

$resultado = $db->query("
    SELECT id, nombre, apellidos, empresa, telefono, email, ciudad, provincia, saldo
    FROM clientes
    ORDER BY id ASC
");

$clientes = [];

while ($fila = $resultado->fetchArray(SQLITE3_ASSOC)) {
    $clientes[] = $fila;
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Clientes 3D</title>

<style>
body{
    margin:0;
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    background:
        radial-gradient(circle at top left, #ffffff, #dfe4ec 45%, #b9c1ce);
    font-family:Arial,sans-serif;
    overflow:hidden;
    user-select:none;
}

.drawer-container{
    position:relative;
    width:320px;
    height:320px;
    perspective:1200px;
}

.drawer{
    position:absolute;
    width:100%;
    height:100%;
    transform-style:preserve-3d;
    transition:transform 0.1s linear;
}

.square{
    position:absolute;
    left:55px;
    top:55px;
    width:210px;
    height:210px;
    padding:22px;
    box-sizing:border-box;

    display:flex;
    flex-direction:column;
    justify-content:center;
    gap:8px;

    color:#1f2937;
    cursor:pointer;

    background:rgba(255,255,255,0.32);
    backdrop-filter:blur(18px);
    -webkit-backdrop-filter:blur(18px);

    border:1px solid rgba(255,255,255,0.65);
    border-radius:24px;

    box-shadow:
        0 25px 60px rgba(31,41,55,0.18),
        inset 0 1px 0 rgba(255,255,255,0.7);

    transform-style:preserve-3d;

    transition:
        transform 0.7s cubic-bezier(.2,.8,.2,1),
        opacity 0.5s ease,
        box-shadow 0.5s ease,
        background 0.5s ease;
}

.square::before{
    content:"";
    position:absolute;
    inset:0;
    border-radius:24px;
    background:linear-gradient(
        135deg,
        rgba(255,255,255,0.55),
        rgba(255,255,255,0.05)
    );
    pointer-events:none;
}

.square strong{
    position:relative;
    font-size:19px;
    color:#111827;
    line-height:1.15;
}

.square span,
.square small{
    position:relative;
    font-size:13px;
    color:#374151;
    opacity:0.85;
}

.square .details{
    display:flex;
    flex-direction:column;
    gap:6px;
    transition:opacity 0.35s ease, transform 0.35s ease;
}

.square:hover{
    background:rgba(255,255,255,0.46);
    box-shadow:
        0 38px 90px rgba(31,41,55,0.28),
        inset 0 1px 0 rgba(255,255,255,0.8);
}

.square:hover .details{
    opacity:0;
    transform:translateY(18px);
}

.square:hover strong{
    transform:translateY(-42px);
}

.square strong{
    transition:transform 0.35s ease;
}

.square.detached{
    transform:translateX(310px) translateZ(70px) rotateY(-25deg) !important;
    opacity:0.98;
    z-index:20;
}
</style>
</head>

<body>

<div class="drawer-container">
    <div class="drawer" id="drawer">

        <?php foreach ($clientes as $i => $cliente): ?>
            <?php $z = -24 * $i; ?>

            <div class="square" style="transform:translateZ(<?= $z ?>px);">

                <strong>
                    <?= htmlspecialchars($cliente['nombre'] . ' ' . $cliente['apellidos']) ?>
                </strong>

                <div class="details">
                    <span><?= htmlspecialchars($cliente['empresa']) ?></span>

                    <small>
                        <?= htmlspecialchars($cliente['ciudad'] . ', ' . $cliente['provincia']) ?>
                    </small>

                    <small><?= htmlspecialchars($cliente['telefono']) ?></small>

                    <small><?= htmlspecialchars($cliente['email']) ?></small>

                    <small>
                        Saldo: <?= number_format((float)$cliente['saldo'], 2, ',', '.') ?> €
                    </small>
                </div>

            </div>

        <?php endforeach; ?>

    </div>
</div>

<script>
const drawer = document.getElementById("drawer");
const squares = document.querySelectorAll(".square");

let rotX = -15;
let rotY = 25;
let zoom = 0;

let dragging = false;
let lastX = 0;
let lastY = 0;
let moved = false;

function updateCamera(){
    drawer.style.transform =
        `translateZ(${zoom}px) rotateX(${rotX}deg) rotateY(${rotY}deg)`;
}

updateCamera();

document.addEventListener("mousedown", e => {
    dragging = true;
    moved = false;
    lastX = e.clientX;
    lastY = e.clientY;
});

document.addEventListener("mousemove", e => {
    if(!dragging) return;

    const dx = e.clientX - lastX;
    const dy = e.clientY - lastY;

    if(Math.abs(dx) > 2 || Math.abs(dy) > 2){
        moved = true;
    }

    rotY += dx * 0.35;
    rotX -= dy * 0.35;

    rotX = Math.max(-80, Math.min(80, rotX));

    lastX = e.clientX;
    lastY = e.clientY;

    updateCamera();
});

document.addEventListener("mouseup", () => {
    dragging = false;
});

document.addEventListener("wheel", e => {
    e.preventDefault();

    zoom -= e.deltaY * 0.8;
    zoom = Math.max(-700, Math.min(500, zoom));

    updateCamera();
}, { passive:false });

squares.forEach(square => {
    square.addEventListener("click", e => {
        e.stopPropagation();

        if(moved) return;

        square.classList.toggle("detached");
    });
});
</script>

</body>
</html>