# -*- coding: utf-8 -*-

import fileinput
import sys, glob

# Toma cualquier nombre del libro con comienzo "Busi_" y terminación ".txt"
archivos = glob.glob("../Management books/Busi_*.txt")
archivos.sort()

# Toma cada nombre de archivo
for linea in fileinput.input(archivos, openhook=fileinput.hook_encoded("utf-8")):
    if fileinput.isfirstline():
    	# Files name
        ar = fileinput.filename()
        print(ar)