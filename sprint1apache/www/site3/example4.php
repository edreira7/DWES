<!DOCTYPE html>
<html>
<head>
    <title>Edad en 7 años</title>
</head>
<body>
    <?php
        $edad = isset($_GET['edad']) ? intval($_GET['edad']) : 0;
        $años_primo = 7; // Cambia este valor si tu número primo favorito es otro.
        $edad_en_X_años = $edad + $años_primo;
        $edad_jubilacion = 65;
    ?>

    <h1>Cálculo de edad en <?php echo $años_primo; ?> años</h1>

    <table border="1">
        <tr>
            <th>Edad Actual</th>
            <th>Edad en <?php echo $años_primo; ?> años</th>
            <th>Mensaje</th>
        </tr>
        <tr>
            <td><?php echo $edad; ?></td>
            <td><?php echo $edad_en_X_años; ?></td>
            <td>
                <?php
                    if ($edad_en_X_años >= $edad_jubilacion) {
                        echo "En $años_primo años tendrás edad de jubilación.";
                    } else {
                        echo "¡Disfruta de tu tiempo!";
                    }
                ?>
            </td>
        </tr>
    </table>
</body>
</html>
