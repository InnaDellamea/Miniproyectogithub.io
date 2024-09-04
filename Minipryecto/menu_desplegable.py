import time 
from tkinter import *
from tkinter import messagebox

# Creación/configuración de la ventana principal
ventana = Tk() 
ventana.title('Menú ')
ventana.geometry('400x400')

# Creación de la barra de menú
barra_menu = Menu(ventana)
ventana.config(menu=barra_menu)

# Creación del menú principal
menu_principal = Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label='Principal', menu=menu_principal)

# Submenú
submenu = Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label='Opciones', menu=submenu)

# Función para mostrar el temporizador 
def mostrar_temporizador():
    # Crea una nueva ventana para el temporizador
    temporizador_ventana = Toplevel(ventana)
    temporizador_ventana.title("Temporizador")
    temporizador_ventana.geometry("300x200")
    
    # Variables del temporizador
    hora = StringVar()
    minuto = StringVar()
    segundo = StringVar()
    
    # Estableciendo el valor predeterminado como 0
    hora.set("00")
    minuto.set("00")
    segundo.set("00")
    
    # Uso de la clase de entrada para tomar la entrada del usuario.
    horaEntry = Entry(ventana, width=3, font=("Arial", 18), textvariable=hora)
    horaEntry.place(x=80, y=20)

    minutoEntry = Entry(ventana, width=3, font=("Arial", 18), textvariable=minuto)
    minutoEntry.place(x=130, y=20)

    segundoEntry = Entry(ventana, width=3, font=("Arial", 18), textvariable=segundo)
    segundoEntry.place(x=180, y=20)

    # Botón
    btn = Button(ventana, text="Establecer el tiempo", bd='5')
    btn.place(x=70, y=120)

# Agregar la opción del temporizador al submenú
submenu.add_command(label='Temporizador', command=mostrar_temporizador)

# Otras opciones del submenú
submenu.add_command(label='Opción 1')
submenu.add_command(label='Opción 2')
submenu.add_command(label='Opción 3')

ventana.mainloop()
