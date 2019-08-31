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

    # 0's y 1's por cada género
    oo_math = []
    oo_bio = []
    oo_law = []
    oo_manag = []
    oo_soci = []
    oo_lite = []

    ##### PASO 1: FRECUENCIAS #####
    # Saca la unión de las palabras de los libros Math
    words_dist = nltk.FreqDist(w for w in new_math_words)

    # Solo junta las palabras de los libros Math en un solo []
    only_math_words_dist = []
    for pair in words_dist.most_common(20):
        only_math_words_dist.append(pair[0])

    # Saca la unión de las palabras de los libros Bio
    words_dist = nltk.FreqDist(w for w in new_bio_words)

    # Solo junta las palabras de los libros Bio en un solo []
    only_bio_words_dist = []
    for pair in words_dist.most_common(20):
        only_bio_words_dist.append(pair[0])

    # Saca la unión de las palabras de los libros Law
    words_dist = nltk.FreqDist(w for w in new_law_words)

    # Solo junta las palabras de los libros Law en un solo []
    only_law_words_dist = []
    for pair in words_dist.most_common(20):
        only_law_words_dist.append(pair[0])

    # Saca la unión de las palabras de los libros Manag
    words_dist = nltk.FreqDist(w for w in new_manag_words)

    # Solo junta las palabras de los libros Manag en un solo []
    only_manag_words_dist = []
    for pair in words_dist.most_common(20):
        only_manag_words_dist.append(pair[0])

    # Saca la unión de las palabras de los libros Soci
    words_dist = nltk.FreqDist(w for w in new_soci_words)

    # Solo junta las palabras de los libros Soci en un solo []
    only_soci_words_dist = []
    for pair in words_dist.most_common(20):
        only_soci_words_dist.append(pair[0])

    # Saca la unión de las palabras de los libros Lite
    words_dist = nltk.FreqDist(w for w in new_lite_words)

    # Solo junta las palabras de los libros Lite en un solo []
    only_lite_words_dist = []
    for pair in words_dist.most_common(20):
        only_lite_words_dist.append(pair[0])

    ##### PASO 2: NORMALIZACIÓN #####
    ##### PARA MATH #####
    # 1 si está, 0 si no está una palabra, por cada libro, dentro de only_math_words_list
    for r in new_math_rows:
        book = []
        for w in range(0, 20):
            if r[w] in only_math_words_dist:
                book.append(1)
            else:
                book.append(0)

        oo_math.append(book)

    sum_math = np.asarray(oo_math)
    sum_math = sum_math.sum(axis=0)
    
    # Solo palabras
    print("\nMath:")
    print("Palabras:",sum_math)
    # Suma palabras
    print("Suma:",sum_math.sum())
    # Probabilidades
    print("Probabilidades:",sum_math/sum_math.sum())

    ##### PARA BIO #####
    # 1 si está, 0 si no está una palabra, por cada libro, dentro de only_bio_words_list
    for r in new_bio_rows:
        book = []
        for w in range(0, 20):
            if r[w] in only_bio_words_dist:
                book.append(1)
            else:
                book.append(0)

        oo_bio.append(book)

    sum_bio = np.asarray(oo_bio)
    sum_bio = sum_bio.sum(axis=0)
    
    # Solo palabras
    print("\nBio:")
    print("Palabras:",sum_bio)
    # Suma palabras
    print("Suma:",sum_bio.sum())
    # Probabilidades
    print("Probabilidades:",sum_bio/sum_bio.sum())

    ##### PARA LAW #####
    # 1 si está, 0 si no está una palabra, por cada libro, dentro de only_law_words_list
    for r in new_law_rows:
        book = []
        for w in range(0, 20):
            if r[w] in only_law_words_dist:
                book.append(1)
            else:
                book.append(0)

        oo_law.append(book)

    sum_law = np.asarray(oo_law)
    sum_law = sum_law.sum(axis=0)
    
    # Solo palabras
    print("\nLaw:")
    print("Palabras:",sum_law)
    # Suma palabras
    print("Suma:",sum_law.sum())
    # Probabilidades
    print("Probabilidades:",sum_law/sum_law.sum())

    ##### PARA MANAG #####
    # 1 si está, 0 si no está una palabra, por cada libro, dentro de only_manag_words_list
    for r in new_manag_rows:
        book = []
        for w in range(0, 20):
            if r[w] in only_manag_words_dist:
                book.append(1)
            else:
                book.append(0)

        oo_manag.append(book)

    sum_manag = np.asarray(oo_manag)
    sum_manag = sum_manag.sum(axis=0)
    
    # Solo palabras
    print("\nManag:")
    print("Palabras:",sum_manag)
    # Suma palabras
    print("Suma:",sum_manag.sum())
    # Probabilidades
    print("Probabilidades:",sum_manag/sum_manag.sum())

    ##### PARA SOCI #####
    # 1 si está, 0 si no está una palabra, por cada libro, dentro de only_soci_words_list
    for r in new_soci_rows:
        book = []
        for w in range(0, 20):
            if r[w] in only_soci_words_dist:
                book.append(1)
            else:
                book.append(0)

        oo_soci.append(book)

    sum_soci = np.asarray(oo_soci)
    sum_soci = sum_soci.sum(axis=0)
    
    # Solo palabras
    print("\nSoci:")
    print("Palabras:",sum_soci)
    # Suma palabras
    print("Suma:",sum_soci.sum())
    # Probabilidades
    print("Probabilidades:",sum_soci/sum_soci.sum())

    ##### PARA LITE #####
    # 1 si está, 0 si no está una palabra, por cada libro, dentro de only_lite_words_list
    for r in new_soci_rows:
        book = []
        for w in range(0, 20):
            if r[w] in only_lite_words_dist:
                book.append(1)
            else:
                book.append(0)

        oo_lite.append(book)

    sum_lite = np.asarray(oo_lite)
    sum_lite = sum_lite.sum(axis=0)

    # Solo palabras
    print("\nLite:")
    print("Palabras:",sum_lite)
    # Suma palabras
    print("Suma:",sum_lite.sum())
    # Probabilidades
    print("Probabilidades:",sum_lite/sum_lite.sum())

    ##### PASO 3: TEST... #####

    # Dado Math_1.txt y sus palabras...
    # Tomar las palabras de matriz new_math_rows (fila 0)
    math1_test1 = np.asarray(new_math_rows[0])
    print(math1_test1)

    ## CALCULAR PROBABILIDADES PARA MATH ##
    # Calcular 0's y 1's para math1_test1
    math1_test1_oo = []
    # Tomar only_math_words_dist para comparar con math1_test1
    for w in math1_test1:
        if w in only_math_words_dist:
            math1_test1_oo.append(1)
        else:
            math1_test1_oo.append(0)

    print(np.asarray(math1_test1_oo))

    # Calcular las probabilidades para cada clase
    # Para la clase math, utilizar sum_math/sum_math.sum()
    prob_math = sum_math/sum_math.sum()
    print(prob_math)
    class_math = []
    for i in range(0, 20):
        if math1_test1_oo[i] == 1:
            class_math.append(prob_math[i]);
        else:
            class_math.append(0)

    #class_math = np.asarray(class_math)

    p_math = 1
    for i in range(0, 20):
        if class_math[i] > 0:
            p_math = class_math[i] * p_math

    if p_math == 1:
        print("Probabilidad de que sea Math:", 0)
    else:
        print("Probabilidad de que sea Math:", 0.16 * p_math)

    ## CALCULAR PROBABILIDADES PARA BIO
    # Calcular 0's y 1's para math1_test1
    math1_test1_oo = []
    # Tomar only_math_words_dist para comparar con math1_test1
    for w in math1_test1:
        if w in only_bio_words_dist:
            math1_test1_oo.append(1)
        else:
            math1_test1_oo.append(0)

    print(np.asarray(math1_test1_oo))

    # Calcular las probabilidades para cada clase
    # Para la clase math, utilizar sum_bio/sum_bio.sum()
    prob_math = sum_bio/sum_bio.sum()
    print(prob_math)
    class_math = []
    for i in range(0, 20):
        if math1_test1_oo[i] == 1:
            class_math.append(prob_math[i]);
        else:
            class_math.append(0)

    #class_math = np.asarray(class_math)

    p_math = 1
    for i in range(0, 20):
        if class_math[i] > 0:
            p_math = class_math[i] * p_math

    if p_math == 1:
        print("Probabilidad de que sea Bio:", 0)
    else:
        print("Probabilidad de que sea Bio:", 0.16 * p_math)

    ## CALCULAR PROBABILIDADES PARA LAW
    # Calcular 0's y 1's para math1_test1
    math1_test1_oo = []
    # Tomar only_math_words_dist para comparar con math1_test1
    for w in math1_test1:
        if w in only_law_words_dist:
            math1_test1_oo.append(1)
        else:
            math1_test1_oo.append(0)

    print(np.asarray(math1_test1_oo))

    # Calcular las probabilidades para cada clase
    # Para la clase math, utilizar sum_law/sum_law.sum()
    prob_math = sum_law/sum_law.sum()
    print(prob_math)
    class_math = []
    for i in range(0, 20):
        if math1_test1_oo[i] == 1:
            class_math.append(prob_math[i])
        else:
            class_math.append(0)

    #class_math = np.asarray(class_math)

    p_math = 1
    for i in range(0, 20):
        if class_math[i] > 0:
            p_math = class_math[i] * p_math

    if p_math == 1:
        print("Probabilidad de que sea Law:", 0)
    else:
        print("Probabilidad de que sea Law:", 0.16 * p_math)