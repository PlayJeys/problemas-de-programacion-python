
"""
1. Escribir en lenguaje Python una función que tome como entrada una función f(x) y un
intervalo [a,b] y retorne una tupla (fmax, xmax) con el valor máximo fmax que alcanza la
función en dicho intervalo y el punto xmax ∈ [a,b] donde se alcanza dicho máximo

"""


#He propuesto dos formas de resolver el problema, 1. con paso fijo y 2. con paso variable

def f(x):
	return -(x**2) + (x**3) + 5


def max_val_pasofijo(a,b,v):
	paso_fijo = abs(b-a)/v
	if a > b:
		a,b = b,a

	M = [f(a),a]
	x = a

	for i in range(v):
		y = round(f(x),5)
		if y > M[0]:
			M = [y,x]
			
		x += paso_fijo
		
	return tuple(M)


"""
print("Indica el intervalo [a,b] para el que se evaluará la función: ")
s1 = float(input("a: "))
s2 = float(input("b: "))
error = int(input("Indica el error asociado (cuanto mayor sea el valor, menor el error): "))


print(max_val(s1,s2,error))


"""


def max_val_pasovariable(a,b,iteraciones,funcion):
	res = 100
	n = 0

	for i in range(iteraciones):
		paso = (b-a)/res
		M = [f(a),a]
		x = a

		for i in range(res):
			n = n + 1
			y = round(funcion(x),10)
			if y < M[0]:
				M = [y,x]
			x += paso

		a = M[1] - paso*10
		b = M[1] + paso*10
		res = res*10

	return tuple(M),n



		

print("Indica el intervalo [a,b] para el que se evaluará la función: ")
s1 = float(input("a: "))
s2 = float(input("b; "))
iteraciones = int(input("Indica la cantidad de iteraciones de aumento de resolución(cuanto mayor sea el valor, menor el error): "))


print(max_val_pasovariable(s1,s2,iteraciones,f))












