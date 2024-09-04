import tkinter as tk

# Placeholder para la entrada de usuario
class PlaceholderEntry(tk.Entry):
    def __init__(self, master=None, placeholder='', *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = 'saddle brown'
        self.default_fg_color = self.cget('fg')

        # Inicializa el placeholder
        self.insert(0, self.placeholder)
        self.config(fg=self.placeholder_color)

        # Configura eventos para el campo de entrada
        self.bind('<FocusIn>', self.on_focus_in)
        self.bind('<FocusOut>', self.on_focus_out)

    def on_focus_in(self, event):
        if self.get() == self.placeholder:
            self.delete(0, tk.END)
            self.config(fg=self.default_fg_color)

    def on_focus_out(self, event):
        if not self.get():
            self.insert(0, self.placeholder)
            self.config(fg=self.placeholder_color)

    # Crear ventana de saludo

# Crea una nueva ventana que recibe el nombre de usuario
def abrir_ventana_saludo(nombre):
    ventana_saludo = tk.Toplevel()
    ventana_saludo.title("Entrada")
    ventana_saludo.geometry("670x700+300+0")
    
    saludo = f"Hola {nombre}! \n¿Qué comemos hoy?"
    etiqueta_saludo = tk.Label(ventana_saludo, text=saludo, font=("Courier", 16))
    etiqueta_saludo.pack(side=tk.TOP, pady=20, padx=20)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Recetario")
ventana.geometry("670x700+300+0")
ventana.resizable(0, 0)

# Campo usuario
label_usuario = tk.Label(ventana, text="Usuario", foreground="black", font=("Courier", 12, 'bold'))
label_usuario.place(x=200, y=500)  # Ajusta la posición de la etiqueta

# Agregar texto a la ventana con un Label
mensaje = tk.Label(ventana, text="Hola, soy tu chef personal, por favor ingresa tu nombre y presiona OK para continuar",
font=("Courier", 12), foreground="black", wraplength=400, justify="left")
mensaje.place(x=150, y=400)  # Ajustar la posición para que esté centrado y sea legible


# Ejemplo de entrada de usuario
entrada_usuario = PlaceholderEntry(ventana, placeholder="Ej: Juan", foreground="black", font=("Courier", 14))
entrada_usuario.place(x=205, y=525, width=230, height=35)  # Ajusta la posición y tamaño de la entrada

#MANEJO DEL BOTON "OK"
def manejar_boton_ok():
    nombre = entrada_usuario.get()
    if nombre != entrada_usuario.placeholder and nombre:  # Verifica que no sea el placeholder ni esté vacío
        abrir_ventana_saludo(nombre)

#BOTON "OK"
boton_ok = tk.Button(ventana, text="OK", command=manejar_boton_ok, foreground="black", activebackground="gold", activeforeground="black",
font=("Courier", 12))
boton_ok.place(x=455, y=527)  # Ajusta la posición del botón

# Correr la ventana
ventana.mainloop()