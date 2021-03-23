<html>
<body bgcolor ="Yellowgreen">
<form action ="main.html" method="post">
<center>
<br>
<br>
<?php
include_once'conn.php';
if(isset($_POST['submit']))
{
$uname=$_POST['uname'];
$pass=$_POST['password'];
$gen=$_POST['gender'];
$em=$_POST['email'];
$ph1=$_POST['code'];
$ph2=$_POST['phno'];
$sql="INSERT INTO abcd123(uname,pass,gender,email,code,phno)VALUES('$uname','$pass','$gen','$em','$ph1','$ph2')";
if(mysqli_query($conn,$sql))
{
echo "record created Succesfully";
}
else
{
    echo "Error:".$sql."".mysqli_error($conn);
}
mysqli_close($conn);
}
?>
<br><br><input type="submit" value="Back to Home Page" name="submit">
</center>
</body>
</html>