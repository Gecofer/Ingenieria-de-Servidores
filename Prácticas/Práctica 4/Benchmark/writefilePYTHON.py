#!/usr/bin/env python

from sys import argv
import subprocess

argumentos = argv
archivo = str(argv[1])

f = open(archivo, 'w')

for i in range(0, 1000000, 1):
    f.write(str(i))
