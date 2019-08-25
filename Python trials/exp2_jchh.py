# -*- coding: utf-8 -*-

import fileinput
import sys, glob

archivos = glob.glob("../Management books/Busi_*.txt")
archivos.sort()
for linea in fileinput.input(archivos, openhook=fileinput.hook_encoded("utf-8")):
    if fileinput.isfirstline():
    	# Files name
        ar = fileinput.filename()
        print(ar)