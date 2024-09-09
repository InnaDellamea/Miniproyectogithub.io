#Tkinter es una interfaz grafica (ventanas que como usuarios interactuamos)
import tkinter as tk

def saludar():
    
    texto_dos =tk.Label(ventana, text="Hola comision 3")
    texto_dos.pack()



ventana = tk.Tk() #creando mi primera interfaz (guardando)

ventana.title("Primer ejemplo Comision 3")
ventana.geometry("400x300") #tamano cuando inicia la ventana, dsp se puede modificar

texto_uno = tk.Label(ventana, text="Programa de saludos!",font=('Arial',20))
texto_uno.pack() #nos agrega el elemento a la ventana

boton_uno = tk.Button(ventana, text="Saludar", command=saludar) #saludar sin parentesis
boton_uno.pack()

ventana.mainloop() #funcion que se ejecuta, la ventana se abre cuando se pon e esta funcion


