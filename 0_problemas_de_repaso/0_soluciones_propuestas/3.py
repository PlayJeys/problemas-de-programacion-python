
"""

3. Considerese un archivo de texto, cuyas líneas contendrán cada una de ellas 2 números
enteros positivos o nulos y un número real, como por ejemplo:

    2 0 1.12
    3 3 -4.67
    4 2 -0.99
    3 1 6.03
    0 1 -4.71

Los dos primeros números representan los índices de fila y columna (a partir de 0) de una
matriz y el número real es el valor correspondiente a dicha posición. Se supone que las
posiciones no listadas en el archivo contienen todas ellas el valor 0, y que el listado no
contiene posiciones repetidas.

Escribir en lenguaje Python una función que tome como entrada el nombre de un archivo
como el que se ha descrito arriba, y retorne la matriz correspondiente. En el caso
mostrado arriba, la función debería retornar:
[ [0, -4.71, 0, 0], [0, 0, 0, 0], [1.12, 0, 0, 0], [0, 6.03, 0, -4.67], [0, 0, -0.99, 0] ]


"""

def matriz_archivo(archivo):

    fichero = open(str(archivo) + ".txt", "rt" , encoding = "utf-8")

    #Recorrer el archivo para buscar los índices mayores
    columna_max = -1
    fila_max = -1

    for linea in fichero:
        if len(linea) != 1:
            fila, columna, valor = map(float, linea.split())

            if int(fila) > fila_max:
                fila_max = int(fila)

            if int(columna) > columna_max:
                columna_max = int(columna)

    #Crear la matriz de tamaño adecuado
    M = []
    a = [0] * (columna_max+1)

    for i in range(fila_max + 1):
        M.append(a[:])

    fichero.close()
    
    #Recorrer de nuevo el fichero y registrar los valores
    fichero = open(str(archivo) + ".txt", "rt", encoding = "utf-8")

    for linea in fichero:
        fila, columna, valor = map(float, linea.split())
        M[int(fila)][int(columna)] = valor
    
    fichero.close()

    return M



print(matriz_archivo("fichero_3"))







