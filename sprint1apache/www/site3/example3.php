<!DOCTYPE html>
<html>
<head>
    <title>Cálculo de Jubilación</title>
</head>
<body>
    <?php
        $edad = isset($_GET['edad']) ? intval($_GET['edad']) : 0;
        $edad_jubilacion = 65;

        if ($edad >= $edad_jubilacion) {
            echo "<h1>¡Felicidades! Ya puedes jubilarte.</h1>";
        } else {
            $años_restantes = $edad_jubilacion - $edad;
            echo "<h1>Te quedan $años_restantes años para jubilarte.</h1>";
        }
    ?>
</body>
</html>
