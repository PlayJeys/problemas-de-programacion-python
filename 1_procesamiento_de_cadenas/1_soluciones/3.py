
"""
Escribir una función format_num(x, size, d) que construya y retorne una cadena
s representando el número real x en una cadena de longitud size con d decimales,
dejando espacios en blanco en las posiciones sobrantes por la izquierda
"""

#Precodinciones: size >= 0, d>=0
def format_num(x, size, d):

    s = str(round(x,d))
    longitud = len(s)

    if longitud < size:
        s = ((" ")*(size-longitud)) + s

    return s


def format_num_fstring(x, size, d):
    return f"{x:{size}.{d}e}", f"{x:{size}.{d}f}"

print(format_num(0.1234440,20,5))

print(format_num_fstring(0.00043234,20,5))
