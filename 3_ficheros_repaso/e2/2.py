

"""
Escribir un programa que: (a) pida al usuario una cadena con caracteres permitidos
y el nombre de dos ficheros de texto; y (b) escriba en el segundo fichero, para cada
línea del primer fichero, el número de línea seguido del porcentaje de palabras de esa
línea que contengan sólo caracteres permitidos.
"""

def allowed_char(caracteres_permitidos, f1, f2):
    with open(f1, "rt", encoding = "utf-8") as fp1:
        with open(f2, "wt", encoding ="utf-8") as fp2:
            for i,linea in enumerate(fp1):
                count = 0
                linea = linea.split()
                for palabra in linea:
                    if all(char in caracteres_permitidos for char in palabra):
                        count += 1

                porcentaje = (count/len(linea))*100
                
                fp2.write(f"Linea: {i}, con {round(porcentaje,2)} por ciento de aparición \n")

    return True


caracteres_permitidos = input("Ingrese los caracteres permitidos: ")
archivo_entrada = input("Ingrese el nombre del archivo de entrada: ")
archivo_salida = input("Ingrese el nombre del archivo de salida: ")

allowed_char(caracteres_permitidos, archivo_entrada, archivo_salida)