<?php

# What is the largest prime factor of the number 600851475143 ?

$num = 600851475143;
$counter = 2;
while ($counter < $num) {
	if ($num % $counter == 0) {
		$num = $num / $counter;
		$counter = 1;
	}
	$counter += 1;
}

echo $num;
echo "\n";

# 6857