from operaciones import *

while  True:
    a = input("N1:   ")
    if compnum(a):
        a = pasaranum(a)
        break
while  True:
    b = input("N2:   ")
    if compnum(b):
        b = pasaranum(b)
        break
print("Ambos numeros son: n1: ",a,"y n2: ",b)

print("Que operación deseas hacer? (+-*/)")
operacion = input()
if operacion == "+":
    print("Resultado de la suma = ",suma(a,b))
elif operacion == "-":
    print("Resultado de la resta = " , resta(a,b))
elif operacion == "-":
    print("Resultado de la multiplicación = " , multiplicacion(a,b))
elif operacion == "/":
    if b == 0:
        print("NO SE PUEDE DIVIDIR ENTRE 0")
    else:
        print("Resultado de la división = ", dividision(a,b) )
else:
    print("No has introducido una opción valida.")