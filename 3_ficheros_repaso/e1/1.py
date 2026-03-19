"""
Escribir un programa que: (a) pida al usuario una cadena con caracteres prohibidos
y el nombre de dos ficheros de texto; y (b) escriba en el segundo fichero, para cada
línea del primer fichero, el número de línea seguido de aquellas palabras de dicha línea
que no contengan ninguno de los caracteres prohibidos.
"""

def proh_chars_1(caracteres_prohibidos, f1, f2):
    with open(f1, "rt", encoding = "utf-8") as fp1:
        with open(f2, "wt", encoding ="utf-8") as fp2:
            for i,linea in enumerate(fp1):
                s = []

                for palabra in linea.split():
                    encontrado = False
                    for char in caracteres_prohibidos:
                        if char in palabra:
                            encontrado = True
                            break
                    
                    if not encontrado:
                        s.append(palabra)

                if s:
                    s.insert(0, f"{i}")
                    s.append("\n")
                    fp2.write(" ".join(s))

                

    return True

caracteres_prohibidos = input("Ingrese los caracteres prohibidos: ")
archivo_entrada = input("Ingrese el nombre del archivo de entrada: ")
archivo_salida = input("Ingrese el nombre del archivo de salida: ")

proh_chars_1(caracteres_prohibidos, archivo_entrada, archivo_salida)


