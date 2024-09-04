
# crear un menu en el que el usuario elija entre las operaciones
# tambien tiene un boton de salir
#Crear una calculadora....
# primer archivo(operciones.py) 
# 4 operaciones basicas: +,-,/,x.

#valor_uno = int(input("Por favor ingrese un numero: "))
#valor_dos = int(input("Por favor ingrese un numero: "))

def sumar (valor_uno, valor_dos):
    resultado = valor_uno + valor_dos
    return resultado

    resultado = suma(valor_uno, valor_dos)

    print(f"El valor total de la suma es {resultado}.")
    print("-----------------")

def resta():

    valor_uno = int(input("Por favor ingrese un numero: "))
    valor_dos = int(input("Por favor ingrese un numero: "))

def resta (valor_uno, valor_dos):
    resultado = valor_uno - valor_dos
    return resultado

    resultado = resta(valor_uno, valor_dos)
    print(f"El valor total de la resta es {resultado}.")
    print("-----------------")


def multiplicacion():
    valor_uno = int(input("Por favor ingrese un numero: "))
    valor_dos = int(input("Por favor ingrese un numero: "))

def multipliacion (valor_uno, valor_dos):
    resultado = valor_uno * valor_dos
    return resultado

    resultado = multiplicacion(valor_uno, valor_dos)
    print(f"El valor total de la multiplicacion es {resultado}.")
    print("-----------------")


def division():   

    valor_uno = int(input("Por favor ingrese un numero: "))
    valor_dos = int(input("Por favor ingrese un numero: "))

def division (valor_uno, valor_dos):
    resultado = valor_uno // valor_dos
    return resultado

    resultado = division(valor_uno, valor_dos)
    print(f"El valor total de la division es {resultado}.")
    print("-----------------")

