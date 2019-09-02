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

'''Clasificar libros de matematicas (validacion)'''
##Probabilidad de que sea de matematicas
#Obtener matriz binaria de cada libro de validacion
math_binary = []
for i in range(10) :
    oo_math = []
    for word in math_features :
        if word in v_math_rows[i] :
            oo_math.append(1)
        else :
            oo_math.append(0)
    math_binary.append(oo_math)
    
#Calculando probabilidades para cada libro segun sus palabras clave
mmath_prob_matrix = []
for j in range(10) :
    prob_math = p_c1
    for i in range(20) :
        if math_binary[j][i] == 1 :
            prob_math = prob_math * p_math_c1[0][i]
        
        if math_binary[j][i] == 0 :
            prob_math = prob_math * p_math_c1[1][i]
            
    mmath_prob_matrix.append(prob_math)
    
##Probabilidad de que sea de biologia
#Obtener matriz binaria de cada libro de validacion
math_binary = []
for i in range(10) :
    oo_math = []
    for word in bio_features :
        if word in v_math_rows[i] :
            oo_math.append(1)
        else :
            oo_math.append(0)
    math_binary.append(oo_math)
    
#Calculando probabilidades para cada libro segun sus palabras clave
mbio_prob_matrix = []
for j in range(10) :
    prob_bio = p_c1
    for i in range(20) :
        if math_binary[j][i] == 1 :
            prob_bio = prob_bio * p_bio_c1[0][i]
        
        if math_binary[j][i] == 0 :
            prob_bio = prob_bio * p_bio_c1[1][i]
            
    mbio_prob_matrix.append(prob_bio)

##Probabilidad de que sea de leyes
#Obtener matriz binaria de cada libro de validacion
math_binary = []
for i in range(10) :
    oo_math = []
    for word in law_features :
        if word in v_math_rows[i] :
            oo_math.append(1)
        else :
            oo_math.append(0)
    math_binary.append(oo_math)
    
#Calculando probabilidades para cada libro segun sus palabras clave
mlaw_prob_matrix = []
for j in range(10) :
    prob_law = p_c1
    for i in range(20) :
        if math_binary[j][i] == 1 :
            prob_law = prob_law * p_law_c1[0][i]
        
        if math_binary[j][i] == 0 :
            prob_law = prob_law * p_law_c1[1][i]
            
    mlaw_prob_matrix.append(prob_law)

##Probabilidad de que sea de negocios
#Obtener matriz binaria de cada libro de validacion
math_binary = []
for i in range(10) :
    oo_math = []
    for word in busi_features :
        if word in v_math_rows[i] :
            oo_math.append(1)
        else :
            oo_math.append(0)
    math_binary.append(oo_math)
    
#Calculando probabilidades para cada libro segun sus palabras clave
mbusi_prob_matrix = []
for j in range(10) :
    prob_busi = p_c1
    for i in range(20) :
        if math_binary[j][i] == 1 :
            prob_busi = prob_busi * p_busi_c1[0][i]
        
        if math_binary[j][i] == 0 :
            prob_busi = prob_busi * p_busi_c1[1][i]
            
    mbusi_prob_matrix.append(prob_busi)

##Probabilidad de que sea de ciencias sociales
#Obtener matriz binaria de cada libro de validacion
math_binary = []
for i in range(10) :
    oo_math = []
    for word in soci_features :
        if word in v_math_rows[i] :
            oo_math.append(1)
        else :
            oo_math.append(0)
    math_binary.append(oo_math)
    
#Calculando probabilidades para cada libro segun sus palabras clave
msoci_prob_matrix = []
for j in range(10) :
    prob_soci = p_c1
    for i in range(20) :
        if math_binary[j][i] == 1 :
            prob_soci = prob_soci * p_soci_c1[0][i]
        
        if math_binary[j][i] == 0 :
            prob_soci = prob_soci * p_soci_c1[1][i]
            
    msoci_prob_matrix.append(prob_soci)

##Probabilidad de que sea de literatura general
#Obtener matriz binaria de cada libro de validacion
math_binary = []
for i in range(10) :
    oo_math = []
    for word in literature_features :
        if word in v_math_rows[i] :
            oo_math.append(1)
        else :
            oo_math.append(0)
    math_binary.append(oo_math)
    
