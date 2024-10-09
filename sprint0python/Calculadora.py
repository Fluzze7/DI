from operaciones import *
while  True: #función que solicita por teclado la variable n1 y solo termina cuando este es un numero
    n1 = input("N1:   ")
    if checknum(n1):
        n1 = tonum(n1)
        break
while  True: #misma función que la anterior pero para la variable n2
    n2 = input("N2:   ")
    if checknum(n2):
        n2 = tonum(n2)
        break
print("Ambos numeros son: n1: ",n1,"y n2: ",n2) #muestra por consola los valores introducidos
# por el usuario en las variables n1 y n2.
print("Que operación deseas hacer? (+-*/)")
operacion = input() #lee un valor por teclado esperando recibir +-*/, en caso de no hacerlo no haría nada
#sino, en funcion del simbolo hace dicha operación.
if operacion == "+":
    print("Resultado de la suma = ",add(n1,n2))
elif operacion == "-":
    print("Resultado de la resta = " , substract(n1,n2))
elif operacion == "-":
    print("Resultado de la multiplicación = " , product(n1,n2))
elif operacion == "/":
        print("Resultado de la división = ", division(n1,n2) )
else:
    print("No has introducido una opción valida.")