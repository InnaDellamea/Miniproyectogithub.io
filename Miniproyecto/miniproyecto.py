
import tkinter as tk
import time



#Modificar
ventana = tk.Tk()
ventana.title('Bienvenido')
ventana.geometry('400x400')


#Barra de desplazamiento
ventana = tk.Tk()
ventana.title('Barra de desplazamiento' )
ventana.geometry ('600x600' )
marco = tk.Frame(ventana)
marco.pack(padx = 10, pady = 10)
scrollbar = tk.Scrollbar (marco)
scrollbar .pack(side = tk.RIGHT, fill = tk.Y)
lista = tk.Listbox(marco, yscrollcommand
= scrollbar .set)
for i in range(100):
    lista.insert(tk.END, f'Elemento {i+1}')
lista.pack(side = tk.LEFT, fill =
tk.BOTH)
scrollbar .config(command = lista.yview)

# #Reloj
# ventana.title('Reloj simple')
# ventana.geometry('50x50')
# reloj = tk.Label(ventana, font =
# ('Arial', 14), bg = 'black', fg = 'white')
# def hora():
#     tiempo_actual = time.strftime('%H:%M:%S')
#     reloj.config(text = tiempo_actual)
# ventana.after(1000, hora)
# reloj.pack()
# hora()

# #Menu desplegable
# ventana.title('Menú desplegable')
# ventana.geometry('400x400')
# barra_menu = tk.Menu(ventana)
# ventana.config(menu=barra_menu)
# menu_principal = tk.Menu(barra_menu)
# barra_menu.add_cascade(label =
# 'Principal', menu=menu_principal)
# submenu = tk.Menu(menu_principal)
# menu_principal.add_cascade(label =
# 'Opciones', menu=submenu)
# submenu.add_command(label = 'Opción 1')
# submenu.add_command(label = 'Opción 2')
# submenu.add_command(label = 'Opción 3')
# submenu.add_command(label = 'Opción 4')
# submenu.add_command(label = 'Opción 5')
# submenu.add_command(label = 'Opción 6')
# submenu.add_command(label = 'Opción 7')



# #Lista de tareas
# ventana.geometry('400x600')
# ingreso_tarea = tk.Entry(ventana)
# ingreso_tarea.pack()
# def agregar_tarea():
#     tarea = ingreso_tarea.get()
#     if tarea:lista_tareas.insert(tk.END, tarea)
# ingreso_tarea.delete(0, tk.END)
# boton_agregar = tk.Button(ventana, text = 'Agregar tarea', command = agregar_tarea)
# boton_agregar.pack()
# def eliminar_tarea():
#     seleccion = lista_tareas.curselection()
#     if seleccion: lista_tareas.delete(seleccion)
# boton_eliminar = tk.Button (ventana, text = 'Eliminar  tarea', command = eliminar_tarea)
# boton_eliminar.pack()
# lista_tareas = tk.Listbox(ventana)
# lista_tareas.pack()






ventana.mainloop()