#Calculando probabilidades para cada libro segun sus palabras clave
mlit_prob_matrix = []
for j in range(10) :
    prob_lit = p_c1
    for i in range(20) :
        if math_binary[j][i] == 1 :
            prob_lit = prob_lit * p_lit_c1[0][i]
        
        if math_binary[j][i] == 0 :
            prob_lit = prob_lit * p_lit_c1[1][i]
            
    mlit_prob_matrix.append(prob_lit)

#Se tienen 6 vectores de probabilidades, cada uno tiene 10 probabilidades, para
#los 10 libros de validacion.

#Comparas cada columna de probabilidad (para cada libro)
probabilities_math = [mmath_prob_matrix, mbio_prob_matrix, mlaw_prob_matrix,
                      mbusi_prob_matrix, msoci_prob_matrix, mlit_prob_matrix]

books_prob_math = []
for i in range(10) :
    winner = probabilities_math[0][0] #Partir de que se trata de matematicas
    genre = 1
    for j in range(6) :
        if winner < probabilities_math[j][i] :
            winner = probabilities_math[j][i]
            genre = j + 1
    books_prob_math.append(genre)

print(books_prob_math)

'''Clasificar libros de biologia (validacion)'''
##Probabilidad de que sea de matematicas
#Obtener matriz binaria de cada libro de validacion
bio_binary = []
for i in range(10) :
    oo_bio = []
    for word in math_features :
        if word in v_bio_rows[i] :
            oo_bio.append(1)
        else :
            oo_bio.append(0)
    bio_binary.append(oo_bio)
    
#Calculando probabilidades para cada libro segun sus palabras clave
bmath_prob_matrix = []
for j in range(10) :
    prob_math = p_c1
    for i in range(20) :
        if bio_binary[j][i] == 1 :
            prob_math = prob_math * p_math_c1[0][i]
        
        if bio_binary[j][i] == 0 :
            prob_math = prob_math * p_math_c1[1][i]
            
    bmath_prob_matrix.append(prob_math)

##Probabilidad de que sea de biologia
#Obtener matriz binaria de cada libro de validacion
bio_binary = []
for i in range(10) :
    oo_bio = []
    for word in bio_features :
        if word in v_bio_rows[i] :
            oo_bio.append(1)
        else :
            oo_bio.append(0)
    bio_binary.append(oo_bio)
    
#Calculando probabilidades para cada libro segun sus palabras clave
bbio_prob_matrix = []
for j in range(10) :
    prob_bio = p_c1
    for i in range(20) :
        if bio_binary[j][i] == 1 :
            prob_bio = prob_bio * p_bio_c1[0][i]
        
        if bio_binary[j][i] == 0 :
            prob_bio = prob_bio * p_bio_c1[1][i]
            
    bbio_prob_matrix.append(prob_bio)

##Probabilidad de que sea de leyes
#Obtener matriz binaria de cada libro de validacion
bio_binary = []
for i in range(10) :
    oo_bio = []
    for word in law_features :
        if word in v_bio_rows[i] :
            oo_bio.append(1)
        else :
            oo_bio.append(0)
    bio_binary.append(oo_bio)
    
#Calculando probabilidades para cada libro segun sus palabras clave
blaw_prob_matrix = []
for j in range(10) :
    prob_law = p_c1
    for i in range(20) :
        if bio_binary[j][i] == 1 :
            prob_law = prob_law * p_law_c1[0][i]
        
        if bio_binary[j][i] == 0 :
            prob_law = prob_law * p_law_c1[1][i]
            
    blaw_prob_matrix.append(prob_law)
    
##Probabilidad de que sea de negocios
#Obtener matriz binaria de cada libro de validacion
bio_binary = []
for i in range(10) :
    oo_bio = []
    for word in busi_features :
        if word in v_bio_rows[i] :
            oo_bio.append(1)
        else :
            oo_bio.append(0)
    bio_binary.append(oo_bio)
    
