#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sys import argv
import subprocess
import time

print("-----------------------------------------------------------------")
print("Programando un BENCHMARK: ") 
print("Comparando la velocidad de 3 lenguajes (PHP, PYTHON, PERL)")
print("-----------------------------------------------------------------")


#########################################################################
#                       ESPECIFICACIÓN DE MI MÁQUINA                    #
#########################################################################

#print("Las especificaciones de mi máquina son: \n")
#subprocess.call(['lscpu'])


#########################################################################
#               TEST PARA COMPROBAR LA VELOCIDAD DE LECTURA             #
#########################################################################

# Nos declaramos los valores donde guardamos la media de cada prueba
media_python = 0
media_php = 0
media_perl = 0

# Variables que usaremos para obtener la media final (media/8)
media_py = 0
media_ph = 0
media_pe = 0

# Nos creamos un archivo de 6MB, para probar la lectura del mismo
print("\nCreando un archivo para el test de lectura con tamaño de 6MB.")
subprocess.call(['dd', 'if=/dev/zero', 'of=testarchivo6MB', 'bs=6291456', 'count=1'])

print("\nRealizando el TEST DE LECTURA, 10 mediciones para cada lenguaje.")
print("Esta prueba puede tardar unos segundos.\n")

r = open('datos_read.txt','w')
r.write("\nTEST DE LECTURA\n")
r.write("\nResultados para las 10 ejecuciones de cada lenguaje:\n")

# Hacemos que se ejecute 8 veces cada prueba
for i in range(0, 10, 1):
    # PYTHON
    start = time.time()
    subprocess.call(['python', 'readfilePYTHON.py', 'testarchivo6MB'])
    end = time.time()
    media_python = media_python + (end - start)
    r.write("- Ejecución " + str(i+1) + " en Python\t" + " " + str(media_python) + "\n")
    media_py += media_python

    # PHP
    start = time.time()
    subprocess.call(['php', 'readfilePHP.php', 'testarchivo6MB'])
    end = time.time()
    media_php = media_php + (end - start)
    r.write("- Ejecución " + str(i+1) + " en PHP\t\t" + " " + str(media_php) + "\n")
    media_ph += media_php

    # PERL
    start = time.time()
    subprocess.call(['perl', 'readfilePERL.pl', 'testarchivo6MB'])
    end = time.time()
    media_perl = media_perl + (end - start)
    r.write("- Ejecución " + str(i+1) + " en PERL\t\t" + " " + str(media_perl) + "\n")
    media_pe += media_perl

# Rellenamos el archivo que va a contener los resultados para el test de lectura
r.write("\nMedia en el test de lectura de cada lenguaje de programación:\n\n")
r.write("Python\t" + " " + str(media_py/10) + "\n")
r.write("PHP\t" + " " + str(media_ph/10) + "\n")
r.write("PERL\t" + " " + str(media_pe/10) + "\n")
r.close()


#########################################################################
#               TEST PARA COMPROBAR LA VELOCIDAD DE ESCRITURA           #
#########################################################################

# Asignamos a 0, las variables, borrando lo que puedan contener
media_python = 0
media_php = 0
media_perl = 0

# Asignamos a 0, las variables, borrando lo que puedan contener
media_py = 0
media_ph = 0
media_pe = 0

print("Realizando el TEST DE ESCRITURA, 10 mediciones para cada lenguaje.")
print("Esta prueba puede tardar unos segundos.\n")

l = open('datos_write.txt','w')
l.write("\nTEST DE ESCRITURA\n")
l.write("\nResultados para las 10 ejecuciones de cada lenguaje:\n")

for i in range(0, 10, 1):
    # PYTHON
    start = time.time()
    subprocess.call(['python', 'writefilePYTHON.py', 'writePYTHON.txt'])
    end = time.time()
    media_python = media_python + (end - start)
    l.write("- Ejecución " + str(i+1) + " en Python\t" + " " + str(media_python) + "\n")
    media_py += media_python

    # PHP
    start = time.time()
    subprocess.call(['php', 'writefilePHP.php', 'writePHP.txt'])
    end = time.time()
    media_php = media_php + (end - start)
    l.write("- Ejecución " + str(i+1) + " en PHP\t\t" + " " + str(media_php) + "\n")
    media_ph += media_php

    # PHP
    start = time.time()
    subprocess.call(['perl', 'writefilePERL.pl', 'writePERL.txt'])
    end = time.time()
    media_perl = media_perl + (end - start)
    l.write("- Ejecución " + str(i+1) + " en PERL\t\t" + " " + str(media_perl) + "\n")
    media_pe += media_perl

# Rellenamos el archivo que va a contener los resultados para el test de escritura
l.write("\nMedia en el test de escritura de cada lenguaje de programación:\n\n")
l.write("Python\t" + " " + str(media_py/10) + "\n")
l.write("PHP\t" + " " + str(media_ph/10) + "\n")
l.write("PERL\t" + " " + str(media_pe/10) + "\n")
l.close()

