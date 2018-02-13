#!/usr/bin/perl

use warnings;
use strict;

my $archivo = shift @ARGV;

open(my $f, '<:encoding(UTF-8)', $archivo);

while (my $row = <$f>) {
    chomp $row;
    my $fila =  "$row\n";
}