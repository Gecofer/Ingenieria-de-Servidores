#!/usr/bin/perl

use warnings;
use strict;

my $archivo = shift @ARGV;

open(my $f, '>', $archivo);

for my $i (0..1000000) {
    print $f $i;
}

close $f;