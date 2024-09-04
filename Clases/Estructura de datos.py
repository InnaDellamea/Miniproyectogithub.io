#Estructura de datos

#Listas 
#Colecciones ordenanas y mutables de elementos, permite elementos duplicados, son dinamica

mi_lista = [" Inna", "Chaco"," 24", "True", ["Argentina","Brasil","Chile"]]
print(mi_lista)

mi_lista_dos = [" Franco" ," 24" , "Argentina", mi_lista]
print(mi_lista_dos[3][4][2])

[' Inna', 'Chaco', ' 24', 'True', ['Argentina', 'Brasil', 'Chile']]

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sublista_uno = lista[2:7] #para
print(sublista_uno)

sublista_dos= lista[::-1]
print(sublista_dos)
#¿Que pasa si como el ejemplo pongo print(sublista [-1]. Lista python metodos

lista = ["Inna","chaco", 24, "True"]
print(lista)

lista.append ("Enzo")

print(lista)
#Pop?





#Tuplas () -> TUPLE  (vocales)
#Colecciones ordenanas y INmutables de elementos. (DNI, para que no se modifique)
tupla_uno = (" Inna", "Chaco"," 24", "True", "Argentina")
print(tupla_uno)






#Conjuntos {} -> SET
#Desordenados pero sus elementos son unico.
#Existe una funcion "LEN"
conjunto_uno = {"Inna", "Chaco","24", "True", "Argentina"}
print(conjunto_uno)


if "24" in conjunto_uno:
    print("Si se encuentra")
else:
    print("No se encuentra")

for elemento in conjunto_uno:
    print ("----------")
print(elemento)

conju_a = {1, 2, 3, 4}
conju_b = {3, 4, 5, 6}

#Union
print (conju_a | conju_b) # {1, 2, 3, 4, 5, 6}

#Interseccion
print( conju_a & conju_b) #{3, 4} va

#Diferecia
print (conju_a -conju_b) #{1, 2}

#Diferncia similar #Signo de potencia shift+6
print(conju_a ^ conju_b) #{1, 2, 5, 6}


#Diccionarios
