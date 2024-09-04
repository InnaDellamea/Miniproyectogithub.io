from tkinter import *

raiz=Tk()
raiz.title("Ventana de prueba")

#raiz.resizable(0,0) # Admite dos paramentros width, height,  buleanos (True o 0). No se puede redimencionar

raiz.iconbitmap("imagen/calcu.ico")
#Podemos cambiar la pluma que tiene de icono: conversor.ico... hay que tener una imagen descargada.ico.
raiz.geometry("650x350") #Cambia el ancho y el alto estandar
raiz.config(bg="blue") #bg=background, cambia le fondo 












raiz.mainloop()#siempre en ultimo lugar
