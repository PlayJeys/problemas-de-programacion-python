
"""
Utilizando el módulo random, escribir una función que retorne una palabra
de n letras minúsculas generadas aleatoriamente. Al generar cada letra,
la probabilidad de generar una vocal deberá ser la misma que la de generar
una consonante.
"""

import random
import string

def palabra_aleatoria(n):
    resultado = ""
    s = string.ascii_lowercase
    vocales = "aeiou"
    consonantes = "".join(letra for letra in s if letra not in vocales)

    for i in range(n):
        l = random.choice([vocales, consonantes])
        resultado += random.choice(l)

    return resultado

for i in range(5):
    print(palabra_aleatoria(random.randint(1,50)))