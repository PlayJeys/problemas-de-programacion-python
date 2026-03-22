"""
Escribir en Python una función que tome como entrada un fichero de texto y retorne un diccionario d_pos tal que d_pos[w] contenga
la lista de posiciones (i, j) en las que aparece cada palabra w dentro del fichero, siendo i: índice de línea y j: índice de la palabra 
dentro de la línea (ambas empezando desde 1). Recuérdese que el final de línea viene marcado por el carácter '\n'.
"""
import shelve

def dict_pos(fichero):
    with shelve.open("pos_" + str(fichero[:-4])) as d:
        d.clear()
        with open(fichero, "rt", encoding = "utf-8") as fp:
            i = 0
            for linea in fp:
                j = 0
                for palabra in linea.rstrip().split():
                    print(palabra)
                    if palabra in d:
                        d[palabra].append((i,j))
                    else:
                        d[palabra] = [(i,j)]
                    j += 1

                i += 1

"""
dict_pos("archivo.txt")

with shelve.open("pos_archivo") as d:
    for palabra in d:
        print(f"{palabra}: {d[palabra]}")
"""