#Calculando probabilidades para cada libro segun sus palabras clave
bbusi_prob_matrix = []
for j in range(10) :
    prob_busi = p_c1
    for i in range(20) :
        if bio_binary[j][i] == 1 :
            prob_busi = prob_busi * p_busi_c1[0][i]
        
        if bio_binary[j][i] == 0 :
            prob_busi = prob_busi * p_busi_c1[1][i]
            
    bbusi_prob_matrix.append(prob_busi)

##Probabilidad de que sea de ciencias sociales
#Obtener matriz binaria de cada libro de validacion
bio_binary = []
for i in range(10) :
    oo_bio = []
    for word in soci_features :
        if word in v_bio_rows[i] :
            oo_bio.append(1)
        else :
            oo_bio.append(0)
    bio_binary.append(oo_bio)
    
#Calculando probabilidades para cada libro segun sus palabras clave
bsoci_prob_matrix = []
for j in range(10) :
    prob_soci = p_c1
    for i in range(20) :
        if bio_binary[j][i] == 1 :
            prob_soci = prob_soci * p_soci_c1[0][i]
        
        if bio_binary[j][i] == 0 :
            prob_soci = prob_soci * p_soci_c1[1][i]
            
    bsoci_prob_matrix.append(prob_soci)

##Probabilidad de que sea de literatura
#Obtener matriz binaria de cada libro de validacion
bio_binary = []
for i in range(10) :
    oo_bio = []
    for word in literature_features :
        if word in v_bio_rows[i] :
            oo_bio.append(1)
        else :
            oo_bio.append(0)
    bio_binary.append(oo_bio)
    
#Calculando probabilidades para cada libro segun sus palabras clave
blit_prob_matrix = []
for j in range(10) :
    prob_lit = p_c1
    for i in range(20) :
        if bio_binary[j][i] == 1 :
            prob_lit = prob_lit * p_lit_c1[0][i]
        
        if bio_binary[j][i] == 0 :
            prob_lit = prob_lit * p_lit_c1[1][i]
            
    blit_prob_matrix.append(prob_lit)

#Se tienen 6 vectores de probabilidades, cada uno tiene 10 probabilidades, para
#los 10 libros de validacion.

#Comparas cada columna de probabilidad (para cada libro)
probabilities_bio = [bmath_prob_matrix, bbio_prob_matrix, blaw_prob_matrix,
                      bbusi_prob_matrix, bsoci_prob_matrix, blit_prob_matrix]

books_prob_bio = []
for i in range(10) :
    winner = probabilities_bio[0][0] #Partir de que se trata de matematicas
    genre = 1
    for j in range(6) :
        if winner < probabilities_bio[j][i] :
            winner = probabilities_bio[j][i]
            genre = j + 1
    books_prob_bio.append(genre)

print(books_prob_bio)

'''Clasificar libros de leyes (validacion)'''
##Probabilidad de que sea de matematicas
#Obtener matriz binaria de cada libro de validacion
law_binary = []
for i in range(10) :
    oo_law = []
    for word in math_features :
        if word in v_law_rows[i] :
            oo_law.append(1)
        else :
            oo_law.append(0)
    law_binary.append(oo_law)
    
#Calculando probabilidades para cada libro segun sus palabras clave
lmath_prob_matrix = []
for j in range(10) :
    prob_math = p_c1
    for i in range(20) :
        if law_binary[j][i] == 1 :
            prob_math = prob_math * p_math_c1[0][i]
        
        if law_binary[j][i] == 0 :
            prob_math = prob_math * p_math_c1[1][i]
            
    lmath_prob_matrix.append(prob_math)

##Probabilidad de que sea de biologia
#Obtener matriz binaria de cada libro de validacion
law_binary = []
for i in range(10) :
    oo_law = []
    for word in bio_features :
        if word in v_law_rows[i] :
            oo_law.append(1)
        else :
            oo_law.append(0)
    law_binary.append(oo_law)
    
#Calculando probabilidades para cada libro segun sus palabras clave
lbio_prob_matrix = []
for j in range(10) :
    prob_bio = p_c1
    for i in range(20) :
        if law_binary[j][i] == 1 :
            prob_bio = prob_bio * p_bio_c1[0][i]
        
        if law_binary[j][i] == 0 :
            prob_bio = prob_bio * p_bio_c1[1][i]
            
    lbio_prob_matrix.append(prob_bio)

