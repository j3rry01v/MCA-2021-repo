<html>

<head>
    <title>String Reverse</title>
    <style>
        .container {
            width: 40%;
            color: #d8d8d8;
            background-color: #49826d;
            border-radius: 8px;
            transform: translatey(40%);
            margin: auto;
            padding: 2em;
        }

        p {
            color: #b1ffb3;
        }
    </style>
</head>

<body>
    <div class="container">
        <h1 align="center">FACTORIAL</h1>
        <p align="center">
            <?php
            $num = 3;
            $factorial = 1;

            for ($x = $num; $x >= 1; $x--) {
                $factorial = $factorial * $x;
            }

            echo "The factorial of $num is : $factorial";
            ?>
        </p>
    </div>

</body>

</html>