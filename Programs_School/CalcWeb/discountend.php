<html>
    <header>
        <title>Discount CALC results</title>
    </header>
<body>
<h1>Discount CALC results</h1>
    <!-- calculate discount based on bought amount 500 1000 and greater than 1000 -->
    <?php 
        if(isset($_POST['price per piece']) && isset($_POST['bought amount'])){
            $price = $_POST['price per piece'];
            $amount = $_POST['bought amount'];
            if($amount < 500){
                $discount = 2;
            }
            if($amount >= 500 && $amount < 1000){
                $discount = 5;
            }
            if($amount >= 1000 && $timecustomer < 10){
                $discount = 15;
            }
            else{
                $discount = 10;
            }
            $discount = $discount / 100;
            $discount = $discount * $Price;
            $discount = $Price - $discount;
            echo "The sold price per piece is: $discount, the price to pay is: $discount * $amount";
            };
    ?>
    <a href="index.php">Back to Calculator</a>
</body>
</html>