##Probabilidad de que sea de leyes
#Obtener matriz binaria de cada libro de validacion
law_binary = []
for i in range(10) :
    oo_law = []
    for word in law_features :
        if word in v_law_rows[i] :
            oo_law.append(1)
        else :
            oo_law.append(0)
    law_binary.append(oo_law)
    
#Calculando probabilidades para cada libro segun sus palabras clave
llaw_prob_matrix = []
for j in range(10) :
    prob_law = p_c1
    for i in range(20) :
        if law_binary[j][i] == 1 :
            prob_law = prob_law * p_law_c1[0][i]
        
        if law_binary[j][i] == 0 :
            prob_law = prob_law * p_law_c1[1][i]
            
    llaw_prob_matrix.append(prob_law)
    
##Probabilidad de que sea de negocios
#Obtener matriz binaria de cada libro de validacion
law_binary = []
for i in range(10) :
    oo_law = []
    for word in busi_features :
        if word in v_law_rows[i] :
            oo_law.append(1)
        else :
            oo_law.append(0)
    law_binary.append(oo_law)
    
#Calculando probabilidades para cada libro segun sus palabras clave
lbusi_prob_matrix = []
for j in range(10) :
    prob_busi = p_c1
    for i in range(20) :
        if law_binary[j][i] == 1 :
            prob_busi = prob_busi * p_busi_c1[0][i]
        
        if law_binary[j][i] == 0 :
            prob_busi = prob_busi * p_busi_c1[1][i]
            
    lbusi_prob_matrix.append(prob_busi)

##Probabilidad de que sea de ciencias sociales
#Obtener matriz binaria de cada libro de validacion
law_binary = []
for i in range(10) :
    oo_law = []
    for word in soci_features :
        if word in v_law_rows[i] :
            oo_law.append(1)
        else :
            oo_law.append(0)
    law_binary.append(oo_law)
    
#Calculando probabilidades para cada libro segun sus palabras clave
lsoci_prob_matrix = []
for j in range(10) :
    prob_soci = p_c1
    for i in range(20) :
        if law_binary[j][i] == 1 :
            prob_soci = prob_soci * p_soci_c1[0][i]
        
        if law_binary[j][i] == 0 :
            prob_soci = prob_soci * p_soci_c1[1][i]
            
    lsoci_prob_matrix.append(prob_soci)

##Probabilidad de que sea de literatura
#Obtener matriz binaria de cada libro de validacion
law_binary = []
for i in range(10) :
    oo_law = []
    for word in literature_features :
        if word in v_law_rows[i] :
            oo_law.append(1)
        else :
            oo_law.append(0)
    law_binary.append(oo_law)
    
#Calculando probabilidades para cada libro segun sus palabras clave
llit_prob_matrix = []
for j in range(10) :
    prob_lit = p_c1
    for i in range(20) :
        if law_binary[j][i] == 1 :
            prob_lit = prob_lit * p_lit_c1[0][i]
        
        if law_binary[j][i] == 0 :
            prob_lit = prob_lit * p_lit_c1[1][i]
            
    llit_prob_matrix.append(prob_lit)

#Se tienen 6 vectores de probabilidades, cada uno tiene 10 probabilidades, para
#los 10 libros de validacion.

#Comparas cada columna de probabilidad (para cada libro)
probabilities_law = [lmath_prob_matrix, lbio_prob_matrix, llaw_prob_matrix,
                      lbusi_prob_matrix, lsoci_prob_matrix, llit_prob_matrix]

books_prob_law = []
for i in range(10) :
    winner = probabilities_law[0][0] #Partir de que se trata de matematicas
    genre = 1
    for j in range(6) :
        if winner < probabilities_law[j][i] :
            winner = probabilities_law[j][i]
            genre = j + 1
    books_prob_law.append(genre)

print(books_prob_law)

