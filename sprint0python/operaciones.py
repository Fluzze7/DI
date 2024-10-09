def add(number1,number2):
    """
    :param number1: float
        primer número a sumar.
    :param number2: float
        segundo número a sumar.
    :return: float
        suma de number1 y number2.
    """
    return number1+number2
def substract(number1,number2):
    """
    :param number1: float
        primer número a restar
    :param number2: float
        segundo número a restar
    :return: float
        resta de number1 y number2.
    """
    return number1-number2
def product(number1,number2):
    """
    :param number1: float
        primer número a multiplicar
    :param number2: float
        segundo número a multiplicar
    :return: float
        multiplicación de number1 y number2.
    """
    return number1*number2
def division(number1,number2):
    """
    :param number1: float
        dividendo de la operación
    :param number2: float
        divisor de la operación
    :return: float
        division entre ambos numeros, numero1 y numero2 siempre que numero2 != 0
    """
    if number2 != 0:
        return number1/number2
    else:
        print("No puedes dividir por 0")
def checknum(value):
    """
    :param value: str
    :return: boolean
        comprueba si el valor es un número y devuelve true, o no y devuelve false.
    """
    return value.replace(".","").isdigit()
def tonum(value):
    """
    :param value: str
    :return: float
        cambia el tipo de variable de un String a Float. Debe ejecutarse previamente la funcion
        checknum(value) y esta devolver True, sino esta función romperá el programa.
    """
    return float(value)

