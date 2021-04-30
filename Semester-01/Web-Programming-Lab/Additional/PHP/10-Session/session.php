<html>

<head>
    <title>Session</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100vh;
        }

        .message {
            margin: 2em;
            padding: 1em;
            color: #1F4F59;
            background-color: #c4e0f9;
            border: 1px solid #212226;
            box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
            border-radius: 5px;
            float: right;
        }
    </style>
</head>

<body>
    <div class="message">
        <?php
        session_start();
        if (isset($_SESSION['counter'])) {
            $_SESSION['counter'] += 1;
        } else {
            $_SESSION['counter'] = 1;
        }
        echo "You have visitted this page " . $_SESSION['counter'] . " time in this session";
        ?>
    </div>
</body>

</html>