'''Clasificar libros de negocios (validacion)'''
##Probabilidad de que sea de matematicas
#Obtener matriz binaria de cada libro de validacion
busi_binary = []
for i in range(10) :
    oo_busi = []
    for word in math_features :
        if word in v_manag_rows[i] :
            oo_busi.append(1)
        else :
            oo_busi.append(0)
    busi_binary.append(oo_busi)
    
#Calculando probabilidades para cada libro segun sus palabras clave
bumath_prob_matrix = []
for j in range(10) :
    prob_math = p_c1
    for i in range(20) :
        if busi_binary[j][i] == 1 :
            prob_math = prob_math * p_math_c1[0][i]
        
        if busi_binary[j][i] == 0 :
            prob_math = prob_math * p_math_c1[1][i]
            
    bumath_prob_matrix.append(prob_math)
    
##Probabilidad de que sea de biologia
#Obtener matriz binaria de cada libro de validacion
busi_binary = []
for i in range(10) :
    oo_busi= []
    for word in bio_features :
        if word in v_manag_rows[i] :
            oo_busi.append(1)
        else :
            oo_busi.append(0)
    busi_binary.append(oo_busi)
    
#Calculando probabilidades para cada libro segun sus palabras clave
bubio_prob_matrix = []
for j in range(10) :
    prob_bio = p_c1
    for i in range(20) :
        if busi_binary[j][i] == 1 :
            prob_bio = prob_bio * p_bio_c1[0][i]
        
        if busi_binary[j][i] == 0 :
            prob_bio = prob_bio * p_bio_c1[1][i]
            
    bubio_prob_matrix.append(prob_bio)

##Probabilidad de que sea de leyes
#Obtener matriz binaria de cada libro de validacion
busi_binary = []
for i in range(10) :
    oo_busi = []
    for word in law_features :
        if word in v_manag_rows[i] :
            oo_busi.append(1)
        else :
            oo_busi.append(0)
    busi_binary.append(oo_busi)
    
#Calculando probabilidades para cada libro segun sus palabras clave
bulaw_prob_matrix = []
for j in range(10) :
    prob_law = p_c1
    for i in range(20) :
        if busi_binary[j][i] == 1 :
            prob_law = prob_law * p_law_c1[0][i]
        
        if busi_binary[j][i] == 0 :
            prob_law = prob_law * p_law_c1[1][i]
            
    bulaw_prob_matrix.append(prob_law)

##Probabilidad de que sea de negocios
#Obtener matriz binaria de cada libro de validacion
busi_binary = []
for i in range(10) :
    oo_busi = []
    for word in busi_features :
        if word in v_manag_rows[i] :
            oo_busi.append(1)
        else :
            oo_busi.append(0)
    busi_binary.append(oo_busi)
    
#Calculando probabilidades para cada libro segun sus palabras clave
bubusi_prob_matrix = []
for j in range(10) :
    prob_busi = p_c1
    for i in range(20) :
        if busi_binary[j][i] == 1 :
            prob_busi = prob_busi * p_busi_c1[0][i]
        
        if busi_binary[j][i] == 0 :
            prob_busi = prob_busi * p_busi_c1[1][i]
            
    bubusi_prob_matrix.append(prob_busi)

##Probabilidad de que sea de ciencias sociales
#Obtener matriz binaria de cada libro de validacion
busoci_binary = []
for i in range(10) :
    oo_busi = []
    for word in soci_features :
        if word in v_manag_rows[i] :
            oo_busi.append(1)
        else :
            oo_busi.append(0)
    busoci_binary.append(oo_busi)
    
#Calculando probabilidades para cada libro segun sus palabras clave
busoci_prob_matrix = []
for j in range(10) :
    prob_soci = p_c1
    for i in range(20) :
        if busi_binary[j][i] == 1 :
            prob_soci = prob_soci * p_soci_c1[0][i]
        
        if busi_binary[j][i] == 0 :
            prob_soci = prob_soci * p_soci_c1[1][i]
            
    busoci_prob_matrix.append(prob_soci)

##Probabilidad de que sea de literatura general
#Obtener matriz binaria de cada libro de validacion
busi_binary = []
for i in range(10) :
    oo_busi = []
    for word in literature_features :
        if word in v_manag_rows[i] :
            oo_busi.append(1)
        else :
            oo_busi.append(0)
    busi_binary.append(oo_busi)
    
