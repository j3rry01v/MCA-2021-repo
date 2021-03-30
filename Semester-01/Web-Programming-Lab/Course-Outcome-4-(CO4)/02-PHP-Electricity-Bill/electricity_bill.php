<html>
 <head>
  <title>form</title>
  </head>

<center>
<body bgcolor="#69807d">
<br>
<br>
<h1 >ELECTRCITY BILL</h3>

<form action='' method="POST">
<table>
 <tr>
  <td> Name</td>
  <td> <input type="text" id="name" name="name"></td>
 </tr>
 <tr>
  <td> Consumer Number</td>
  <td> 
<input type="number" name="consumer" >
  </td>
 </tr>
 <tr>
  <td> Unit used</td>
  <td> 
<input type="number" name="unit" >
  </td>
 </tr>
</table>
<br>
<input type="submit" value="Check bill" name="submit" style="background:green;color:white">

<h3 style="color:red"></h3>
<h3 style="color:green"></h3>
</form>

<?php
$a="<h3 style='color:red'>";
$b="<h3 style='color:green'>";
$c="</h3>";
if(isset($_POST["submit"]))
{
$name=$_POST["name"];
    if($name==NULL)
    {
        echo "$a Name can not be Empty $c";
        exit;
    }
    else
    {
        if(!preg_match("^[a-zA-Z]^",$name))
        {
        echo "$a Only characters and white space allowed in names $b";
        exit;
        }
    }

$consumer=$_POST["consumer"];
if($consumer==NULL)
{
    echo "$a Consumer number cannot be empty $c";
    exit;
}
else
{
    if(mb_strlen($consumer)!=10)
    {
    echo "$a consumer number must contain 10 digit only $b";
    exit;
    }
}

$unit=$_POST["unit"];
if($unit==NULL)
{
    echo "$a Enter unit used $c";
    exit;
}
else
{
    if($unit<=100)
        $amount=3*$unit;
    elseif($unit<=200)
        $amount=4*$unit;
    elseif($unit<=300)
        $amount=5*$unit;
    else
        $amount=6*$unit;
}



$m=$a.'Payment server offline....'.$c;
$t= "<h4> <u>BILL</u></h4><table id='bill' border='0px' width='20%' height='10%'> <tr><th class='h'>Name</th><th class='h'>Unit</th><th class='h'>Amount</th></tr>";
echo "$t <tr><th>$name</th><th>$unit</th><th>$amount</th></tr>";
echo "<tr><th colspan='3' class='t'>total\t:$amount</th></tr></table>";

}

?>
</center>
</body>
</html>
