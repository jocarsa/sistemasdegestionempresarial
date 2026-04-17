<?php
$url = "https://www.aemet.es/xml/municipios/localidad_46250.xml";
$xmlString = @file_get_contents($url);
$xml = $xmlString ? @simplexml_load_string($xmlString) : false;

function widgetTiempoEmoji($descripcion) {
	$descripcion = mb_strtolower(trim((string)$descripcion), 'UTF-8');

	if (strpos($descripcion, 'tormenta') !== false) return "⛈️";
	if (strpos($descripcion, 'lluvia') !== false) return "🌧️";
	if (strpos($descripcion, 'nieve') !== false) return "❄️";
	if (strpos($descripcion, 'despejado') !== false) return "☀️";
	if (strpos($descripcion, 'poco nuboso') !== false) return "🌤️";
	if (strpos($descripcion, 'intervalos nubosos') !== false) return "⛅";
	if (strpos($descripcion, 'muy nuboso') !== false) return "☁️";
	if (strpos($descripcion, 'nuboso') !== false) return "☁️";
	if (strpos($descripcion, 'cubierto') !== false) return "☁️";

	return "🌡️";
}

function widgetTiempoDia($fecha) {
	$dias = [
		'Monday' => 'Lun',
		'Tuesday' => 'Mar',
		'Wednesday' => 'Mié',
		'Thursday' => 'Jue',
		'Friday' => 'Vie',
		'Saturday' => 'Sáb',
		'Sunday' => 'Dom'
	];
	$en = date('l', strtotime($fecha));
	return $dias[$en] ?? $fecha;
}

function widgetTiempoDescripcionDia($dia) {
	foreach ($dia->estado_cielo as $estado) {
		if ((string)$estado['periodo'] === '00-24' || !isset($estado['periodo'])) {
			return (string)$estado['descripcion'];
		}
	}
	if (isset($dia->estado_cielo[0])) {
		return (string)$dia->estado_cielo[0]['descripcion'];
	}
	return "Sin datos";
}

function widgetTiempoProbabilidad($dia) {
	foreach ($dia->prob_precipitacion as $pp) {
		if ((string)$pp['periodo'] === '00-24' || !isset($pp['periodo'])) {
			$valor = trim((string)$pp);
			return $valor === '' ? '0' : $valor;
		}
	}
	if (isset($dia->prob_precipitacion[0])) {
		$valor = trim((string)$dia->prob_precipitacion[0]);
		return $valor === '' ? '0' : $valor;
	}
	return '0';
}
?>

<style>
.widget-tiempo-flotante{
	position:fixed;
	right:20px;
	bottom:20px;
	width:360px;
	max-width:calc(100vw - 40px);
	background:rgba(255,255,255,0.96);
	backdrop-filter:blur(10px);
	-webkit-backdrop-filter:blur(10px);
	border:1px solid rgba(0,0,0,0.08);
	border-radius:18px;
	box-shadow:0 12px 35px rgba(0,0,0,0.18);
	font-family:Arial, Helvetica, sans-serif;
	color:#1f2937;
	z-index:99999;
	overflow:hidden;
}

.widget-tiempo-flotante *{
	box-sizing:border-box;
}

.widget-tiempo-cabecera{
	padding:14px 16px 10px 16px;
	background:linear-gradient(135deg,#2563eb,#60a5fa);
	color:white;
}

.widget-tiempo-cabecera .titulo{
	font-size:16px;
	font-weight:bold;
	line-height:1.2;
}

.widget-tiempo-cabecera .subtitulo{
	font-size:12px;
	opacity:0.9;
	margin-top:4px;
}

.widget-tiempo-cuerpo{
	padding:10px;
	max-height:420px;
	overflow:auto;
}

.widget-tiempo-dia{
	display:grid;
	grid-template-columns:60px 46px 1fr auto;
	align-items:center;
	gap:8px;
	padding:10px;
	border-bottom:1px solid #e5e7eb;
}

.widget-tiempo-dia:last-child{
	border-bottom:none;
}

.widget-tiempo-nombre{
	font-size:13px;
	font-weight:bold;
}

.widget-tiempo-fecha{
	font-size:11px;
	color:#6b7280;
	margin-top:2px;
}

.widget-tiempo-emoji{
	font-size:28px;
	text-align:center;
}

.widget-tiempo-desc{
	font-size:12px;
	color:#374151;
	line-height:1.3;
}

.widget-tiempo-extra{
	text-align:right;
	white-space:nowrap;
}

.widget-tiempo-temp{
	font-size:13px;
	font-weight:bold;
}

.widget-tiempo-lluvia{
	font-size:11px;
	color:#2563eb;
	margin-top:4px;
}

.widget-tiempo-error{
	padding:16px;
	font-size:13px;
	color:#991b1b;
	background:#fef2f2;
}
</style>

<div class="widget-tiempo-flotante">
	<?php if ($xml): ?>
		<div class="widget-tiempo-cabecera">
			<div class="titulo">🌤️ Tiempo en <?php echo htmlspecialchars((string)$xml->nombre); ?></div>
			<div class="subtitulo">Previsión semanal</div>
		</div>

		<div class="widget-tiempo-cuerpo">
			<?php foreach ($xml->prediccion->dia as $dia): ?>
				<?php
					$fecha = (string)$dia['fecha'];
					$descripcion = widgetTiempoDescripcionDia($dia);
					$emoji = widgetTiempoEmoji($descripcion);
					$max = (string)$dia->temperatura->maxima;
					$min = (string)$dia->temperatura->minima;
					$lluvia = widgetTiempoProbabilidad($dia);
				?>
				<div class="widget-tiempo-dia">
					<div>
						<div class="widget-tiempo-nombre"><?php echo widgetTiempoDia($fecha); ?></div>
						<div class="widget-tiempo-fecha"><?php echo date('d/m', strtotime($fecha)); ?></div>
					</div>
					<div class="widget-tiempo-emoji"><?php echo $emoji; ?></div>
					<div class="widget-tiempo-desc"><?php echo htmlspecialchars($descripcion); ?></div>
					<div class="widget-tiempo-extra">
						<div class="widget-tiempo-temp"><?php echo $max; ?>° / <?php echo $min; ?>°</div>
						<div class="widget-tiempo-lluvia">💧 <?php echo $lluvia; ?>%</div>
					</div>
				</div>
			<?php endforeach; ?>
		</div>
	<?php else: ?>
		<div class="widget-tiempo-error">
			No se ha podido cargar la previsión meteorológica.
		</div>
	<?php endif; ?>
</div>