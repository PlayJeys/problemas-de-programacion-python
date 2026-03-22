"""
Se dice que una matriz es dispersa cuando la mayor parte de sus valores son nulos.
En Python, una matriz dispersa A puede representarse de manera eficiente mediante un diccionario 
que contenga únicamente los valores no nulos de la matriz, tal que una tupla de índices (i, j) sirva 
de clave para acceder al valor almacenado en dicha posición. Así, por ejemplo, la matriz:

   A = [ [0, 0, 3.7, 0], [-1.4, 0, 0, 5.21], [0, 0, 0, 1.5], [0, 1.92, 0, 0] ]
   
se representaría como sigue:

    A_dict = { (0, 2): 3.7, (1, 0): -1.4, (1, 3): 5.21, (2, 3): 1.5, (3, 1): 1.92 }.

Escribir en Python dos funciones, suma(a,b) y producto(a,b), que tomen como entrada dos matrices 
dispersas a y b (representadas del modo descrito más arriba) y retornen una nueva matriz dispersa 
con la suma y el producto de ambas, respectivamente.
"""

def suma(a,b):
    d = dict()
    for k, v in a.items():
        d[k] = v + b.get(k,0)
    return d

def producto(a, b):
    result = dict()
    for (i, j), value_a in a.items():
        for (k, l), value_b in b.items():
            if j == k:
                result[(i, l)] = result.get((i, l), 0) + value_a * value_b
    return result



"""
A_dict = {(0, 2): 3.7, (1, 0): -1.4, (1, 3): 5.21, (2, 3): 1.5, (3, 1): 1.92}
B_dict = {(0, 0): 2.0, (1, 3): 3.0, (2, 3): 4.0, (3, 1): 2.0}
print("Matriz A:", A_dict)
print("Matriz B:", B_dict)
print("Suma:", suma(A_dict, B_dict))
print("Producto:", producto(A_dict, B_dict))

"""