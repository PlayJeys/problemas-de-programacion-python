"""
Escribir un primer programa que genere una lista de 1000 cadenas de caracteres
aleatorias (formadas sólo por letras minúsculas, de longitud entre 5 y 10), y la guarde
en un fichero mediante el módulo pickle. Escribir un segundo programa que cargue
dos de esos ficheros en sendas listas (también mediante el módulo pickle) y retorne el
número de veces que una palabra de la primera lista es más larga que la palabra
correspondiente de la segunda lista. ¿Se puede estimar este número?
"""

import random
import pickle
import string

def generar_cadenas():
    cadenas = []
    for _ in range(1000):
        longitud = random.randint(5, 10)
        cadena = ''.join(random.choice(string.ascii_lowercase) for _ in range(longitud))
        cadenas.append(cadena)
    return cadenas

def guardar_lista_en_pickle(lista, nombre_archivo):
    with open(nombre_archivo, 'wb') as archivo:
        pickle.dump(lista, archivo)

def cargar_lista_desde_pickle(nombre_archivo):
    with open(nombre_archivo, 'rb') as archivo:
        lista = pickle.load(archivo)
    return lista

def comparar_longitudes(lista1, lista2):
    contador = 0
    for palabra1, palabra2 in zip(lista1, lista2):
        if len(palabra1) > len(palabra2):
            contador += 1
    return contador

# Generar y guardar las listas en archivos pickle
lista1 = generar_cadenas()
lista2 = generar_cadenas()
guardar_lista_en_pickle(lista1, 'lista1.pkl')
guardar_lista_en_pickle(lista2, 'lista2.pkl')

# Cargar las listas desde los archivos pickle
lista1 = cargar_lista_desde_pickle('lista1.pkl')
lista2 = cargar_lista_desde_pickle('lista2.pkl')

# Comparar las longitudes de las palabras en las dos listas
numero_de_veces = comparar_longitudes(lista1, lista2)
print("El número de veces que una palabra de la primera lista es más larga que la palabra correspondiente de la segunda lista es:", numero_de_veces)


