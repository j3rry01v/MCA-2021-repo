<html>
<head><title>Insert Data in the form</title></head>
<body>
    <form action = "getdata.php" methord = "POST">
    Name : <input type ="text" name ="name_text">
    <br>
    <br>
    Roll Number :<input type = "text" name ="roll_no_text">
    <br><br>
    Address : <textarea name = "add_text" type ="textarea"></textarea>
    <br><br>
    Contact No :<input type = "text" name = "contact_text">
    <br> <br>
    Email ID : <input type = "text" name = "email_text">
    <input type = "Submit" name = "insert" value = "save">
    <input type = "reset" value = "cancel">
    </form>
</body>
</html>