"""
Escribir en Python una función que tome como entrada un entero n>0 y retorne un diccionario f con la descomposición de n en factores primos, 
tal que las claves del diccionario sean los factores y el valor asociado a cada clave sea el exponente de dicho factor. 
Así, si n=360, la función deberá retornar el diccionario: f = {2: 3, 3: 2, 5: 1}.
"""

def fact_descomp(n):
    f = dict()
    factor = 2
    
    while n != 1:
        if n % factor == 0:
            f[factor] = f.get(factor, 0) + 1
            n = n/factor
        else:
            factor += 1

    return f


#print(fact_descomp(360))

