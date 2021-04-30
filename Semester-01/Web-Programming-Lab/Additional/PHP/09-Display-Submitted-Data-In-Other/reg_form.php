<html>

<head>
    <title>Registration from</title>
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Akaya+Telivigala&display=swap" rel="stylesheet">
    <style>
        * {
            box-sizing: border-box;
        }

        body {
            background-color: #66717F;
            width: 100%;
            height: 100vh;
            padding-top: 4em;
        }

        .regform {
            background: #2E3740;
            color: #858f99;
            margin: auto;
            width: 50%;
            border: 1px solid black;
            box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px;
        }

        .content {
            margin: auto;
            width: 60%;
        }

        h1 {
            color: #6D7781;
            font-family: 'Akaya Telivigala', cursive;
            text-align: center;
        }

        legend {
            color: #6D7781;
            font-family: 'Akaya Telivigala', cursive;
        }

        label {
            font-family: 'Akaya Telivigala', cursive;
        }

        .first {
            text-align: right;
            width: 40%;
        }

        .button {
            margin-top: 10px;
            text-align: center;
        }

        input {
            padding: 5px 10px 5px 10px;
            height: 2em;
            border-radius: 5px;
            border: 1px solid #858f99;
            background: #2E3740;
            color: #858f99;
        }

        textarea {
            background: #2E3740;
            padding: 5px;
            border-radius: 5px;
            border: 1px solid #858f99;
            color: #858f99;
        }

        input[type="submit"] {
            margin-top: 3em;
            width: 8em;
            height: 2.5em;
            text-align: right;
            text-align: center;
            background-color: #1FCE6D;
            cursor: pointer;
            color: #2E3740;
        }

        input[type="text"],
        input[type="email"],
        input[type="number"],
        textarea,
        select {
            width: 90%;
        }

        input[type="tel"] {
            width: 80%;
        }

        .row {
            margin-top: 0.5em;
        }

        form {
            margin-top: 1em;
        }
    </style>
</head>

<body>
    <div class="regform">
        <h1>REGISTRATION FORM</h1>
        <hr width="50%">
        <div class="content">
            <form action="getdata.php" method="post">
                <div class="row">
                    <label for="name">Name:</label><br>
                </div>
                <div class="row">
                    <input type="text" name="name"><br>
                </div>

                <div class="row">
                    <label for="roll_no">Roll no:</label><br>
                </div>
                <div class="row">
                    <input type="number" name="roll_no"><br>
                </div>

                <div class="row">
                    <label for="address">Address:</label><br>
                </div>
                <div class="row">
                    <textarea name="address" id="" cols="21" rows="5"></textarea><br>
                </div>

                <div class="row"></div>
                <label for="ph">Contact No:</label><br>
                <div class="row"></div>
                <span>+91<input type="tel" name="ph" id="phone" style="width:85%;"></span><br>

                <div class="row">
                    <label for="mail">Email ID:</label><br>
                </div>
                <div class="row">
                    <input type="email" name="mail"><br>
                </div>

                <div class="row" style="display: flex;flex-direction: row-reverse;">
                    <input type="submit" value="submit" style="justify-content: end; margin:0 0 0 10px;">
                    <input type="submit" value="clear" style="margin:0 0 0 10px;">
                </div>
            </form>
        </div>
    </div>
</body>

</html>