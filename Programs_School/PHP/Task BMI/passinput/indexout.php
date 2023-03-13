<html>
<head>
    <meta charset='utf-8'>
    <title>BMI-Calculator</title>
</head>
<body>
    <?php 
        $name = $_GET['name'];
        $size = $_GET['size'];
        $mass    = $_GET['mass'];
        $bmi = $mass / ($size * $size);
        echo "Hello $name, your BMI is $bmi";
    ?>
</body>
</html>