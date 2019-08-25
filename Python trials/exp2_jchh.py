# -*- coding: utf-8 -*-

import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import fileinput
import sys, glob
import time

# Toma cualquier nombre del libro con comienzo "Busi_" y terminación ".txt"
archivos = glob.glob("../Management books/Busi_*.txt")
archivos.sort()

# Toma cada nombre de archivo
for linea in fileinput.input(archivos, openhook=fileinput.hook_encoded("utf-8")):
    if fileinput.isfirstline():
        # Files name
        book = fileinput.filename()

        book_1 = open(book, encoding="utf-8").read()

        book1 = nltk.word_tokenize(book_1)

        stop_words = set(stopwords.words('english')) 

        filtered_book = [w for w in book1 if not w in stop_words]

        single_character = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'eg',
                      'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'σi', 'σn',
                      'α', 'β', 'βn', 'xn', 'αv', 'ν', 'ϕ', 'ba', 'ip', 'fi', 'kr', 'fr', 'ij', 
                      'bd', 'nj', 'ac', 'bd', 'hk', 'gc', 'xg', 'dn', 'bi', 'mn', 'αu', 'hg', 
                      'zn', 'nth', 'mmc','gcd', 'cd', 'ub', 'di', 'ad', 'ab','gh', 'στ', 'σ', 'ai',
                      'cis', 'abab', 'aabb', 'id', 'sn', 'ax', 'bx', 'αn','px', 'acr', 'bcs', 'hn',
                      'kx', 'ζ', 'η', 'θ', 'κ', 'λ', 'μ', 'ξ', 'ρ', 'τ', 'φ', 'χ', 'ψ', 
                      'ω', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                      'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Ω', 'Ψ', 'Σ', 'Π', 
                      'Ξ', 'Λ', 'Θ', 'Δ', 'Γ', 'aβ', 'aβj', 'βj', 'gf', 'pn', 'bp', 'zp', 
                      'bch', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '|', '°', '¬', '!', '#', 
                      '$', '%', '&', '/', '(', ')', '=', '?', '¡', '¿', ',', ';', ':', '.', '-', '_',
                      '*', '+', '{', '}', '[', ']', '◦', '→', '➨', '∑')

        filtered_book = [w for w in filtered_book if not w in single_character]

        print(" -------- LIBRO -------- ")

        # Abre nuevo archivo para almacenar lista filtered_book
        file = open("archivoEj.txt", "w", encoding="utf-8")

        # Arreglo de caracteres numéricos
        number_caracter = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
        
        # Recorrido para escribir en archivo la lista fitered_book
        # Por cada item (palabra) en la lista filtered_book
        for item in filtered_book:
            # Si el primer caracter de cada item en la lista no es un número dentro de la lista number_caracter
            if not item[0] in number_caracter:
                # Escribe en el archivo
                file.write('\r%s' % item)

        file.close()
        print("Terminado")

        # Terminar con ctrl + c
        time.sleep(30)