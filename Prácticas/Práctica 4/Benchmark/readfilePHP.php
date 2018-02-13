<?php

	$archivo = $argv[1];
	$f = fopen($archivo, 'rb');

	while (($line = fgets($f)) !== false) {}

?>