#Calculando probabilidades para cada libro segun sus palabras clave
bulit_prob_matrix = []
for j in range(10) :
    prob_lit = p_c1
    for i in range(20) :
        if busi_binary[j][i] == 1 :
            prob_lit = prob_lit * p_lit_c1[0][i]
        
        if busi_binary[j][i] == 0 :
            prob_lit = prob_lit * p_lit_c1[1][i]
            
    bulit_prob_matrix.append(prob_lit)

#Se tienen 6 vectores de probabilidades, cada uno tiene 10 probabilidades, para
#los 10 libros de validacion.

#Comparas cada columna de probabilidad (para cada libro)
probabilities_busi = [bumath_prob_matrix, bubio_prob_matrix, bulaw_prob_matrix,
                      bubusi_prob_matrix, busoci_prob_matrix, bulit_prob_matrix]

books_prob_busi = []
for i in range(10) :
    winner = probabilities_busi[0][0] #Partir de que se trata de matematicas
    genre = 1
    for j in range(6) :
        if winner < probabilities_busi[j][i] :
            winner = probabilities_busi[j][i]
            genre = j + 1
    books_prob_busi.append(genre)

print(books_prob_busi)

'''Clasificar libros de ciencias sociales (validacion)'''
##Probabilidad de que sea de matematicas
#Obtener matriz binaria de cada libro de validacion
soci_binary = []
for i in range(10) :
    oo_soci = []
    for word in math_features :
        if word in v_soci_rows[i] :
            oo_soci.append(1)
        else :
            oo_soci.append(0)
    soci_binary.append(oo_soci)
    
#Calculando probabilidades para cada libro segun sus palabras clave
smath_prob_matrix = []
for j in range(10) :
    prob_math = p_c1
    for i in range(20) :
        if soci_binary[j][i] == 1 :
            prob_math = prob_math * p_math_c1[0][i]
        
        if soci_binary[j][i] == 0 :
            prob_math = prob_math * p_math_c1[1][i]
            
    smath_prob_matrix.append(prob_math)
    
##Probabilidad de que sea de biologia
#Obtener matriz binaria de cada libro de validacion
soci_binary = []
for i in range(10) :
    oo_soci= []
    for word in bio_features :
        if word in v_soci_rows[i] :
            oo_soci.append(1)
        else :
            oo_soci.append(0)
    soci_binary.append(oo_soci)
    
#Calculando probabilidades para cada libro segun sus palabras clave
sbio_prob_matrix = []
for j in range(10) :
    prob_bio = p_c1
    for i in range(20) :
        if soci_binary[j][i] == 1 :
            prob_bio = prob_bio * p_bio_c1[0][i]
        
        if soci_binary[j][i] == 0 :
            prob_bio = prob_bio * p_bio_c1[1][i]
            
    sbio_prob_matrix.append(prob_bio)

##Probabilidad de que sea de leyes
#Obtener matriz binaria de cada libro de validacion
soci_binary = []
for i in range(10) :
    oo_soci = []
    for word in law_features :
        if word in v_soci_rows[i] :
            oo_soci.append(1)
        else :
            oo_soci.append(0)
    soci_binary.append(oo_soci)
    
#Calculando probabilidades para cada libro segun sus palabras clave
slaw_prob_matrix = []
for j in range(10) :
    prob_law = p_c1
    for i in range(20) :
        if soci_binary[j][i] == 1 :
            prob_law = prob_law * p_law_c1[0][i]
        
        if soci_binary[j][i] == 0 :
            prob_law = prob_law * p_law_c1[1][i]
            
    slaw_prob_matrix.append(prob_law)

##Probabilidad de que sea de negocios
#Obtener matriz binaria de cada libro de validacion
soci_binary = []
for i in range(10) :
    oo_soci = []
    for word in soci_features :
        if word in v_soci_rows[i] :
            oo_soci.append(1)
        else :
            oo_soci.append(0)
    soci_binary.append(oo_soci)
    
