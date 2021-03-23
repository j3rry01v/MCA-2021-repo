<html>
<body bgcolor="Lightblue">
<form action="main.html" method="post">
<center>
<?php
include_once 'conn.php';
if(isset($_POST['submit']))
{
$uid=$_POST['id'];
$fname=$_POST['uname'];
$pass=$_POST['pass'];
$gen=$_POST['gender'];
$em=$_POST['email'];
$ph1=$_POST['code'];
$ph2=$_POST['phno'];
$sql="UPDATE abcd123 SET
Name='$fname',Password='$pass',Gender='$gen', Email='$em',Phonenumber='$ph1'
Phonenumber='$ph2' where frmid='$uid'";
if(mysqli_query($conn,$sql))
{
echo "Updated Successfully !<br><br>";
}
else
{
echo "Error:".$sql."".mysqli_error($conn);
}
mysqli_close($conn);
}
?>
<br>
<br>
<input type="submit" value=""Back to home page" name="submit">
</center>
</body>
</html> 