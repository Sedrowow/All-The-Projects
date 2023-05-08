<!DOCTYPE html>
<html>
<head>
    <title>Netto Calulator Results</title>
</head>
<body>
<h1>Netto Results</h1>
    <?php
        if(isset($_POST['price'])){
            $price = $_POST['price'];
            $netto = $price / 1.19;
            $brutto = $price;
            $tax = $brutto - $netto;
            echo "Your netto price is: $netto €<br> you have bought for $brutto €<br> the tax deducted from this payment contains: $tax €";
        }
    ?>
<a href="index.php">Back to Calculator</a>
</body>
</html>
