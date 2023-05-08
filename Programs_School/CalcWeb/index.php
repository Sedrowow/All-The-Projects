<html>
<header>
    <title>Choose the Calculator</title>
</header>
<body>
    <h1>Choose the Calculator</h1>
    <form method="post">
        <input type="radio" name="calc" value="add">NettoCALC<br>
        <input type="radio" name="calc" value="sub">Interest CALC<br>
        <input type="radio" name="calc" value="mul">Discount calc<br>
        <input type="submit" value="Submit">
    </form>
    <?php
        if(isset($_POST['calc'])){
            $calc = $_POST['calc'];
            if($calc == "add"){
                header("Location: netto.php");
            }
            if($calc == "sub"){
                header("Location: interest.php");
            }
            if($calc == "mul"){
                header("Location: discount.php");
            }
        }

    ?>
</body>
</html>