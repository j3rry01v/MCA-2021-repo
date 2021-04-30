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
        <h1 align="center">String Count function</h1>
        <p align="center">
            <?php
            $sample_words = "This is Tutorials Class, learn programming tutorials here";
            echo "Number of strings in \"$sample_words\" is : ", str_word_count($sample_words);
            ?>
        </p>
    </div>

</body>

</html>