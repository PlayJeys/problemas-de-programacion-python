
"""
Repetir el ejercicio anterior usando el módulo shelve para, en lugar de retornar la descomposición de n en factores primos, 
guardarla de manera persistente en un fichero. Además, escribir en Python una función que reciba como entrada dos ficheros 
shelve con la factorización de sendos enteros n y m, y devuelva el máximo común divisor de n y m.
"""

import shelve

def fact_descomp_file(n, nombre_shelve):
    with shelve.open(nombre_shelve) as d:
        factor = 2
        while n != 1:
            if n % factor == 0:
                d[str(factor)] = d.get(str(factor), 0) + 1
                n = n/factor
            
            else:
                factor += 1

            
def maximo_c_div(archivo1, archivo2):
    max_fact = 1
    with shelve.open(archivo1) as d:
        with shelve.open(archivo2) as f:
            for k1 in d.keys():
                if k1 in f:
                    max_fact = max(max_fact,int(k1))

    return max_fact

            
"""
fact_descomp_file(360, "shv360")
fact_descomp_file(100, "shv100")

print(maximo_c_div("shv360", "shv100"))
"""



