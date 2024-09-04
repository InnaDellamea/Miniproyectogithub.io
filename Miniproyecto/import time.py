import time
from tkinter import *
from tkinter import messagebox

# Creación/configuración de la ventana principal
ventana = Tk()
ventana.title('Temporizador')
ventana.geometry('400x400')
temp = 0
no_pausado = True

# Variables para almacenar tiempo
hora = StringVar()
minuto = StringVar()
segundo = StringVar()

# Estableciendo el valor predeterminado como 0
hora.set("00")
minuto.set("00")
segundo.set("00")

# Campos de entrada de tiempo
horaEntry = Entry(ventana, width=3, font=("Arial", 18), textvariable=hora, bg="#c799e1")
horaEntry.place(x=80, y=20)

minutoEntry = Entry(ventana, width=3, font=("Arial", 18), textvariable=minuto, bg="#c799e1")
minutoEntry.place(x=130, y=20)

segundoEntry = Entry(ventana, width=3, font=("Arial", 18), textvariable=segundo, bg="#c799e1")
segundoEntry.place(x=180, y=20)

# Función para iniciar el temporizador
def submit():
    global temp
    global no_pausado
    no_pausado = True

    try:
        temp = int(hora.get()) * 3600 + int(minuto.get()) * 60 + int(segundo.get())
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un valor correcto")
        return

    # Inicia el temporizador con after
    countdown()

def countdown():
    global temp
    if temp > 0 and no_pausado:
        mins, secs = divmod(temp, 60)
        horas_locales = 0
        if mins >= 60:
            horas_locales, mins = divmod(mins, 60)
        # Actualizar los valores de las variables
        hora.set(f"{horas_locales:02}")
        minuto.set(f"{mins:02}")
        segundo.set(f"{secs:02}")

        temp -= 1
        ventana.after(1000, countdown)  # Llama a countdown después de 1 segundo
    elif temp <= 0:
        messagebox.showinfo("Tiempo terminado", "¡El tiempo se ha agotado!")

# Función para detener el temporizador
def stop():
    global temp
    temp = 0
    hora.set("00")
    minuto.set("00")
    segundo.set("00")

def pausa():
    global no_pausado
    no_pausado = False

# Botones para controlar el temporizador
btn_start = Button(ventana, text="Establecer el tiempo", bd='5', command=submit)
btn_stop = Button(ventana, text="Detener", bd='5', command=stop)
btn_pause = Button(ventana, text="Pausa", bd='5', command=pausa)
btn_start.place(x=90, y=120)
btn_stop.place(x=90, y=160)
btn_pause.place(x=90, y=200)

ventana.mainloop()
