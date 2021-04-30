<html>

<head>
    <title>Message</title>
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
            border-radius: 5px;
            float: right;
        }
    </style>
</head>

<body>
    <div class="message">
        <?php

        $afternoon = "Good afternoon!";
        $evening = "Good evening!";
        $late = "Working late?";
        $morning = "Good morning!";
        $friday = "Get ready for weakend!";

        //Get current hour
        $current_time = date('G');

        //Get the current day
        $current_day = date('i');

        if ($current_time >= 12 && $current_time <= 16)
            echo $afternoon;

        elseif ($current_time >= 17 && $current_time <= 24)
            echo $evening;

        elseif ($current_time >= 1 && $current_time <= 5)
            echo $late;

        elseif ($current_time >= 6 && $current_time <= 11)
            echo $morning;

        if ($current_day == "Friday")
            echo $friday;

        ?>
    </div>
</body>

</html>