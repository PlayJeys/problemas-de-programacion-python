
"""

4. Escribir en lenguaje Python una función que tome como entrada una lista l y la
modifique de manera que queden en ella sólo los elementos que estaban repetidos, cada
uno de ellos apareciendo una sola vez. Considerese, por ejemplo, la lista
l=[1,0,3,4,1,2,3,9,1]; tras llamar a la función, quedará: l=[1,3].


"""

def l_repeticiones(l):
    elementos = set()
    repetidos = set()

    for i in l:
        if i not in elementos:
            elementos.add(i)
        else:
            repetidos.add(i)


    return list(repetidos)


l=[1,0,3,4,1,2,3,9,1]
print(l_repeticiones(l))



def rep_items_v5(l):
    l_copia = l[:]
    for x in l_copia:
        if l_copia.count(x) == 1:
            l.remove(x)
        else:
            n = l.count(x)
            for _ in range(n-1):
                l.remove(x)



#Para probar el código creamos un tester

import time
import random

"""
for rango in [10, 100, 1000, 1000]:
    t_v1 = 0
    t_v2 = 0
    t_v3 = 0
    t_v4 = 0
    t_v5 = 0

    for i in range(100):
        lista_1 = []
        for j in range(1000):
            lista_1.append(random, randit(i,rango))
        for i in range(4):
            eval("t_v"+str(i+2)) = lsita_1[:]
        
        for i in range(5)
            eval("t" + str(i+1)) = time.perf_counter()
            rep_items_v1(eval()

"""
            



