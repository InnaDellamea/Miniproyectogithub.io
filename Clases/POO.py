#Programacion orientada a objetos (POO)
#Organizar y estructurar nuetsro codigo para entender mas  facil, mantener y reutilizar.
#Abarca objetos, instancias y clases.
#Clases : class (planillas, plantillas), dentro de la clase vamos a tener atributos y metodos.
#Atributos: propiedades. Metodos: funcionalidades o acciones


#PLANILLS, CAMPOS QUE HAY QUE RELLENAR

#def calcular_distancias (velocidad, tiempo):  #No pertenece a la clase pero tiene relacion. 
 #   return velocidad * tiempo

#8km/h 2h > 160km

#class Coche:
    #ruedas = 4
    #ATRIBUTO#marca
    #modelo
    #color
    
    #CONSTRUCTOR (init) creando atributos de instancias(dinamicos ,variables)
   # def __init__(self, marca, modelo, color): #self ya viene con la clase. Hace referencia a la instancia misma
       # self.marca = marca
      #  self.modelo = modelo
     #   self.color = color
    
    
    #def acelerar(self):
      #  print(f"El {self.marca} {self.modelo} esta acelerado")
        
    #def frenar(self):
     #    print(f"El coche esta frenado")
    
    #@staticmethod   
    #def calcular_distancias (velocidad, tiempo): #metodo estatico
    #    return velocidad * tiempo
    
    #METODO de clase#acelerar()
    #Frenar()
    
    #Metodo de clase. se ejecuta en todas las instancias. 
    #@classmethod  #decorador lo pongo encima de una funcions, va a tener funcionaliades/ permisos nuevas
    #def incrementar_ruedas (cls):  
    #   cls.ruedas += 1
    
        

#instancionas u objetos

#OBEJTO        #INSTANCIA
#coche_franco = Coche("Toyota", "Etios", "Gris") 
#print(coche_franco.ruedas)
#coche_franco.incrementar_ruedas() 
#print(coche_franco.ruedas)

                     #constructores lo que esta dentro de ""
#coche_inna =Coche("Chevrolet", "Camaro", "Amarillo")
#coche_inna.frenar()
#Dicen que instanciar una clase, quiere decir llamar a la clase y recien cuando ya esta invocada es un objeto


#coche_seba =Coche("Chevrolet", "Camaro", "Amarillo")
#print(coche_seba.ruedas)

#CONTRUCTORES
#Cuando yo instancio la clase se ejecuta  la class 
#metodos estaticos: @staticmethod  


#SOLID
#Conjunto de cinco  principios de disenos hacia objetos de calidad.
#S - SINGLE RESPONSIBILITY PRINCIPLE
#O - OPEN/CLOSED PRINCIPLE
#L - LISKPV SUBSTITUTION PRINCIPLE
#I - INTERFACE SEGREGATION PRIINCIPLE
#D - DEPENDENCY INVERSION PRINCIPLE



# HERENCIA, POLIMORFISMO, ENCAPSULAMIENTO, METODOS MAGICOS (DUNDER METHODS), EJERCICIOS PRACTICOS
#planificar el codigo con una abstracion mas alta 

#HERENCIA
#class Vehiculo: 
 #   def __init__(self, marca, modelo ,color, ruedas):
  #    self.marca = marca
    #  self.modelo = modelo
     # self.color = color
      #self.ruedas= ruedas
      
      
    #def acelerar(self):
     #   print(f"El {self.marca} {self.modelo} esta acelerando")
    
   # def frenar(self):
    #    print (f"El {self.marca} {self.modelo} esta frenando")

#class Coche(Vehiculo):
    
 #   def __init__(self, marca, modelo, color, ruedas, duenio):
  #      super().__init__(marca, modelo, color, ruedas)
   #     self.duenio = duenio 
    
   # def bocina(self):
    #    print(f"{self.duenio} esta tocando bocina")

#class bicicleta (Vehiculo):
 #   def acelerar(self):
 #      print(f"La bicicleta {self.marca} {self.modelo} esta pedaleando")

#Coche_franco = Coche ("Chrevolet", "camaro", "amarillo", 4, "Franco")
#Coche_franco.bocina()

#vehiculo_inna = Vehiculo("Toyota", "Etios", "Gris", 4)
#vehiculo_inna.acelerar()

#vehiculo_franco = Vehiculo("Chrevolet", "camaro", "amarillo", 4)
#vehiculo_franco.frenar()

#HERENCIA MULTIPLE
#Clase padre 1

#class A:
   # def __init__(self):
  #      super().__init__()
 #       print("Soy la clase a❤")
       
        
 #Clase padre 2
#class B:
   # def __init__(self):
  #      super().__init__()
 #       print("soy la clase b💙")

#class C(A ,B):
   # def __init__(self):
  #      super().__init__()
 #       print("soy la clase c💜")

#print(f" MRO -> {C.__mro__}") #ORDEN DE RESOLUCION

#terminal  MRO -> (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

#prueba = C()
        
 
#POLIMORSMO  POLI=NUMEROSO MORFOS= FORMAS MUCHAS FORMAS
#DEFINIR LOS METODOS EN LAS CLASE PADRES CON SUS CLASES HIJAS

class Empleado:
    def __init__(self, nombre, sueldo_mensual):
        self.nombre = nombre 
        self.sueldo_mensual = sueldo_mensual
        
    def calcular_sueldo_anual(self):
        sueldo_anual = 12 * self.sueldo_mensual * (1 + 1/100)  #1%
        print(f"El sueldo anual de {self.nombre} (EMPLEADO) es de  ARS{sueldo_anual}.")
    
class Programdor (Empleado):
    
    def calcular_sueldo_anual(self):
        sueldo_anual = 12 * self.sueldo_mensual * (1 + 4/100)  #4%
        print(f"El sueldo anual de {self.nombre}  (PROGRAMADOR) es de ARS {sueldo_anual}.")

class Disenador (Empleado):
    
    def calcular_sueldo_anual(self):
        sueldo_anual = 12 * self.sueldo_mensual * (1 + 5/100) # 5% bonus
        print(f"El sueldo anual de {self.nombre} empleando DISENADOR  es de {sueldo_anual}.")


empleados = [
    Programdor( "Franco" , 1000),
    Disenador("Israel", 2500),
    Empleado("Nicolas",500),
    Programdor( "inna" , 1500),
    Disenador("Ana", 3500),
    Empleado("rob",800),
    
]
for empleado in empleados:
    empleado.calcular_sueldo_anual()













