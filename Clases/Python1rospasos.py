#print('Hola mundo')  
#print es una funcion que imprime lo que hay en el parentesis.

#TIPOS DE DATOS
#Definir, encabezado. 

nombre =" inna" #string/cadena de caracteres, Char="h"(uno). "str"
anio = 2024 #entero "int"
altura = 1.60 #decimal "float"
trabajando = False #booleano "bool"

#FUNCION print [mensaje]  y type
#NOTA: type te devuelve si es un string, un entero, un decimal o un booleano.
print(type(nombre)) #type que tipo de dato tengo en el parentesis. REsponde al tipo de dato que es la variable
print(type(anio)) #print responde el msj dentro del parentesis. 
print(type(altura))
print(type(trabajando))

anio = 2024      #Python cambio el valor y tmb  el tipo de dato.


print(type(anio))
anio = "Inna"

#FUNCION input seria = leer [variable].Si tiene dos parentisis es una FUNCION   
edad = input("ingresar tu edad: ") #input = entrada de datos

#En edad guardaria el valor 

print(edad)

#Caracteristica de input vaa poner todo en caracteres=str
numero_uno = int(input ("ingresa un valor:  ")) #Int es un conversor. Pide el valor. Lo puedo convertir en todos los tipos de datos, siempre que se pueda

numero_dos = int(input ("ingresa un segundo valor: "))

#print(type(numero_uno))
#print(type(numero_dos))

resultado = numero_uno + numero_dos

print(resultado) 

#ERRORES (ES HACER UN CONDICIONAL MUY GRANDE)
#try: (intentr, intentar hacer esto con el bloque sino podes anda por este bloque (except) )
#print("auxiliar")
#except ValueError:
#print("auxiliar")

edad=18
if edad >18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")


