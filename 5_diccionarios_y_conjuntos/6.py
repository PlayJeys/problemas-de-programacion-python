"""
Escribir una función oov(l_words, vocab) que retorne el conjunto de palabras de la lista l_words que no 
aparecen en la lista vocab. 

Escribir un programa que: 
    (1) cree una lista con 1000 palabras aleatorias (de longitudes comprendidas entre 4 y 6) y 4 vocabularios distintos (listas con palabras generadas aleatoriamente 
de longitud entre 4 y 6) de longitudes 100, 1000, 10000 y 100000; y 
    (2) aplique la función oov() para determinar 
el número de palabras fuera del vocabulario en cada caso, calculando el tiempo empleado en hacerlo. Comparar los 
tiempos obtenidos al utilizar o no utilizar conjuntos en la definición de la función oov().
"""

import random as r
import string
import time

def oov(l_words, covab):
    l_aux = list()
    for word in l_words:
        if word in covab:
            l_aux.append(word)
    return l_aux


def oov_conjuntos(l_words, covab):
    s = set()
    for word in l_words:
        s.add(word)

    return s

#Definir variables
l = list()
vocabularios = {f"voc_{i}": list() for i in range(4)}

#Crear lista con 1000 palabras aleatorias
for i in range(1000):
    l_aux = list()
    for j in range(r.randrange(4,6)):
        l_aux.append(r.choice(string.ascii_letters))

    l.append("".join(l_aux))

#Generar los vocabularios
for voc in vocabularios:
    for _ in range(r.choice([100, 1000])):
        char_aux = list()
        for _ in range(r.randrange(4,6)):
            char_aux.append(r.choice(string.ascii_letters))

        vocabularios[voc].append("".join(char_aux))


#Numero de palabras fuera del vocabulario
for k in vocabularios:
    t1 = time.process_time()
    n1 = len(oov(l,vocabularios[k]))
    t2 = time.process_time()
    n2 = len(oov_conjuntos(l, vocabularios[k]))
    t3 = time.process_time()

    print(f"Tiempo para el vocabulario {k}: ")
    print(f"   - Primer método: {t2-t1:10.7f} segundos")
    print(f"   - Segundo método: {t3-t2:10.7f} segundos", end = "\n\n")



    

