#!/usr/bin/env python

from sys import argv

argumentos = argv
archivo = str(argv[1])

with open(archivo) as f:
    data = f.read()
