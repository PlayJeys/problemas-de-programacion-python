"""
 Escribir una función stats(filename) que retorne una tupla con las proporciones (tantos por ciento sobre el total de caracteres) 
 de vocales, consonantes, dígitos, signos de puntuación y blancos en el archivo filename.

Solucionar:
    - Tratamiento del conjunto onsontantes
"""

import string

def stats(archivo):

    l = ["vocales", "consonantes", "dígitos", "signos de puntuación" ,"blancos"]

    stats = [
        ["vocales", "aeiou"],
        ["consonantes", string.ascii_letters],
        ["dígitos", string.digits],
        ["signos de puntuacion", string.punctuation],
        ["blancos", string.whitespace]
        ]

    d_total = dict()
    n = 0

    with open(archivo, "rt", encoding="utf-8") as fp:
        for line in fp:
            for char in line:
                for k in stats:
                    if char in k[1]:
                        d_total[k[0]] = d_total.get(k[0],0) + 1
                        n += 1
                        break

    p = list()
    for k in d_total:
        porcentaje = round((d_total[k]/n)*100,2)
        p.append((k,porcentaje))

    return p



#print(stats("golondrinas.txt"))





