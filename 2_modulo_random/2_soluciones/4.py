
"""
Utilizando el módulo secrets, escribir una función que retorne una
contraseña de n ≥ 8 caracteres alfanuméricos con al menos una letra
minúscula, una letra mayúscula, un dígito y un carácter especial.
"""

import secrets
import string

def strong_password(k):
    n = (secrets.randbelow(k) + 8)
    caracteres = string.ascii_letters + string.digits + string.punctuation

    while True:
        minuscula, mayuscula, digito, caracter_especial = False, False, False, False
        contrasena = "".join(secrets.choice(caracteres) for i in range(n))
        for caracter in contrasena:
            if caracter.islower():
                minuscula = True
            elif caracter.isupper():
                mayuscula = True
            elif caracter.isdigit():
                digito = True
            elif caracter in string.punctuation:
                caracter_especial = True
            if minuscula and mayuscula and digito and caracter_especial:
                return contrasena

print(strong_password(10))



def generar_contrasena(k):
    longitud = (secrets.randbelow(k) + 8)
    caracteres = string.ascii_letters + string.digits + string.punctuation
    while True:
        contrasena = ''.join(secrets.choice(caracteres) for i in range(longitud))
        if (any(c.islower() for c in contrasena)
                and any(c.isupper() for c in contrasena)
                and any(c.isdigit() for c in contrasena)
                and any(c in string.punctuation for c in contrasena)):
            return contrasena

print(generar_contrasena(10))
