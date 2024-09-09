#def saludar():
 #   return "Hola mundo"
#print("Hola mundo")



#         PARAMENTROS POSICIONALES (requerimientos)
#def suma(valor_uno, valor_dos): #parametros:variables que se ocupan dentro de la funcion 
 #   return valor_uno + valor_dos

#               Argumentos
#resultado = suma(6, 5)

#print(f"El resultado de la suma es {resultado}.")

#VALORES POR DEFECTOS
#def saludar(nombre,mensaje="HOLA"):  #se coloca al reves
 #   return f"{mensaje}, {nombre}" 

#print(saludar("comision 3"))
#print(saludar("buenos dias, comision 3"))
 
 
 # *ARGS produce una tupla
#def receta_de_cocina(nombre, *args):
    #nombre de la receta
 #   print(f"receta de {nombre}")
   # print("ingredientes:")
    #ingredients
    #for ingredientes in args:
 
#recetas_de_cocina("torta de limon", "Harina", "huevo", "leche", "limon"): 
#recetas_de_cocina("milanesa","carne")
#receta_de_cocina("papas frita","papas", "aceitne")#

# **KWARS PRODUCE DICCIONARIOS {calve : valor}

# INGRESANDO DATOS POR PARAMETROS

#def suma(**kwargs):
    #resultado = 0
    
    #for clave, valor in kwargs.items():
         #print(f"{clave} -> { valor }")
         #resultado += valor
        # print(f"resultado temporal: {resultado}")
        
    #RETORNANDO UN RESULTADO
 #   return resultado

                        #             PASANDO ARGUMENTOS
#print(f"el resultado de la suma es {suma(a=4, b=2, c=129, d=30)}")

#def operaciones(valor_uno, valor_dos):
 #   suma = valor_uno + valor_dos
  #  resta =valor_uno - valor_dos
    
   # return suma, resta 
#print (operaciones(10,5))
#resultado_uno, resultado_dos = operaciones (10, 5)

#print(f"el resultado de la suma es {resultado_uno}")
#print(f"el resultado de la resta es {resultado_dos}")

#nombre = "inna"
#def prueba():
 #   nombre="Inna"
  #  print(f"mi nombre es {nombre}")
    
    
#def pedir_nombre():
 #   nombre =input("escribir tu nombre: ")
  #  return nombre

#def saludar():
    #print(f"hola {pedir_nombre()}")  

#saludar()


#import random
#Generar el numero ganador
#numero_ganador = random.randint(1, 100)
#intentos = 0
#flag= True

#while flag:
    
    #if intentos = 5:
     #   print("Se te terminaron los intentos, sos re malo.Suerte para la prox.")
      #  break
    
        #Requerir adivinanza
       # adivinanza = input("Intruduce tu adivinanza")
        
    #if not adivinanza.isdigit():
    #        print("Por favor, ingrese un numero valido")
     #       continue
        
    #adivinanza = int(adivinanza)
    #intentos += 1
         
    #if adivinanza < numero_ganador:
     #    print("Friiiiiooo, numero bajo. Intente de nuevo")
    #elif adivinanza > numero_ganador:
     #   print("Frioo, numero muy alto. Intentne de nuevo")
    #else:
     #   print(f" Ganasteee!, Te llevo {intentos} intentos.")
        
#print("Gracias por jugar")
#Ver cual es el error


                