<!DOCTYPE html>
<html>
<head>
    <title>Interest Calulator Results</title>
</head>
<body>
<!-- input the average account balance and if balance is 2000€ or more the interest is 0.5% -->

    <h1>Interest Results</h1>
    <?php
        if(isset($_POST['balance'])){
            $balance = $_POST['balance'];
            if($balance >= 2000){
                $interest = 0.5;
                echo "Enough Balance, monthly interest is: $interest .<br>"; 
            }
            else{
                $interest = 0;
                echo "balance too low, no interest included<br>";
            }
            $interest = $interest / 100;
            $interest = $interest * $balance;
            $mo2 = $interest * 2;
            $mo5 = $interest * 5;
            echo "your new balance will be after one month: $interest €, two months: $mo2, €, five months: $mo3,.";
        }
    ?>
    <a href="index.php">Back to Calculator</a>
</body>
</html>