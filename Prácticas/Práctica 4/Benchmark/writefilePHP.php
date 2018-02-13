<?php

	$archivo = $argv[1];
	$myarchivo = fopen($archivo, "w");
	
	for( $i=0; $i<1000000; $i++) {
  		fwrite($myarchivo, $i);
	}

	fclose($myarchivo);
	
?>
