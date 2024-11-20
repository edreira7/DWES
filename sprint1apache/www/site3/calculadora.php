<!DOCTYPE html>
<html>
<head>
    <title>Calculadora Aritmética</title>
</head>
<body>
    <h1>Calculadora Aritmética</h1>

    <form method="post" action="">
        <label for="numero1">Número 1:</label>
        <input type="number" id="numero1" name="numero1" step="0.01" required>
        <br><br>

        <label for="numero2">Número 2:</label>
        <input type="number" id="numero2" name="numero2" step="0.01" required>
        <br><br>

        <label for="operacion">Operación:</label>
        <select id="operacion" name="operacion" required>
            <option value="suma">Suma</option>
            <option value="resta">Resta</option>
            <option value="multiplicacion">Multiplicación</option>
            <option value="division">División</option>
        </select>
        <br><br>

        <button type="submit">Calcular</button>
    </form>

    <?php
    if ($_SERVER['REQUEST_METHOD'] == 'POST') {
        $numero1 = floatval($_POST['numero1']);
        $numero2 = floatval($_POST['numero2']);
        $operacion = $_POST['operacion'];
        $resultado = '';

        switch ($operacion) {
            case 'suma':
                $resultado = $numero1 + $numero2;
                break;
            case 'resta':
                $resultado = $numero1 - $numero2;
                break;
            case 'multiplicacion':
                $resultado = $numero1 * $numero2;
                break;
            case 'division':
                if ($numero2 != 0) {
                    $resultado = $numero1 / $numero2;
                } else {
                    $resultado = "Error: División entre 0 no permitida.";
                }
                break;
            default:
                $resultado = "Operación no válida.";
                break;
        }

        echo "<h2>Resultado: $resultado</h2>";
    }
    ?>
</body>
</html>
