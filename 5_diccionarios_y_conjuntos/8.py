"""
Escribir una función random_word(n) que genere una palabra aleatoria de n caracteres. 
Escribir una función num_words(n, charset, n_tries=10) que calcule y retorne el número 
promedio de palabras aleatorias de longitud n que es necesario generar hasta haber generado 
(al menos una vez en alguna palabra) todos los caracteres del conjunto charset. 
El promedio se calculará sobre un total de n_tries pruebas.
"""

import random as r
import string

def random_word(n):
    l_aux = []
    for _ in range(n):
        l_aux.append(r.choice(string.ascii_letters))

    return "".join(l_aux)


def num_words(n, charset, n_tries = 10):
    suma = 0
    for _ in range(n_tries):
        tries = 0
        while True:
            every_char_in_charset = True
            for char in random_word(n):
                if char not in charset:
                    every_char_in_charset = False
                    break
                
            tries += 1

            if every_char_in_charset:
                break

        suma += tries

    return round(suma/n_tries,2)

        
#print(num_words(5, "abcdefghijk"))


