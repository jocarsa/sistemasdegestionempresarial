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
    background:radial-gradient(circle at top left,#fff,#dfe4ec 45%,#b9c1ce);
    font-family:Arial,sans-serif;
    overflow:hidden;
    user-select:none;
}

.search-panel{
    position:fixed;
    top:24px;
    left:50%;
    transform:translateX(-50%);
    z-index:100;
    width:min(420px,calc(100vw - 40px));
}

.search-panel input{
    width:100%;
    padding:15px 20px;
    border-radius:999px;
    border:1px solid rgba(255,255,255,0.7);
    background:rgba(255,255,255,0.42);
    backdrop-filter:blur(18px);
    -webkit-backdrop-filter:blur(18px);
    box-shadow:0 18px 45px rgba(31,41,55,0.18);
    font-size:15px;
    color:#111827;
    outline:none;
}

.scene{
    position:absolute;
    inset:0;
    display:flex;
    justify-content:center;
    align-items:center;
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

    background:rgba(255,255,255,0.34);
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
        background 0.5s ease,
        filter 0.5s ease;
}

.square::before{
    content:"";
    position:absolute;
    inset:0;
    border-radius:24px;
    background:linear-gradient(135deg,rgba(255,255,255,0.55),rgba(255,255,255,0.05));
    pointer-events:none;
}

.square strong,
.square .details{
    position:relative;
}

.square strong{
    font-size:19px;
    color:#111827;
    line-height:1.15;
    transition:transform 0.35s ease;
}

.square span,
.square small{
    font-size:13px;
    color:#374151;
    opacity:0.85;
}

.details{
    display:flex;
    flex-direction:column;
    gap:6px;
    transition:opacity 0.35s ease, transform 0.35s ease;
}

.square:hover,
.square.search-match{
    background:rgba(255,255,255,0.52);
    box-shadow:
        0 38px 90px rgba(31,41,55,0.28),
        inset 0 1px 0 rgba(255,255,255,0.8);
}

.square:hover .details,
.square.search-match .details{
    opacity:0;
    transform:translateY(18px);
}

.square:hover strong,
.square.search-match strong{
    transform:translateY(-42px);
}

.square.search-no-match{
    opacity:0.18;
    filter:blur(1px) grayscale(0.4);
    pointer-events:none;
}

.square.detached{
    transform:translateX(310px) translateZ(70px) rotateY(-25deg) !important;
    opacity:0.98;
    z-index:20;
}
</style>
</head>

<body>

<div class="search-panel">
    <input id="searchInput" type="text" placeholder="Buscar cliente, empresa, ciudad, email...">
</div>

<div class="scene" id="scene">
    <div class="drawer-container">
        <div class="drawer" id="drawer">

            <?php foreach ($clientes as $i => $cliente): ?>
                <?php
                $z = -24 * $i;
                $textoBusqueda = strtolower(
                    $cliente['nombre'] . ' ' .
                    $cliente['apellidos'] . ' ' .
                    $cliente['empresa'] . ' ' .
                    $cliente['telefono'] . ' ' .
                    $cliente['email'] . ' ' .
                    $cliente['ciudad'] . ' ' .
                    $cliente['provincia']
                );
                ?>

                <div class="square"
                     data-search="<?= htmlspecialchars($textoBusqueda) ?>"
                     style="transform:translateZ(<?= $z ?>px);">

                    <strong>
                        <?= htmlspecialchars($cliente['nombre'] . ' ' . $cliente['apellidos']) ?>
                    </strong>

                    <div class="details">
                        <span><?= htmlspecialchars($cliente['empresa']) ?></span>
                        <small><?= htmlspecialchars($cliente['ciudad'] . ', ' . $cliente['provincia']) ?></small>
                        <small><?= htmlspecialchars($cliente['telefono']) ?></small>
                        <small><?= htmlspecialchars($cliente['email']) ?></small>
                        <small>Saldo: <?= number_format((float)$cliente['saldo'], 2, ',', '.') ?> €</small>
                    </div>

                </div>

            <?php endforeach; ?>

        </div>
    </div>
</div>

<script>
const scene = document.getElementById("scene");
const drawer = document.getElementById("drawer");
const squares = document.querySelectorAll(".square");
const searchInput = document.getElementById("searchInput");

let rotX = -15;
let rotY = 25;
let zoom = 0;

let panX = 0;
let panY = 0;

let dragging = false;
let panning = false;

let lastX = 0;
let lastY = 0;
let moved = false;

function updateCamera(){
    scene.style.transform = `translate(${panX}px, ${panY}px)`;

    drawer.style.transform =
        `translateZ(${zoom}px) rotateX(${rotX}deg) rotateY(${rotY}deg)`;
}

updateCamera();

document.addEventListener("mousedown", e => {
    if(e.button === 1){
        e.preventDefault();
        panning = true;
    } else if(e.button === 0){
        dragging = true;
    }

    moved = false;
    lastX = e.clientX;
    lastY = e.clientY;
});

document.addEventListener("mousemove", e => {
    if(!dragging && !panning) return;

    const dx = e.clientX - lastX;
    const dy = e.clientY - lastY;

    if(Math.abs(dx) > 2 || Math.abs(dy) > 2){
        moved = true;
    }

    if(panning){
        panX += dx;
        panY += dy;
    }

    if(dragging){
        rotY += dx * 0.35;
        rotX -= dy * 0.35;
        rotX = Math.max(-80, Math.min(80, rotX));
    }

    lastX = e.clientX;
    lastY = e.clientY;

    updateCamera();
});

document.addEventListener("mouseup", () => {
    dragging = false;
    panning = false;
});

document.addEventListener("wheel", e => {
    e.preventDefault();

    zoom -= e.deltaY * 0.8;
    zoom = Math.max(-700, Math.min(500, zoom));

    updateCamera();
}, { passive:false });

document.addEventListener("auxclick", e => {
    if(e.button === 1){
        e.preventDefault();
    }
});

searchInput.addEventListener("input", () => {
    const query = searchInput.value.trim().toLowerCase();

    squares.forEach(square => {
        square.classList.remove("search-match", "search-no-match");

        if(query === ""){
            return;
        }

        const text = square.dataset.search;

        if(text.includes(query)){
            square.classList.add("search-match");
        } else {
            square.classList.add("search-no-match");
        }
    });
});

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