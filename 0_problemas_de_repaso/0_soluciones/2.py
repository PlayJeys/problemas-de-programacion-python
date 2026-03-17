

"""
2. Escribir en lenguaje Python una función que tome como entrada una cadena de
caracteres representando un número entero en alguno de los siguientes formatos:

    • binario: "b101101" "-b101101"
    • octal: "o55" "-o55"
    • decimal: "d45" "-d45"
    • hexadecimal: "x2d" "-x2d"

y retorne el entero correspondiente.

"""


def convertir_a_entero(cadena):
    if cadena[0] == '-':
        signo = -1
        cadena = cadena[2:]  # Eliminar el signo y el prefijo
    else:
        signo = 1
        cadena = cadena[1:]  # Solo eliminar el prefijo

    base = 10  # Por defecto, decimal

    if cadena[0] == 'b':
        base = 2
        cadena = cadena[1:]
    elif cadena[0] == 'o':
        base = 8
        cadena = cadena[1:]
    elif cadena[0] == 'x':
        base = 16
        cadena = cadena[1:]

    return signo * int(cadena, base)

# Ejemplos de uso:
print(convertir_a_entero("b101101"))  # Salida: 45
print(convertir_a_entero("-b101101")) # Salida: -45
print(convertir_a_entero("o55"))      # Salida: 45
print(convertir_a_entero("-o55"))     # Salida: -45
print(convertir_a_entero("d45"))      # Salida: 45
print(convertir_a_entero("-d45"))     # Salida: -45
print(convertir_a_entero("x2d"))      # Salida: 45
print(convertir_a_entero("-x2d"))     # Salida: -45












