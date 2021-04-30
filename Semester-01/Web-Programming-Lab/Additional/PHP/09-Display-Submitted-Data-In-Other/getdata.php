<html>

<head>
    <title>GET THE DATA</title>
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Akaya+Telivigala&display=swap" rel="stylesheet">
    <style>
        h1 {
            color: #6D7781;
            font-family: 'Akaya Telivigala', cursive;
            text-align: center;
        }

        body {
            background-color: #66717F;
            width: 100%;
            height: 100vh;
            padding-top: 4em;
        }

        .content {
            background: #2E3740;
            color: #858f99;
            margin: auto;
            width: 50%;
            border: 1px solid black;
            padding: 1.5em;
            box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px;
            transform: translatey(50%);
        }

        .data {
            margin-top: auto;
            font-family: 'Akaya Telivigala', cursive;
            width: 80%;
        }
    </style>
</head>

<body>

    <div class="content">
        <h1>PERSONAL DATA</h1>
        <hr width="50%">
        <div class="data">
            <?php

            echo "<ul><li>Name:   " . $_POST["name"] . "</li>";
            echo "<li>Roll no:   " . $_POST["roll_no"] . "</li>";
            echo "<li>Address:   " . $_POST["address"] . "</li>";
            echo "<li>Contact no:   " . $_POST["ph"] . "</li>";
            echo "<li>Email ID:   " . $_POST["mail"] . "</li></ul>";

            ?>
        </div>

    </div>


</body>

</html>