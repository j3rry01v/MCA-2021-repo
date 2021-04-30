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
            margin-left: 16em;
        }
    </style>
</head>

<body>
    <div class="container">
        <h1 align="center">String length</h1>
        <p>
            <?php
            for ($row = 1; $row <= 8; $row++) {
                for ($star = 1; $star <= $row; $star++) {
                    echo "*";
                }
                echo "<br>";
            }
            ?>
        </p>
    </div>

</body>

</html>