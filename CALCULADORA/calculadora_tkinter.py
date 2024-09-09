import tkinter as tk
from operaciones import resta, sumar, multipliacion,division 

ventana = tk. Tk()
ventana.title("calculadora tkinter")
ventana.geometry("400x500")

label_num_uno = tk.Label(ventana, text ="Numero Uno")
label_num_uno.pack()

entry_num_dos =tk.Entry(ventana)
entry_num_dos.pack()


#crear variables para seleccionar la operacion

operaciones =tk.StringVar()
operaciones.set("+") #va a tener el valor  + por defecto (los va a asumar), pero se puede cambiar

#Creamos las funciones
def calcular():
    num_uno = float(entry_num_dos.get()) #get obtiene el numeor ingresado
    num_dos = float(entry_num_dos.get())
    
    operaciones = operaciones.get()

    if operaciones == "+" : ##== comparar, si operaciones es igual al signo mas va a sumar. si ponemos un signo = guarda una variable.
        resultado = sumar(num_uno,num_dos)
    elif operaciones == "-": 
        resultado = resta(num_uno, num_dos)
    elif operaciones == "*":  
        resultado = multiplicacion(num_uno, num_dos)
    elif operaciones == "/": 
        resultado= division(num_uno, num_dos)

#creacion de las operaciones
boton_sumar = tk.Button(ventana, text = "+", command=lambda:sumar())
boton_sumar.pack(side ="left, padx=10,pady=10")
boton_resta = tk.Button(ventana, text = "-", command=lambda:resta())
boton_resta.pack(side ="left, padx=10,pady=10")
boton_multiplicacion = tk.Button(ventana, text = "*", command=lambda:multiplicacion())
boton_multiplicacion.pack (side ="left, padx=10, pady=10")
boton_division = tk.Button(ventana, text = "/", command=lambda:division())
boton_division.pack(side ="left, padx=10, pady=10")

label_resultando = tk.Label(ventana, text="resultado")
label_resultando.pack()

ventana.mainloop
