<!DOCTYPE html>
<html>
<head>
    <title>Conversor de Unidades</title>
</head>
<body>
    <?php
        $cantidad = isset($_GET['cantidad']) ? floatval($_GET['cantidad']) : 0;
        $conversion = isset($_GET['conversion']) ? $_GET['conversion'] : 'euros_dolares';
        $resultado = 0;

        if ($conversion === 'euros_dolares') {
            $tasa_conversion = 1.2; // 1 Euro = 1.2 Dólares.
            $resultado = $cantidad * $tasa_conversion;
        } elseif ($conversion === 'pulgadas_cm') {
            $tasa_conversion = 2.54; // 1 Pulgada = 2.54 cm.
            $resultado = $cantidad * $tasa_conversion;
        } elseif ($conversion === 'pies_cm') {
            $tasa_conversion = 30.48; // 1 Pie = 30.48 cm.
            $resultado = $cantidad * $tasa_conversion;
        }
    ?>

    <h1>Conversor de Unidades</h1>

    <form method="get" action="">
        <label for="cantidad">Introduce la cantidad:</label>
        <input type="number" id="cantidad" name="cantidad" step="0.01" value="<?php echo $cantidad; ?>" required>

        <p>Selecciona la conversión:</p>
        <input type="radio" id="euros_dolares" name="conversion" value="euros_dolares" <?php if ($conversion === 'euros_dolares') echo 'checked'; ?>>
        <label for="euros_dolares">Euros a Dólares</label><br>

        <input type="radio" id="pulgadas_cm" name="conversion" value="pulgadas_cm" <?php if ($conversion === 'pulgadas_cm') echo 'checked'; ?>>
        <label for="pulgadas_cm">Pulgadas a Centímetros</label><br>

        <input type="radio" id="pies_cm" name="conversion" value="pies_cm" <?php if ($conversion === 'pies_cm') echo 'checked'; ?>>
        <label for="pies_cm">Pies a Centímetros</label><br>

        <button type="submit">Convertir</button>
    </form>

    <?php if ($cantidad > 0): ?>
        <p>Resultado: <?php echo number_format($resultado, 2); ?></p>
    <?php endif; ?>
</body>
</html>

