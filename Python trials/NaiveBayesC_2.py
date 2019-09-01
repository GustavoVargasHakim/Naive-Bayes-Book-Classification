#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 17:09:19 2019

@author: gustavo + clemente
"""

import numpy as np
import glob as g
import csv
import nltk

with open('training_books.csv', newline='', encoding="utf-8") as File:
    reader = csv.reader(File)

    # Palabras por cada libro
    new_math_rows = []
    new_bio_rows = []
    new_law_rows = []
    new_manag_rows = []
    new_soci_rows = []
    new_lite_rows = []
    
    # Palabras de cada género
    new_math_words = []
    new_bio_words = []
    new_law_words = []
    new_manag_words = []
    new_soci_words = []
    new_lite_words = []
    
    # Toma cada vector de cada libro
    for row in reader:
        if row:
            # Toma libros solo de Math
            if row[len(row) - 1] == '1':
                new_math_rows.append(row)
                  
                for i in range(0,20):
                    new_math_words.append(row[i])
             
            # Toma libros solo de Bio
            if row[len(row) - 1] == '2':
                new_bio_rows.append(row)
    
                for i in range(0,20):
                    new_bio_words.append(row[i])
    
            # Toma libros solo de Law
            if row[len(row) - 1] == '3':
                new_law_rows.append(row)
        
                for i in range(0,20):
                    new_law_words.append(row[i])
        
            # Toma libros solo de Manag
            if row[len(row) - 1] == '4':
                new_manag_rows.append(row)
        
                for i in range(0,20):
                    new_manag_words.append(row[i])
        
            # Toma libros solo de Soci
            if row[len(row) - 1] == '5':
                new_soci_rows.append(row)
        
                for i in range(0,20):
                    new_soci_words.append(row[i])
        
            # Toma libros solo de Lite
            if row[len(row) - 1] == '6':
                new_lite_rows.append(row)
        
                for i in range(0,20):
                    new_lite_words.append(row[i])

'''Leer las features para cada genero'''
             
with open('math_features.csv', newline='', encoding="utf-8") as File:
    reader = csv.reader(File)
    math_features = list(reader)[0]

with open('biology_features.csv', newline='', encoding="utf-8") as File:
    reader = csv.reader(File)
    bio_features = list(reader)[0]

with open('business_features.csv', newline='', encoding="utf-8") as File:
    reader = csv.reader(File)
    busi_features = list(reader)[0] 

with open('law_features.csv', newline='', encoding="utf-8") as File:
    reader = csv.reader(File)
    law_features = list(reader)[0]

with open('Social_features.csv', newline='', encoding="utf-8") as File:
    reader = csv.reader(File)
    soci_features = list(reader)[0]

with open('literature_features.csv', newline='', encoding="latin-1") as File:
    reader = csv.reader(File)
    literature_features = list(reader)[0]

#Probabilidades a priori
p_c1 = 20/120        
p_c2 = 100/120

'''Clasificador 1 (matematicas)'''

c1 = [new_math_rows] #Si son de matematicas
c2 = [new_bio_rows, new_law_rows, new_manag_rows, new_soci_rows, new_lite_rows] #No son de matematicas

#Obtener la matriz binaria total de todos los libros
binary_matrix = []
for i in range(20) :
    oo_math = []
    for word in math_features :
        if word in c1[0][i] :
            oo_math.append(1)
        else :
            oo_math.append(0)
    binary_matrix.append(oo_math)

other1 = c2[0]
for i in range(20) :
    oo_math = []
    for word in math_features :
        if word in other1[0][i] :
            oo_math.append(1)
        else :
            oo_math.append(0)
    binary_matrix.append(oo_math)

other2 = c2[1]
for i in range(20) :
    oo_math = []
    for word in math_features :
        if word in other2[0][i] :
            oo_math.append(1)
        else :
            oo_math.append(0)
    binary_matrix.append(oo_math)

other3 = c2[2]
for i in range(20) :
    oo_math = []
    for word in math_features :
        if word in other3[0][i] :
            oo_math.append(1)
        else :
            oo_math.append(0)
    binary_matrix.append(oo_math)

other4 = c2[3]
for i in range(20) :
    oo_math = []
    for word in math_features :
        if word in other4[0][i] :
            oo_math.append(1)
        else :
            oo_math.append(0)
    binary_matrix.append(oo_math)

other5 = c2[4]
for i in range(20) :
    oo_math = []
    for word in math_features :
        if word in other5[0][i] :
            oo_math.append(1)
        else :
            oo_math.append(0)
    binary_matrix.append(oo_math)

#Tablas de frecuencias para ambas clases
binary_c1 = []
binary_c2 = []
for i in range(20) :
    binary_c1.append(binary_matrix[i])
binary_c1 = np.asarray(binary_c1)

for i in range(20,120) :
    binary_c2.append(binary_matrix[i])
binary_c2 = np.asarray(binary_c2)

zeros_c1 = []
ones_c1 = []
for i in range(20) :
    z = 0
    o = 0
    for j in range(20) :
        if binary_c1[j][i] == 0 :
            z = z + 1
        if binary_c1[j][i] == 1 :
            o = o + 1
    zeros_c1.append(z)
    ones_c1.append(o)

zeros_c2 = []
ones_c2 = []
for i in range(20) :
    z = 0
    o = 0
    for j in range(100) :
        if binary_c2[j][i] == 0 :
            z = z + 1
        if binary_c2[j][i] == 1 :
            o = o + 1
    zeros_c2.append(z)
    ones_c2.append(o)

zeros_c1 = np.asarray(zeros_c1)
zeros_c2 = np.asarray(zeros_c2)
ones_c1 = np.asarray(ones_c1)
ones_c2 = np.asarray(ones_c2)

#Correccion de laplace
zeros_c2 = zeros_c2 + 1
ones_c2 = ones_c2 + 1 
zeros_c1 = zeros_c1 + 1
ones_c1 = ones_c1 + 1

#Probabilidades (normalización)
sum_c1 = 22
sum_c2 = 102

zeros_c1 = zeros_c1/sum_c1
ones_c1 = ones_c1/sum_c1

zeros_c2 = zeros_c2/sum_c2
ones_c2 = ones_c2/sum_c2

#Clasificador de matematicas entrenado
p_math_c1 = np.asarray([zeros_c1, ones_c1]) #Probabilidades de ser de matematicas
p_math_c2 = np.asarray([zeros_c2, ones_c2]) #Probabilidades de no ser de matematicas

'''Clasificador 2 (biologia)'''

c1 = [new_bio_rows] #Si son de biologia
c2 = [new_math_rows, new_law_rows, new_manag_rows, new_soci_rows, new_lite_rows] #No son de biologia

#Obtener la matriz binaria total de todos los libros
binary_matrix = []
for i in range(20) :
    oo_bio = []
    for word in bio_features :
        if word in c1[0][i] :
            oo_bio.append(1)
        else :
            oo_bio.append(0)
    binary_matrix.append(oo_bio)

other1 = c2[0]
for i in range(20) :
    oo_bio = []
    for word in bio_features :
        if word in other1[0][i] :
            oo_bio.append(1)
        else :
            oo_bio.append(0)
    binary_matrix.append(oo_bio)

other2 = c2[1]
for i in range(20) :
    oo_bio = []
    for word in bio_features :
        if word in other2[0][i] :
            oo_bio.append(1)
        else :
            oo_bio.append(0)
    binary_matrix.append(oo_bio)

other3 = c2[2]
for i in range(20) :
    oo_bio = []
    for word in bio_features :
        if word in other3[0][i] :
            oo_bio.append(1)
        else :
            oo_bio.append(0)
    binary_matrix.append(oo_bio)

other4 = c2[3]
for i in range(20) :
    oo_bio = []
    for word in bio_features :
        if word in other4[0][i] :
            oo_bio.append(1)
        else :
            oo_bio.append(0)
    binary_matrix.append(oo_bio)

other5 = c2[4]
for i in range(20) :
    oo_bio = []
    for word in bio_features :
        if word in other5[0][i] :
            oo_bio.append(1)
        else :
            oo_bio.append(0)
    binary_matrix.append(oo_bio)
    
#Tablas de frecuencias para ambas clases
binary_c1 = []
binary_c2 = []
for i in range(20) :
    binary_c1.append(binary_matrix[i])
binary_c1 = np.asarray(binary_c1)

for i in range(20,120) :
    binary_c2.append(binary_matrix[i])
binary_c2 = np.asarray(binary_c2)

zeros_c1 = []
ones_c1 = []
for i in range(20) :
    z = 0
    o = 0
    for j in range(20) :
        if binary_c1[j][i] == 0 :
            z = z + 1
        if binary_c1[j][i] == 1 :
            o = o + 1
    zeros_c1.append(z)
    ones_c1.append(o)

zeros_c2 = []
ones_c2 = []
for i in range(20) :
    z = 0
    o = 0
    for j in range(100) :
        if binary_c2[j][i] == 0 :
            z = z + 1
        if binary_c2[j][i] == 1 :
            o = o + 1
    zeros_c2.append(z)
    ones_c2.append(o)

zeros_c1 = np.asarray(zeros_c1)
zeros_c2 = np.asarray(zeros_c2)
ones_c1 = np.asarray(ones_c1)
ones_c2 = np.asarray(ones_c2)

#Correccion de laplace
zeros_c2 = zeros_c2 + 1
ones_c2 = ones_c2 + 1 
zeros_c1 = zeros_c1 + 1
ones_c1 = ones_c1 + 1

#Probabilidades (normalización)
sum_c1 = 22
sum_c2 = 102

zeros_c1 = zeros_c1/sum_c1
ones_c1 = ones_c1/sum_c1

zeros_c2 = zeros_c2/sum_c2
ones_c2 = ones_c2/sum_c2

#Clasificador de matematicas entrenado
p_bio_c1 = np.asarray([zeros_c1, ones_c1]) #Probabilidades de ser de biologia
p_bio_c2 = np.asarray([zeros_c2, ones_c2]) #Probabilidades de no ser de biologia

'''Clasificador 3 (leyes)'''

c1 = [new_law_rows] #Si son de leyes
c2 = [new_math_rows, new_bio_rows, new_manag_rows, new_soci_rows, new_lite_rows] #No son de leyes

#Obtener la matriz binaria total de todos los libros
binary_matrix = []
for i in range(20) :
    oo_law = []
    for word in law_features :
        if word in c1[0][i] :
            oo_law.append(1)
        else :
            oo_law.append(0)
    binary_matrix.append(oo_law)

other1 = c2[0]
for i in range(20) :
    oo_law = []
    for word in law_features :
        if word in other1[0][i] :
            oo_law.append(1)
        else :
            oo_law.append(0)
    binary_matrix.append(oo_law)

other2 = c2[1]
for i in range(20) :
    oo_law = []
    for word in law_features :
        if word in other2[0][i] :
            oo_law.append(1)
        else :
            oo_law.append(0)
    binary_matrix.append(oo_law)

other3 = c2[2]
for i in range(20) :
    oo_law = []
    for word in law_features :
        if word in other3[0][i] :
            oo_law.append(1)
        else :
            oo_law.append(0)
    binary_matrix.append(oo_law)

other4 = c2[3]
for i in range(20) :
    oo_law = []
    for word in law_features :
        if word in other4[0][i] :
            oo_law.append(1)
        else :
            oo_law.append(0)
    binary_matrix.append(oo_law)

other5 = c2[4]
for i in range(20) :
    oo_law = []
    for word in law_features :
        if word in other5[0][i] :
            oo_law.append(1)
        else :
            oo_law.append(0)
    binary_matrix.append(oo_law)
    
#Tablas de frecuencias para ambas clases
binary_c1 = []
binary_c2 = []
for i in range(20) :
    binary_c1.append(binary_matrix[i])
binary_c1 = np.asarray(binary_c1)

for i in range(20,120) :
    binary_c2.append(binary_matrix[i])
binary_c2 = np.asarray(binary_c2)

zeros_c1 = []
ones_c1 = []
for i in range(20) :
    z = 0
    o = 0
    for j in range(20) :
        if binary_c1[j][i] == 0 :
            z = z + 1
        if binary_c1[j][i] == 1 :
            o = o + 1
    zeros_c1.append(z)
    ones_c1.append(o)

zeros_c2 = []
ones_c2 = []
for i in range(20) :
    z = 0
    o = 0
    for j in range(100) :
        if binary_c2[j][i] == 0 :
            z = z + 1
        if binary_c2[j][i] == 1 :
            o = o + 1
    zeros_c2.append(z)
    ones_c2.append(o)

zeros_c1 = np.asarray(zeros_c1)
zeros_c2 = np.asarray(zeros_c2)
ones_c1 = np.asarray(ones_c1)
ones_c2 = np.asarray(ones_c2)

#Correccion de laplace
zeros_c2 = zeros_c2 + 1
ones_c2 = ones_c2 + 1 
zeros_c1 = zeros_c1 + 1
ones_c1 = ones_c1 + 1

#Probabilidades (normalización)
sum_c1 = 22
sum_c2 = 102

zeros_c1 = zeros_c1/sum_c1
ones_c1 = ones_c1/sum_c1

zeros_c2 = zeros_c2/sum_c2
ones_c2 = ones_c2/sum_c2

#Clasificador de matematicas entrenado
p_law_c1 = np.asarray([zeros_c1, ones_c1]) #Probabilidades de ser de leyes
p_law_c2 = np.asarray([zeros_c2, ones_c2]) #Probabilidades de no ser de leyes

'''Clasificador 4 (negocios)'''

c1 = [new_manag_rows] #Si son de negocios
c2 = [new_math_rows, new_bio_rows, new_law_rows, new_soci_rows, new_lite_rows] #No son de negocios

#Obtener la matriz binaria total de todos los libros
binary_matrix = []
for i in range(20) :
    oo_busi = []
    for word in busi_features :
        if word in c1[0][i] :
            oo_busi.append(1)
        else :
            oo_busi.append(0)
    binary_matrix.append(oo_busi)

other1 = c2[0]
for i in range(20) :
    oo_busi = []
    for word in busi_features :
        if word in other1[0][i] :
            oo_busi.append(1)
        else :
            oo_busi.append(0)
    binary_matrix.append(oo_busi)

other2 = c2[1]
for i in range(20) :
    oo_busi = []
    for word in busi_features :
        if word in other2[0][i] :
            oo_busi.append(1)
        else :
            oo_busi.append(0)
    binary_matrix.append(oo_busi)

other3 = c2[2]
for i in range(20) :
    oo_busi = []
    for word in busi_features :
        if word in other3[0][i] :
            oo_busi.append(1)
        else :
            oo_busi.append(0)
    binary_matrix.append(oo_busi)

other4 = c2[3]
for i in range(20) :
    oo_busi = []
    for word in busi_features :
        if word in other4[0][i] :
            oo_busi.append(1)
        else :
            oo_busi.append(0)
    binary_matrix.append(oo_busi)

other5 = c2[4]
for i in range(20) :
    oo_busi = []
    for word in busi_features :
        if word in other5[0][i] :
            oo_busi.append(1)
        else :
            oo_busi.append(0)
    binary_matrix.append(oo_busi)
    
#Tablas de frecuencias para ambas clases
binary_c1 = []
binary_c2 = []
for i in range(20) :
    binary_c1.append(binary_matrix[i])
binary_c1 = np.asarray(binary_c1)

for i in range(20,120) :
    binary_c2.append(binary_matrix[i])
binary_c2 = np.asarray(binary_c2)

zeros_c1 = []
ones_c1 = []
for i in range(20) :
    z = 0
    o = 0
    for j in range(20) :
        if binary_c1[j][i] == 0 :
            z = z + 1
        if binary_c1[j][i] == 1 :
            o = o + 1
    zeros_c1.append(z)
    ones_c1.append(o)

zeros_c2 = []
ones_c2 = []
for i in range(20) :
    z = 0
    o = 0
    for j in range(100) :
        if binary_c2[j][i] == 0 :
            z = z + 1
        if binary_c2[j][i] == 1 :
            o = o + 1
    zeros_c2.append(z)
    ones_c2.append(o)

zeros_c1 = np.asarray(zeros_c1)
zeros_c2 = np.asarray(zeros_c2)
ones_c1 = np.asarray(ones_c1)
ones_c2 = np.asarray(ones_c2)

#Correccion de laplace
zeros_c2 = zeros_c2 + 1
ones_c2 = ones_c2 + 1 
zeros_c1 = zeros_c1 + 1
ones_c1 = ones_c1 + 1

#Probabilidades (normalización)
sum_c1 = 22
sum_c2 = 102

zeros_c1 = zeros_c1/sum_c1
ones_c1 = ones_c1/sum_c1

zeros_c2 = zeros_c2/sum_c2
ones_c2 = ones_c2/sum_c2

#Clasificador de matematicas entrenado
p_busi_c1 = np.asarray([zeros_c1, ones_c1]) #Probabilidades de ser de negocios
p_busi_c2 = np.asarray([zeros_c2, ones_c2]) #Probabilidades de no ser de negocios

'''Clasificador 5 (ciencias sociales)'''

c1 = [new_soci_rows] #Si son de ciencias sociales
c2 = [new_math_rows, new_bio_rows, new_law_rows, new_manag_rows, new_lite_rows] #No son de ciencias sociales

#Obtener la matriz binaria total de todos los libros
binary_matrix = []
for i in range(20) :
    oo_soci = []
    for word in soci_features :
        if word in c1[0][i] :
            oo_soci.append(1)
        else :
            oo_soci.append(0)
    binary_matrix.append(oo_soci)

other1 = c2[0]
for i in range(20) :
    oo_soci = []
    for word in soci_features :
        if word in other1[0][i] :
            oo_soci.append(1)
        else :
            oo_soci.append(0)
    binary_matrix.append(oo_soci)

other2 = c2[1]
for i in range(20) :
    oo_soci = []
    for word in soci_features :
        if word in other2[0][i] :
            oo_soci.append(1)
        else :
            oo_soci.append(0)
    binary_matrix.append(oo_soci)

other3 = c2[2]
for i in range(20) :
    oo_soci = []
    for word in soci_features :
        if word in other3[0][i] :
            oo_soci.append(1)
        else :
            oo_soci.append(0)
    binary_matrix.append(oo_soci)

other4 = c2[3]
for i in range(20) :
    oo_soci = []
    for word in soci_features :
        if word in other4[0][i] :
            oo_soci.append(1)
        else :
            oo_soci.append(0)
    binary_matrix.append(oo_soci)

other5 = c2[4]
for i in range(20) :
    oo_soci = []
    for word in soci_features :
        if word in other5[0][i] :
            oo_soci.append(1)
        else :
            oo_soci.append(0)
    binary_matrix.append(oo_soci)
    
#Tablas de frecuencias para ambas clases
binary_c1 = []
binary_c2 = []
for i in range(20) :
    binary_c1.append(binary_matrix[i])
binary_c1 = np.asarray(binary_c1)

for i in range(20,120) :
    binary_c2.append(binary_matrix[i])
binary_c2 = np.asarray(binary_c2)

zeros_c1 = []
ones_c1 = []
for i in range(20) :
    z = 0
    o = 0
    for j in range(20) :
        if binary_c1[j][i] == 0 :
            z = z + 1
        if binary_c1[j][i] == 1 :
            o = o + 1
    zeros_c1.append(z)
    ones_c1.append(o)

zeros_c2 = []
ones_c2 = []
for i in range(20) :
    z = 0
    o = 0
    for j in range(100) :
        if binary_c2[j][i] == 0 :
            z = z + 1
        if binary_c2[j][i] == 1 :
            o = o + 1
    zeros_c2.append(z)
    ones_c2.append(o)

zeros_c1 = np.asarray(zeros_c1)
zeros_c2 = np.asarray(zeros_c2)
ones_c1 = np.asarray(ones_c1)
ones_c2 = np.asarray(ones_c2)

#Correccion de laplace
zeros_c2 = zeros_c2 + 1
ones_c2 = ones_c2 + 1 
zeros_c1 = zeros_c1 + 1
ones_c1 = ones_c1 + 1

#Probabilidades (normalización)
sum_c1 = 22
sum_c2 = 102

zeros_c1 = zeros_c1/sum_c1
ones_c1 = ones_c1/sum_c1

zeros_c2 = zeros_c2/sum_c2
ones_c2 = ones_c2/sum_c2

#Clasificador de matematicas entrenado
p_soci_c1 = np.asarray([zeros_c1, ones_c1]) #Probabilidades de ser de ciencias sociales
p_soci_c2 = np.asarray([zeros_c2, ones_c2]) #Probabilidades de no ser de ciencias sociales

'''Clasificador 6 (literatura general)'''

c1 = [new_lite_rows] #Si son de literatura general
c2 = [new_math_rows, new_bio_rows, new_law_rows, new_manag_rows, new_soci_rows] #No son de literatura general

#Obtener la matriz binaria total de todos los libros
binary_matrix = []
for i in range(20) :
    oo_lit = []
    for word in literature_features :
        if word in c1[0][i] :
            oo_lit.append(1)
        else :
            oo_lit.append(0)
    binary_matrix.append(oo_lit)

other1 = c2[0]
for i in range(20) :
    oo_lit = []
    for word in literature_features :
        if word in other1[0][i] :
            oo_lit.append(1)
        else :
            oo_lit.append(0)
    binary_matrix.append(oo_lit)

other2 = c2[1]
for i in range(20) :
    oo_lit = []
    for word in literature_features :
        if word in other2[0][i] :
            oo_lit.append(1)
        else :
            oo_lit.append(0)
    binary_matrix.append(oo_lit)

other3 = c2[2]
for i in range(20) :
    oo_lit = []
    for word in literature_features :
        if word in other3[0][i] :
            oo_lit.append(1)
        else :
            oo_lit.append(0)
    binary_matrix.append(oo_lit)

other4 = c2[3]
for i in range(20) :
    oo_lit = []
    for word in literature_features :
        if word in other4[0][i] :
            oo_lit.append(1)
        else :
            oo_lit.append(0)
    binary_matrix.append(oo_lit)

other5 = c2[4]
for i in range(20) :
    oo_lit = []
    for word in literature_features :
        if word in other5[0][i] :
            oo_lit.append(1)
        else :
            oo_lit.append(0)
    binary_matrix.append(oo_lit)
    
#Tablas de frecuencias para ambas clases
binary_c1 = []
binary_c2 = []
for i in range(20) :
    binary_c1.append(binary_matrix[i])
binary_c1 = np.asarray(binary_c1)

for i in range(20,120) :
    binary_c2.append(binary_matrix[i])
binary_c2 = np.asarray(binary_c2)

zeros_c1 = []
ones_c1 = []
for i in range(20) :
    z = 0
    o = 0
    for j in range(20) :
        if binary_c1[j][i] == 0 :
            z = z + 1
        if binary_c1[j][i] == 1 :
            o = o + 1
    zeros_c1.append(z)
    ones_c1.append(o)

zeros_c2 = []
ones_c2 = []
for i in range(20) :
    z = 0
    o = 0
    for j in range(100) :
        if binary_c2[j][i] == 0 :
            z = z + 1
        if binary_c2[j][i] == 1 :
            o = o + 1
    zeros_c2.append(z)
    ones_c2.append(o)

zeros_c1 = np.asarray(zeros_c1)
zeros_c2 = np.asarray(zeros_c2)
ones_c1 = np.asarray(ones_c1)
ones_c2 = np.asarray(ones_c2)

#Correccion de laplace
zeros_c2 = zeros_c2 + 1
ones_c2 = ones_c2 + 1 
zeros_c1 = zeros_c1 + 1
ones_c1 = ones_c1 + 1

#Probabilidades (normalización)
sum_c1 = 22
sum_c2 = 102

zeros_c1 = zeros_c1/sum_c1
ones_c1 = ones_c1/sum_c1

zeros_c2 = zeros_c2/sum_c2
ones_c2 = ones_c2/sum_c2

#Clasificador de matematicas entrenado
p_lit_c1 = np.asarray([zeros_c1, ones_c1]) #Probabilidades de ser de literatura general
p_lit_c2 = np.asarray([zeros_c2, ones_c2]) #Probabilidades de no ser de literatura general

'''Cargar libros de validacion'''
with open('validation_books.csv', newline='', encoding="utf-8") as File:
    reader = csv.reader(File)

    # libros de cada género
    v_math_rows = []
    v_bio_rows = []
    v_law_rows = []
    v_manag_rows = []
    v_soci_rows = []
    v_lite_rows = []
    
    # Toma cada vector de cada libro
    for row in reader:
        if row:
            # Toma libros solo de Math
            if row[len(row) - 1] == '1':
                v_math_rows.append(row)

            # Toma libros solo de Bio
            if row[len(row) - 1] == '2':
                v_bio_rows.append(row)

            # Toma libros solo de Law
            if row[len(row) - 1] == '3':
                v_law_rows.append(row)

            # Toma libros solo de Manag
            if row[len(row) - 1] == '4':
                v_manag_rows.append(row)

            # Toma libros solo de Soci
            if row[len(row) - 1] == '5':
                v_soci_rows.append(row)

            # Toma libros solo de Lite
            if row[len(row) - 1] == '6':
                v_lite_rows.append(row)

'''Clasificar libros de matematicas'''
