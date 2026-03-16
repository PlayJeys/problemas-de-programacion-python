
"""
5. Escribir en lenguaje Python una función que tome como entrada una lista y retorne otra
lista con tuplas de la forma (elemento, num_rep), indicando los distintos valores que
aparecen en la lista original y el número de repeticiones de cada uno. Si tomamos, por
ejemplo, la lista l=[1,0,3,4,1,2,3,9,1], la función podría devolver [(1,3), (0,1), (3,2), (4,1),
(2,1), (9,1)].

"""


def element_rep(lista):
    d = {}
    a = []

    for i in lista:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    for val,rep in d.items():
        a.append(tuple([val,rep]))

    return a


#l=[1,0,3,4,1,2,3,9,1]
#print(element_rep(l))








