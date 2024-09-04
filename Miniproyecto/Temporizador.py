import time 
from tkinter import *
#from PIL import Image, ImageTk 
from tkinter import messagebox


#Creacion/confing de la ventana principal
ventana = Tk() 
ventana.title('Menu')
ventana.geometry('400x400')
temp = 0
no_pausado = True

# # Cargar la imagen
# try:
#     image = Image.open("fondo2.jpg")
#     #photo = ImageTk.PhotoImage(image)
#     #label_imagen = Label(ventana, image=photo)
#     #label_imagen.place(x=0, y=0, relwidth=1, relheight=1)  # Esto coloca la imagen como fondo
# except Exception as e:
#     messagebox.showerror("Error", f"No se pudo cargar la imagen: {e}")
    
# Creación de la barra de menú
barra_menu = Menu(ventana)
ventana.config(menu=barra_menu)

# Creación del menú principal
menu_principal = Menu(barra_menu, bg="#D8BFD8",tearoff=0)
barra_menu.add_cascade(label='Principal',menu=menu_principal)

# Creacion del submenú
submenu = Menu(menu_principal,bg="#D8BFD8", tearoff=0)
menu_principal.add_cascade(label='Opciones', menu=submenu)

# Función para mostrar el temporizador
def mostrar_temporizador():
    # Crea una nueva ventana para el temporizador
    temporizador_ventana = Toplevel(ventana)
    temporizador_ventana.title("Temporizador")
    temporizador_ventana.geometry("300x200" )
    temporizador_ventana.config(bg="#D8BFD8")
    
    #Variables para almacenar tiempo
    hora = StringVar()
    minuto = StringVar()
    segundo = StringVar()

    #Estableciendo el valor predeterminado como 0
    hora.set ("00")
    minuto.set ("00")
    segundo.set ("00")

    #Campos de entrada de tiempo
    horaEntry = Entry(temporizador_ventana, width=3, font=("Arial", 18), 
                    textvariable=hora, bg="#c799e1")
    horaEntry.place (x=80, y=20)

    minutoEntry = Entry(temporizador_ventana, width=3, font=("Arial", 18), 
                    textvariable=minuto,bg="#c799e1")
    minutoEntry.place (x=130, y=20)

    segundoEntry = Entry(temporizador_ventana, width=3, font=("Arial", 18), 
                    textvariable=segundo,bg="#c799e1")
    segundoEntry.place (x=180, y=20)
    
    #Funion para iniciar temporizador
    def submit():
        #Conversion y validacion del tiempo
        global temp
        global no_pausado
        no_pausado = True # Esta

        try: 
            temp = int(hora.get()) * 3600 + int(minuto.get()) * 60 + int(segundo.get())      
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un valor correcto")
            return
        #Bucle del temporizador
        while temp > -1 and no_pausado:
            mins, secs = divmod(temp, 60)
            horas_locales = 0  # Cambié 'horas' a 'horas_locales' para evitar el conflicto con 'hora'
            if mins >= 60:
                horas_locales, mins = divmod(mins, 60)
            # Actualizar los valores de las variables
            hora.set(f"{horas_locales:02}")
            minuto.set(f"{mins:02}")
            segundo.set(f"{secs:02}")
                
            temporizador_ventana.update()
            time.sleep(1)
            
            if (temp <= 0):
                messagebox.showinfo("Tiempo terminado", "¡El tiempo se ha agotado!")
            temp -= 1
            
    #Funion para detener el temporizador
    def stop():
        global temp
        temp = 0
        hora.set(f"{'00':02}")
        minuto.set(f"{'00':02}")
        segundo.set(f"{'00':02}")
            
        temporizador_ventana.update()
    
    def pausa():
        global no_pausado
        no_pausado = False
        
    #Boton para establecer el tiempo - stop-
    btn_start = Button(temporizador_ventana, text="Establecer el tiempo", bd='5', command=submit)
    btn_stop = Button(temporizador_ventana, text="Detener", bd='5', command=stop)
    btn_pause = Button(temporizador_ventana, text="Pausa", bd='5', command=pausa)
    btn_start.place(x = 90, y= 120)
    btn_stop.place(x = 90, y= 160)
    btn_pause.place(x = 90, y= 190)

# Agregar la opción del temporizador al submenú
submenu.add_command(label='Temporizador', command=mostrar_temporizador)
# Otras opciones del submenú
submenu.add_command(label='Mis recetas')
submenu.add_command(label='Acerca de')

ventana.mainloop()



