from operaciones import *

while  True:
    n1 = input("N1:   ")
    if compnum(n1):
        n1 = pasaranum(n1)
        break
while  True:
    n2 = input("N2:   ")
    if compnum(n2):
        n2 = pasaranum(n2)
        break
print("Ambos numeros son: n1: ",n1,"y n2: ",n2)

print("Que operación deseas hacer? (+-*/)")
operacion = input()
if operacion == "+":
    print("Resultado de la suma = ",suma(n1,n2))
elif operacion == "-":
    print("Resultado de la resta = " , resta(n1,n2))
elif operacion == "-":
    print("Resultado de la multiplicación = " , multiplicacion(n1,n2))
elif operacion == "/":
    if n2 == 0:
        print("NO SE PUEDE DIVIDIR ENTRE 0")
    else:
        print("Resultado de la división = ", dividision(n1,n2) )
else:
    print("No has introducido una opción valida.")