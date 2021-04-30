<html>

<head>
	<title>substr function</title>
	<style>
		.container {
			width: 40%;
			color: #d8d8d8;
			background-color: #49826d;
			border-radius: 8px;
			margin: auto;
			padding: 2em;
		}

		hr {
			margin-bottom: 1.5em;
		}

		p {
			color: #2b2b2b;
		}

		span {
			color: #2b2b2b;
		}
	</style>
</head>

<body>
	<div class="container">
		<h1 align="center">String and Variable functions</h1>
		<hr align="center" width="70%">
		<h2 align="center">Vardump function</h2>
		<hr align="center" width="30%">

		<?php
		$val1 = 678;
		$val2 = "a678";
		$val3 = "678";
		$val4 = "BetterThanLike.com";
		$val5 = 698.99;
		$val6 = +125689.66;
		echo "$val1 : <span>", var_dump($val1), "</span><br>";
		echo "$val2 : <span>", var_dump($val2), "</span><br>";
		echo "$val3 : <span>", var_dump($val3), "</span><br>";
		echo "$val4 : <span>", var_dump($val4), "</span><br>";
		echo "$val5 : <span>", var_dump($val5), "</span><br>";
		echo "$val6 : <span>", var_dump($val6), "</span><br>";
		?>
		<h2 align="center">subcmp function</h2>
		<hr align="center" width="30%">
		<?php
		$str1 = "Anil";
		$str2 = "anil";
		echo "Comaparing \"$str1\" and \"$str2\" is :";
		if (strcmp($str1, $str2)) {
			echo "<span>2 strings are different</span><br>";
		} else {
			echo "<span>2 strings are same</span><br>";
		}

		$str3 = "anil";
		$str4 = "anil";
		echo "Comaparing \"$str3\" and \"$str4\" is :";
		if (strcmp($str3, $str4)) {
			echo "<span>2 strings are different</span><br>";
		} else {
			echo "<span>2 strings are same</span><br>";
		}
		?>

		<h2 align="center">substr function</h2>
		<hr align="center" width="30%">
		<b> If the start is non-negative, the returned string will start at the start'th position in string, start from 0</b><br><br>
		<?php
		echo "<p>->Substring with positive start :" . substr("abcdef", 2) . "<br><br></p>";
		?>
		<b> If the start is negative, the returned string will start at the start'th charecter in string, from the end of the string</b><br><br>
		<?php
		echo "<p>->Substring with negative start :" . substr("abcdef", -2) . "<br><br></p>";
		?>
		<b> If the start is less than or equal to start charecter long, false will return</b><br><br>
		<?php
		echo "<p>->Start is <= string :" . substr("abcdef", -2) . "<br><br></p>";
		?>

		<h1 align="center">strpos function</h1>
		<hr align="center" width="30%">
		<?php
		$string = "i am anil";
		$pos = strpos($string, "nil");
		if ($pos === false)
			echo "String 'nil' in " . $string . " NOT FOUND<br>";
		else
			echo "String 'nil' in \"$string\" FOUND..!<br>";
		echo "<span><br><br><center>FINISHED</center><br><span>";
		?>
	</div>

</body>

</html>