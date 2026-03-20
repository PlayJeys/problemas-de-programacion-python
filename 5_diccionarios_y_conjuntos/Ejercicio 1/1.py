"""
Escribir en Python una función que tome como entrada un fichero de texto y retorne el histograma de palabras de dicho fichero, 
en forma de diccionario. Escríbase asimismo una función que, tomando como entrada ese histograma y un entero n, devuelva la 
lista de palabras que aparecen exactamente n veces en el fichero. Por último, escríbase un programa que pida al usuario el 
nombre de un fichero y un valor n, y a continuación imprima en líneas sucesivas las palabras que aparecen n veces en dicho fichero.
"""


def histograma_fichero(fichero):
    with open(fichero, "rt", encoding = "utf-8") as fp:
        d = dict()

        for linea in fp:
            linea = linea.split()
            for palabra in linea:
                d[palabra] = d.get(palabra, 0) + 1

    return d


def apariciones(histograma, n):
    l = list()
    for clave, valor in histograma.items():
        if valor == n:
            l.append(clave)
    
    return l


def imprimir_apariciones_especificas(fichero, n):
    d = histograma_fichero(fichero)

    for palabra in apariciones(d,n):
        print(palabra)



"""
d = histograma_fichero("prueba.txt")
print(d)
print(apariciones(d, 5))

imprimir_apariciones_especificas("prueba.txt", 5)
"""""