#Calculando probabilidades para cada libro segun sus palabras clave
sbusi_prob_matrix = []
for j in range(10) :
    prob_busi = p_c1
    for i in range(20) :
        if soci_binary[j][i] == 1 :
            prob_busi = prob_busi * p_busi_c1[0][i]
        
        if soci_binary[j][i] == 0 :
            prob_busi = prob_busi * p_busi_c1[1][i]
            
    sbusi_prob_matrix.append(prob_busi)

##Probabilidad de que sea de ciencias sociales
#Obtener matriz binaria de cada libro de validacion
soci_binary = []
for i in range(10) :
    oo_soci = []
    for word in soci_features :
        if word in v_soci_rows[i] :
            oo_soci.append(1)
        else :
            oo_soci.append(0)
    soci_binary.append(oo_soci)
    
#Calculando probabilidades para cada libro segun sus palabras clave
ssoci_prob_matrix = []
for j in range(10) :
    prob_soci = p_c1
    for i in range(20) :
        if soci_binary[j][i] == 1 :
            prob_soci = prob_soci * p_soci_c1[0][i]
        
        if soci_binary[j][i] == 0 :
            prob_soci = prob_soci * p_soci_c1[1][i]
            
    ssoci_prob_matrix.append(prob_soci)

##Probabilidad de que sea de literatura general
#Obtener matriz binaria de cada libro de validacion
soci_binary = []
for i in range(10) :
    oo_soci = []
    for word in literature_features :
        if word in v_soci_rows[i] :
            oo_soci.append(1)
        else :
            oo_soci.append(0)
    soci_binary.append(oo_soci)
    
#Calculando probabilidades para cada libro segun sus palabras clave
slit_prob_matrix = []
for j in range(10) :
    prob_lit = p_c1
    for i in range(20) :
        if soci_binary[j][i] == 1 :
            prob_lit = prob_lit * p_lit_c1[0][i]
        
        if soci_binary[j][i] == 0 :
            prob_lit = prob_lit * p_lit_c1[1][i]
            
    slit_prob_matrix.append(prob_lit)

#Se tienen 6 vectores de probabilidades, cada uno tiene 10 probabilidades, para
#los 10 libros de validacion.

#Comparas cada columna de probabilidad (para cada libro)
probabilities_soci = [smath_prob_matrix, sbio_prob_matrix, slaw_prob_matrix,
                      sbusi_prob_matrix, ssoci_prob_matrix, slit_prob_matrix]

books_prob_soci = []
for i in range(10) :
    winner = probabilities_soci[0][0] #Partir de que se trata de matematicas
    genre = 1
    for j in range(6) :
        if winner < probabilities_soci[j][i] :
            winner = probabilities_soci[j][i]
            genre = j + 1
    books_prob_soci.append(genre)

print(books_prob_soci)

'''Clasificar libros de literatura general (validacion)'''
##Probabilidad de que sea de matematicas
#Obtener matriz binaria de cada libro de validacion
lit_binary = []
for i in range(10) :
    oo_lit = []
    for word in math_features :
        if word in v_lite_rows[i] :
            oo_lit.append(1)
        else :
            oo_lit.append(0)
    lit_binary.append(oo_lit)
    
#Calculando probabilidades para cada libro segun sus palabras clave
limath_prob_matrix = []
for j in range(10) :
    prob_math = p_c1
    for i in range(20) :
        if lit_binary[j][i] == 1 :
            prob_math = prob_math * p_math_c1[0][i]
        
        if lit_binary[j][i] == 0 :
            prob_math = prob_math * p_math_c1[1][i]
            
    limath_prob_matrix.append(prob_math)
    
##Probabilidad de que sea de biologia
#Obtener matriz binaria de cada libro de validacion
lit_binary = []
for i in range(10) :
    oo_lit= []
    for word in bio_features :
        if word in v_lite_rows[i] :
            oo_lit.append(1)
        else :
            oo_lit.append(0)
    lit_binary.append(oo_lit)
    
#Calculando probabilidades para cada libro segun sus palabras clave
libio_prob_matrix = []
for j in range(10) :
    prob_bio = p_c1
    for i in range(20) :
        if lit_binary[j][i] == 1 :
            prob_bio = prob_bio * p_bio_c1[0][i]
        
        if lit_binary[j][i] == 0 :
            prob_bio = prob_bio * p_bio_c1[1][i]
            
    libio_prob_matrix.append(prob_bio)

