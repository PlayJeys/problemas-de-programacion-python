"""
Escribir una función find_all(t, s, overlaps=True) que retorne una lista con
todas las posiciones donde aparece la subcadena t dentro de la cadena s. Si
overlaps = True (valor por defecto), se permiten solapamientos entre
diferentes ocurrencias de la subcadena. Si overlaps = False, no se permiten
solapamientos entre diferentes ocurrencias de la subcadena. Escribir un
programa que ponga a prueba la función definida, usando la cadena
s="sabbbbabbababababb" y las subcadenas t="abb", t="bbb" y t="aba".
"""

def find_all(t, s, overlaps = True):
    
    index = []
    
    
    if overlaps == True:
        longitud_t = len(t)
        longitud_s = len(s)
        n = True

        for indice in range(longitud_s - longitud_t + 1):
            for i in range(longitud_t):
                if s[int(indice + i)] != t[i]:
                    n = False

            if n:
                index.append(indice)

            n = True   

    elif overlaps == False:
        a = 0
        
        for i in range(s.count(t)):
            x = s.index(t,a)
            index.append(x)
            a = x + 1


    #elif overlaps == False:

    return index


#Podemos sin embargo, aun que ya lo he hecho en la propia función, definir una función auxiliar que haga un window slide.

def find(t,s):
    for i in range(len(s)-len(t)+1):
        if s[i:i+len(t)] == t:
            










s = "abbababbbb"

t = "abb"
print(find_all(t,s))

t = "bbb"
print(find_all(t,s))

t = "bbb"
print(find_all(t,s, False))

t = "aba"
print(find_all(t,s))







