"""
Escribir un programa que: (a) pida al usuario una cadena con caracteres obligatorios
y el nombre de dos ficheros de texto; y (b) escriba en el segundo fichero las palabras
del primer fichero que contienen todos los caracteres obligatorios, a razón de una
palabra por línea y, junto a cada palabra, el número de veces que dicha palabra
aparece en el fichero.
"""

def palabras_co(caracteres_obligatorios, f1, f2):
    with open(f1, "rt", encoding = "utf-8") as fp1:
        with open(f2, "wt", encoding = "utf-8") as fp2:
            palabras_permitidas = {}

            for linea in fp1:
                linea = linea.split()
                for palabra in linea:

                    #Comprobar si la palabra tiene todos los caracteres permitidos
                    caracter_prohibido = False
                    for char in palabra:
                        if char not in caracteres_obligatorios:
                            caracter_prohibido = True
                            break

                    #Aumentar contador de palabras si la palabra está permitida
                    if not caracter_prohibido:
                        if palabra in palabras_permitidas:
                            palabras_permitidas[palabra] += 1
                        else:
                            palabras_permitidas[palabra] = 1

            
            for palabra in palabras_permitidas:
                fp2.write(f"Palabra: {palabra} -> Apariciones: {palabras_permitidas[palabra]} \n")


l = "coam"
palabras_co(l, "ejemplo.txt", "ejemplo_permitido.txt")