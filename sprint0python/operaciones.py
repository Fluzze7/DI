def sumar_numeros(i,w):
    return i+w
def restar_numeros(i,w):
    return i-w
def multiplicar_numeros(i,w):
    return i*w
def dividir_numeros(i,w):
    return i/w
def comprobar_numero(x):
    return x.isdigit()
def devolverNumero(t):
    return int(t)
while True:
    a = input("N1: ")
    if comprobar_numero(a):
        break
    print("DEBE SER UN NUMERO")
while True:
    b = input("N2: ")
    if comprobar_numero(b):
        break
    print("DEBE SER UN NUMERO")
a = devolverNumero(a)
b = devolverNumero(b)
print("OPERACION?: (+-/:)")
operacion = input()
if operacion == "+":
    print("Resultado de la suma = ",sumar_numeros(a,b))
elif operacion == "-":
    print("Resultado de la resta = " , restar_numeros(a,b))
elif operacion == "-":
    print("Resultado de la multiplicación = " , multiplicar_numeros(a,b))
elif operacion == "/":
    if b == 0:
        print("NO SE PUEDE DIVIDIR ENTRE 0")
    else:
        print("Resultado de la división = ", dividir_numeros(a,b) )
else:
    print("No has introducido una opción valida.")
