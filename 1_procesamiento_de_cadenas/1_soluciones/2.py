"""
Escribir una función trans(s, chin, chout) que cree y retorne una nueva cadena
t a partir de la cadena s tal que cada carácter de la cadena chin sea reemplazado
por el carácter correspondiente de la cadena chout. Así, por ejemplo, la llamada
trans(‘Hola mundo’, ‘Ho’, ‘je’) retornaría la cadena ‘jela munde’.
"""

def trans(s, chin, chout):
    t = []

    for caracter in s:
        if caracter in chin:
            i = chin.index(caracter)
            t.append(chout[i])
        else:
            t.append(caracter)

    t = "".join(t)

    return t


print(trans("Hola mundo", "Ho", "je"))