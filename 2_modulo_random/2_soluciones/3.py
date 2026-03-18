
""""
Utilizando el módulo random, escribir una función que retorne una lista con
k permutaciones distintas (aleatorias) de los n primeros números naturales.
La función tendrá como argumentos los valores de k y n (k <= n!).
"""

import random
import string

def rnd_naturals(k,n):
    numeros = [i for i in range(n)]
    for _ in range(k):
        numeros = random.sample(numeros, n)

    return numeros

print(rnd_naturals(5,10))
    




