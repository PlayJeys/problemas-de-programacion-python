
""""
Escribir una función rem_punct(s) que tome como entrada una cadena s y retorne
otra cadena que será copia de s salvo que no contendrá signos de puntuación.
"""

import string

a = "¡hola!, ¿que tal estas?, ?como te encuentras hoy?."

#Versión 1
#Menos eficiente

sigos_puntuación = [".",",","!","¡","?","¿"]

def rem_punct_ver1(s):
    cadena = ""
    for caracter in s:
        if caracter not in sigos_puntuación:
            cadena += caracter
    return cadena



print(rem_punct_ver1(a))


#Versión 2: 
#De mayor eficencia debido al uso de cadenas y signos de puntuación mediante el módulo string
#Sin embargo no toma en cuenta algunso signos como "¿","¡"...

def rem_punct_ver2(s):
    cadena = []
    for caracter in s:
        if caracter not in string.punctuation:
            cadena.append(caracter)

        
    cadena = "".join(cadena)

    return cadena


print(rem_punct_ver2(a))

    