##Probabilidad de que sea de leyes
#Obtener matriz binaria de cada libro de validacion
lit_binary = []
for i in range(10) :
    oo_lit = []
    for word in law_features :
        if word in v_lite_rows[i] :
            oo_lit.append(1)
        else :
            oo_lit.append(0)
    lit_binary.append(oo_lit)
    
#Calculando probabilidades para cada libro segun sus palabras clave
lilaw_prob_matrix = []
for j in range(10) :
    prob_law = p_c1
    for i in range(20) :
        if lit_binary[j][i] == 1 :
            prob_law = prob_law * p_law_c1[0][i]
        
        if lit_binary[j][i] == 0 :
            prob_law = prob_law * p_law_c1[1][i]
            
    lilaw_prob_matrix.append(prob_law)

##Probabilidad de que sea de negocios
#Obtener matriz binaria de cada libro de validacion
lit_binary = []
for i in range(10) :
    oo_lit = []
    for word in soci_features :
        if word in v_lite_rows[i] :
            oo_lit.append(1)
        else :
            oo_lit.append(0)
    lit_binary.append(oo_lit)
    
#Calculando probabilidades para cada libro segun sus palabras clave
libusi_prob_matrix = []
for j in range(10) :
    prob_busi = p_c1
    for i in range(20) :
        if lit_binary[j][i] == 1 :
            prob_busi = prob_busi * p_busi_c1[0][i]
        
        if lit_binary[j][i] == 0 :
            prob_busi = prob_busi * p_busi_c1[1][i]
            
    libusi_prob_matrix.append(prob_busi)

##Probabilidad de que sea de ciencias sociales
#Obtener matriz binaria de cada libro de validacion
lit_binary = []
for i in range(10) :
    oo_lit = []
    for word in soci_features :
        if word in v_lite_rows[i] :
            oo_lit.append(1)
        else :
            oo_lit.append(0)
    lit_binary.append(oo_lit)
    
#Calculando probabilidades para cada libro segun sus palabras clave
lisoci_prob_matrix = []
for j in range(10) :
    prob_soci = p_c1
    for i in range(20) :
        if lit_binary[j][i] == 1 :
            prob_soci = prob_soci * p_soci_c1[0][i]
        
        if lit_binary[j][i] == 0 :
            prob_soci = prob_soci * p_soci_c1[1][i]
            
    lisoci_prob_matrix.append(prob_soci)

##Probabilidad de que sea de literatura general
#Obtener matriz binaria de cada libro de validacion
lit_binary = []
for i in range(10) :
    oo_lit = []
    for word in literature_features :
        if word in v_lite_rows[i] :
            oo_lit.append(1)
        else :
            oo_lit.append(0)
    lit_binary.append(oo_lit)
    
#Calculando probabilidades para cada libro segun sus palabras clave
lilit_prob_matrix = []
for j in range(10) :
    prob_lit = p_c1
    for i in range(20) :
        if lit_binary[j][i] == 1 :
            prob_lit = prob_lit * p_lit_c1[0][i]
        
        if lit_binary[j][i] == 0 :
            prob_lit = prob_lit * p_lit_c1[1][i]
            
    lilit_prob_matrix.append(prob_lit)

#Se tienen 6 vectores de probabilidades, cada uno tiene 10 probabilidades, para
#los 10 libros de validacion.

#Comparas cada columna de probabilidad (para cada libro)
probabilities_lit = [limath_prob_matrix, libio_prob_matrix, lilaw_prob_matrix,
                      libusi_prob_matrix, lisoci_prob_matrix, lilit_prob_matrix]

books_prob_lit = []
for i in range(10) :
    winner = probabilities_soci[0][0] #Partir de que se trata de matematicas
    genre = 1
    for j in range(6) :
        if winner < probabilities_lit[j][i] :
            winner = probabilities_lit[j][i]
            genre = j + 1
    books_prob_lit.append(genre)

print(books_prob_lit)
    


