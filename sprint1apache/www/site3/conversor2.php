<!DOCTYPE html>
<html>
<head>
    <title>Conversor de Moneda</title>
</head>
<body>
    <?php
        $cantidad = isset($_GET['cantidad']) ? floatval($_GET['cantidad']) : 0;
        $tasa_conversion = 1.2; // Ejemplo: 1 Euro = 1.2 Dólares.
        $resultado = $cantidad * $tasa_conversion;
    ?>

    <h1>Conversor de Euros a Dólares</h1>

    <form method="get" action="">
        <label for="cantidad">Introduce la cantidad en euros:</label>
        <input type="number" id="cantidad" name="cantidad" step="0.01" value="<?php echo $cantidad; ?>">
        <button type="submit">Convertir</button>
    </form>

    <?php if ($cantidad > 0): ?>
        <p><?php echo $cantidad; ?> euros son aproximadamente <?php echo number_format($resultado, 2); ?> dólares.</p>
    <?php endif; ?>
</body>
</html>
