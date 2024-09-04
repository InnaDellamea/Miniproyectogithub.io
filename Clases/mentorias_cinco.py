# crear un menu en el que el usuario elija entre las operaciones
# tambien tiene un boton de salir

from calculadora import *

print("Hola, bienvenidos a la calculadora PRO")
print("--------------------")
print("1.Sumar")
print("2.Restar")
print("3.Multiplicar")
print("4.Dividir")
print("5.Salir")

eleccion_usuario = input("Por favor ingrese una opcion: ")

if eleccion_usuario == "1":
    valor_uno = int(input("Ingrese un valor: "))
    valor_dos = int(input("Ingrese un valor: "))
    print("--------------------")
    print(f"El resultado de la suma es: {sumar(valor_uno, valor_dos)}")
    print("--------------------")
    print("Gracias por utilizar el programa")
if eleccion_usuario == "2":
    valor_uno = int(input("Ingrese un valor: "))
    valor_dos = int(input("Ingrese un valor: "))
    print("--------------------")
    print(f"El resultado de la resta es: {resta(valor_uno, valor_dos)}")
    print("--------------------")
    print("Gracias por utilizar el programa")
if eleccion_usuario == "3":
    valor_uno = int(input("Ingrese un valor: "))
    valor_dos = int(input("Ingrese un valor: "))
    print("--------------------")
    print(f"El resultado de la multiplicacion es:{multipliacion(valor_uno, valor_dos)}")
    print("--------------------")
    print("Gracias por utilizar el programa")
if eleccion_usuario == "4":
    valor_uno = int(input("Ingrese un valor: "))
    valor_dos = int(input("Ingrese un valor: "))
    print("--------------------")
    print(f"El resultado de la division es:{division(valor_uno, valor_dos)}")
    print("--------------------")
    print("Gracias por utilizar el programa")
if eleccion_usuario == "5":
    print("--------------------")
    print("Gracias por utilizar el programa")

