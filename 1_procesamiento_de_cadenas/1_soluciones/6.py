"""
Escribir una función my_split(s [, sep_seq [, max_splits]]) 
que tome como entrada una cadena s y, 
utilizando como separadores los elementos de la secuencia sep_seq, 
retorne la lista de cadenas resultante, haciendo como
máximo max_splits separaciones. 
Los argumentos sep_seq y max_splits son opcionales. 
El argumento sep_seq podría ser una cadena de caracteres, tal que
cada carácter de la cadena funcione como separador, o una lista de cadenas,
tal que cada cadena funcione como separador. El valor por defecto de sep_seq
será ' \n\t' y el de max_splits será None (en cuyo caso se realizarán todas las
separaciones posibles). En cualquier caso, si en la cadena s se encuentra una
secuencia contigua de separadores, ésta se tratará como un único separador.
"""

def my_split(s, sep_seq = "\n\t" , max_split = None):
    
    if type(sep_seq) == list:
        separadores = sep_seq[:]
    elif type(sep_seq) == str:
        separadores = sep_seq[:]

    resultado = []
    palabra_actual = ""
    n_sep = 0

    #Recorro la cadena s o en la lista c
    for i, caracter in enumerate(s):
        if caracter in separadores:

            if palabra_actual:
                resultado.append(palabra_actual)
                palabra_actual = ""

            n_sep += 1

            if max_split is not None and max_split == n_sep:
                resultado.append(palabra_actual + s[(i+1):])
                palabra_actual = ""
                break
            
        else:
            palabra_actual += caracter
            
    if palabra_actual:
        resultado.append(palabra_actual)

    return resultado



s = "holta, que tal estas t separación t"


#print(my_split(s,"t",3))