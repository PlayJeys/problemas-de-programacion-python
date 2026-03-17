
"""
Suponiendo que s es una cadena formada sólo por letras minúsculas, escribir
dos funciones lrot(s, n) y rrot(s, n) que devuelvan la cadena resultante de
rotar las letras de s n posiciones a izquierda o n posiciones a derecha en el
alfabeto, respectivamente. Por ejemplo, rotando la letra 'b' 3 posiciones a izquierda
se obtiene la letra 'y'. Y viceversa: rotando la letra 'y' 3 posiciones a derecha se
obtiene la letra 'b'.
"""


def lrot(s,n):
    t = ""
    for caracter in s:
        t += chr((ord(caracter) - ord('a') - n) % 26 + ord('a')) 

    return t


def rrot(s,n):
    t = ""

    for caracter in s:
        t += chr((ord(caracter) - ord('a') + n) % 26 + ord('a')) 

    return t




"""
se está utilizando la operación % 26 para asegurarse de que el resultado de la rotación 
se mantenga dentro del rango de letras minúsculas del alfabeto. El valor 26 se refiere 
al número de letras en el alfabeto inglés.
"""


print(lrot("mesa ",3))
print(rrot("jbpx",3))


