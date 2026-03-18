
"""
Utilizando el módulo random, escribir una función que tome como entrada
un texto (lo más fácil sería tomar ese texto de un archivo) y un entero n>0.
La función deberá retornar un texto de salida con n palabras, eligiendo cada
vez una palabra al azar del texto de entrada.
"""

import random

def ej2(file, n):
    with open(file, "rt", encoding = "utf-8") as fp:
        lista_palabras = []
        for linea in fp:
            for palabra in linea.split():
                if palabra not in lista_palabras:
                    lista_palabras.append(palabra)
        
        result = ""

        for i in range(n):
            result += random.choice(lista_palabras) + " "
        
    return result


print(ej2("ejemplo.txt",5))
