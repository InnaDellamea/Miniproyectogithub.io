from io import StringIO
from logging import config
import tkinter as tk
import time
from PIL import Image, ImageTk
from typing import Self
from tkinter import messagebox, simpledialog
from tkinter import Scrollbar, Text
import traceback

# Placeholder para la entrada de usuario
class PlaceholderEntry(tk.Entry):
    def __init__(self, master=None, placeholder="", *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = "grey"
        self.default_fg_color = self.cget("fg")

        # Inicializa el placeholder
        self.insert(0, self.placeholder)
        self.config(fg=self.placeholder_color)

        # Configura eventos para el campo de entrada
        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)

    def on_focus_in(self, event):
        if self.get() == self.placeholder:
            self.delete(0, tk.END)
            self.config(fg=self.default_fg_color)

    def on_focus_out(self, event):
        if not self.get():
            self.insert(0, self.placeholder)
            self.config(fg=self.placeholder_color)


# Funcion para puntos suspensivos en textos largos
def truncate_text(text, max_length=18):
    return text[:max_length] + '...' if len(text) > max_length else text


# abre ventana de SALADO
def abrir_ventana_salado():
    ventana_saludo = tk.Toplevel()
    ventana_saludo.title("Ventana de Salado")
    ventana_saludo.geometry("570x600+300+0")
    ventana_saludo.resizable(width=False, height=False)
    ventana_saludo.iconbitmap("Miniproyecto/UNIFICADO/IMAGENES/035cook_113744.ico")

# Cargar la imagen de fondo
    try:
        imagen_fondo = Image.open("./Miniproyecto/UNIFICADO/IMAGENES/FONDO RECETAS SALADAS2.png")
        imagen_fondo = imagen_fondo.resize((570, 600), Image.Resampling.LANCZOS)
        fondo_ventana_saludo = ImageTk.PhotoImage(imagen_fondo)
        
        # Crear un label para la imagen de fondo y agregarlo a la ventana
        label_fondo = tk.Label(ventana_saludo, image=fondo_ventana_saludo)
        label_fondo.place(relwidth=1, relheight=1)
        
        # Mantener una referencia a la imagen
        ventana_saludo.fondo_ventana_saludo = fondo_ventana_saludo
    except Exception as e:
        print(f"Error al cargar la imagen: {e}")
        # Si hay un error, continúa sin la imagen de fondo
        
        # Botón Volver
    boton_volver = tk.Button(
        ventana_saludo,  # Aquí debe ser la ventana que creaste
        text="Volver",
        command=ventana_saludo.destroy,  # Cierra la ventana ventana_saludo
        bg="#193eba", 
        fg="white",
        font=("Roboto Condensed", 15, "bold")
    )
    boton_volver.place(x=250, y=550) 
    # ------------------------------------------------------- RECETAS SALADAS (Cami) ---------------------------------------------------------------------------
    def milanesa_napo():
        try:
            ventana_mila_napo = tk.Toplevel()
            ventana_mila_napo.title("Milanesas a la napolitana")
            ventana_mila_napo.geometry("570x600+300+0")
            ventana_mila_napo.resizable(width=False, height=False)
            ventana_mila_napo.iconbitmap("Miniproyecto/UNIFICADO/IMAGENES/035cook_113744.ico")

            # Cargar la imagen de fondo
            imagen_fondo = Image.open("./Miniproyecto/UNIFICADO/IMAGENES/Milas napo.png")
            imagen_fondo = imagen_fondo.resize((570, 600), Image.Resampling.LANCZOS)
            fondo_ventana = ImageTk.PhotoImage(imagen_fondo)
            
            label_fondo = tk.Label(ventana_mila_napo, image=fondo_ventana)
            label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
            ventana_mila_napo.fondo_ventana = fondo_ventana
            # Botón Volver
            boton_volver = tk.Button(
                ventana_mila_napo,
                text="Volver",
                command=ventana_mila_napo.destroy,  # Cierra la ventana
                bg="#1979d8", 
                fg="white",
                font=("Roboto Condensed", 10, "bold")
            )
            boton_volver.place(x=15, y=25)  # Posiciona el botón en la parte inferior
        except Exception as e:
            print(f"Error en milanesa_napo: {e}")
    def empanadas_carne():
        try:
            ventana_empanadas_carne = tk.Toplevel()
            ventana_empanadas_carne.title("Empanadas de carne")
            ventana_empanadas_carne.geometry("570x600+300+0")
            ventana_empanadas_carne.resizable(width=False, height=False)
            ventana_empanadas_carne.iconbitmap("Miniproyecto/UNIFICADO/IMAGENES/035cook_113744.ico")
            
            # Cargar la imagen de fondo
            imagen_fondo = Image.open("./Miniproyecto/UNIFICADO/IMAGENES/Empanadas de carne.png")
            imagen_fondo = imagen_fondo.resize((570, 600), Image.Resampling.LANCZOS)
            fondo_ventana = ImageTk.PhotoImage(imagen_fondo)
            
            label_fondo = tk.Label(ventana_empanadas_carne, image=fondo_ventana)
            label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
            
            ventana_empanadas_carne.fondo_ventana = fondo_ventana

           # Botón Volver
            boton_volver = tk.Button(
                ventana_empanadas_carne,
                text="Volver",
                command=ventana_empanadas_carne.destroy,  # Cierra la ventana
                bg="#1979d8", 
                fg="white",
                font=("Roboto Condensed", 10, "bold")
            )
            boton_volver.place(x=15, y=25)  # Posiciona el botón en la parte inferior
        except Exception as e:
            print(f"Error en empanadas_carne: {e}")

    def milanesa_pollo():
        try:
            ventana_milanesas_pollo = tk.Toplevel()
            ventana_milanesas_pollo.title("Milanesas de pollo")
            ventana_milanesas_pollo.geometry("570x600+300+0")
            ventana_milanesas_pollo.resizable(width=False, height=False)
            ventana_milanesas_pollo.iconbitmap("Miniproyecto/UNIFICADO/IMAGENES/035cook_113744.ico")
            
            # Cargar la imagen de fondo
            imagen_fondo = Image.open("./Miniproyecto/UNIFICADO/IMAGENES/Milas de pollo.png")
            imagen_fondo = imagen_fondo.resize((570, 600), Image.Resampling.LANCZOS)
            fondo_ventana = ImageTk.PhotoImage(imagen_fondo)
            
            label_fondo = tk.Label(ventana_milanesas_pollo, image=fondo_ventana)
            label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
            
            ventana_milanesas_pollo.fondo_ventana = fondo_ventana

           
           # Botón Volver
            boton_volver = tk.Button(
                ventana_milanesas_pollo,
                text="Volver",
                command=ventana_milanesas_pollo.destroy,  # Cierra la ventana
                bg="#1979d8", 
                fg="white",
                font=("Roboto Condensed", 10, "bold")
            )
            boton_volver.place(x=15, y=25)  # Posiciona el botón en la parte inferior
        except Exception as e:
            print(f"Error en milanesas_pollo: {e}")



    def asado_ensalada():
        try:
            ventana_asado_con_ensalada = tk.Toplevel()
            ventana_asado_con_ensalada.title("Asado con ensalada criolla")
            ventana_asado_con_ensalada.geometry("570x600+300+0")
            ventana_asado_con_ensalada.resizable(width=False, height=False)
            ventana_asado_con_ensalada.iconbitmap("Miniproyecto/UNIFICADO/IMAGENES/035cook_113744.ico")

            # Cargar la imagen de fondo
            imagen_fondo = Image.open("./Miniproyecto/UNIFICADO/IMAGENES/Asado.png")
            imagen_fondo = imagen_fondo.resize((570, 600), Image.Resampling.LANCZOS)
            fondo_ventana = ImageTk.PhotoImage(imagen_fondo)
            
            label_fondo = tk.Label(ventana_asado_con_ensalada, image=fondo_ventana)
            label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
            
            ventana_asado_con_ensalada.fondo_ventana = fondo_ventana

           # Botón Volver
            boton_volver = tk.Button(
                ventana_asado_con_ensalada,
                text="Volver",
                command=ventana_asado_con_ensalada.destroy,  # Cierra la ventana
                bg="#1979d8", 
                fg="white",
                font=("Roboto Condensed", 10, "bold")
            )
            boton_volver.place(x=15, y=25)  # Posiciona el botón en la parte inferior
        except Exception as e:
            print(f"Error en asado_con_ensalada: {e}")


    def lentejas_guisadas():
        try:
            ventana_lentejas_guisadas = tk.Toplevel()
            ventana_lentejas_guisadas.title("Lentejas guisadas")
            ventana_lentejas_guisadas.geometry("570x600+300+0")
            ventana_lentejas_guisadas.resizable(width=False, height=False)
            ventana_lentejas_guisadas.iconbitmap("Miniproyecto/UNIFICADO/IMAGENES/035cook_113744.ico")
            
            # Cargar la imagen de fondo
            imagen_fondo = Image.open("./Miniproyecto/UNIFICADO/IMAGENES/Lentejas guisadas.png")
            imagen_fondo = imagen_fondo.resize((570, 600), Image.Resampling.LANCZOS)
            fondo_ventana = ImageTk.PhotoImage(imagen_fondo)
            
            label_fondo = tk.Label(ventana_lentejas_guisadas, image=fondo_ventana)
            label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
            
            ventana_lentejas_guisadas.fondo_ventana = fondo_ventana

            
           # Botón Volver
            boton_volver = tk.Button(
                ventana_lentejas_guisadas,
                text="Volver",
                command=ventana_lentejas_guisadas.destroy,  # Cierra la ventana
                bg="#1979d8", 
                fg="white",
                font=("Roboto Condensed", 10, "bold")
            )
            boton_volver.place(x=15, y=25)  # Posiciona el botón en la parte inferior
        except Exception as e:
            print(f"Error enlentejas_guisadas.: {e}")

    def pastas_bolognesa():
        try:
            ventana_pastas_bolognesa = tk.Toplevel()
            ventana_pastas_bolognesa.title("Pastas con salsa bolognesa")
            ventana_pastas_bolognesa.geometry("570x600+300+0")
            ventana_pastas_bolognesa.resizable(width=False, height=False)
            ventana_pastas_bolognesa.iconbitmap("Miniproyecto/UNIFICADO/IMAGENES/035cook_113744.ico")
            
            # Cargar la imagen de fondo
            imagen_fondo = Image.open("./Miniproyecto/UNIFICADO/IMAGENES/Pastas bolognesas.png")
            imagen_fondo = imagen_fondo.resize((570, 600), Image.Resampling.LANCZOS)
            fondo_ventana = ImageTk.PhotoImage(imagen_fondo)
            
            label_fondo = tk.Label(ventana_pastas_bolognesa, image=fondo_ventana)
            label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
            
            ventana_pastas_bolognesa.fondo_ventana = fondo_ventana
            # Botón Volver
            boton_volver = tk.Button(
                ventana_pastas_bolognesa,
                text="Volver",
                command=ventana_pastas_bolognesa.destroy,  # Cierra la ventana
                bg="#1979d8", 
                fg="white",
                font=("Roboto Condensed", 10, "bold")
            )
            boton_volver.place(x=15, y=25)  # Posiciona el botón en la parte inferior
        except Exception as e:
            print(f"Error en pastas_bolognesa.: {e}")


    def pollo_papas():
        try:
            ventana_pollo_papas = tk.Toplevel()
            ventana_pollo_papas.title("Pollo al horno con papas")
            ventana_pollo_papas.geometry("570x600+300+0")
            ventana_pollo_papas.resizable(width=False, height=False)
            ventana_pollo_papas.iconbitmap("Miniproyecto/UNIFICADO/IMAGENES/035cook_113744.ico")
            
            # Cargar la imagen de fondo
            imagen_fondo = Image.open("./Miniproyecto/UNIFICADO/IMAGENES/Pollo al horno con papas.png")
            imagen_fondo = imagen_fondo.resize((570, 600), Image.Resampling.LANCZOS)
            fondo_ventana = ImageTk.PhotoImage(imagen_fondo)
            
            label_fondo = tk.Label(ventana_pollo_papas, image=fondo_ventana)
            label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
            
            ventana_pollo_papas.fondo_ventana = fondo_ventana

           # Botón Volver
            boton_volver = tk.Button(
                ventana_pollo_papas,
                text="Volver",
                command=ventana_pollo_papas.destroy,  # Cierra la ventana
                bg="#1979d8", 
                fg="white",
                font=("Roboto Condensed", 10, "bold")
            )
            boton_volver.place(x=15, y=25)  # Posiciona el botón en la parte inferior
        except Exception as e:
            print(f"Error en pollo_papas.: {e}")


    def empanadas_jyq():
        try:
            ventana_empanada_jyq = tk.Toplevel()
            ventana_empanada_jyq.title("Empanadas de jamon y queso")
            ventana_empanada_jyq.geometry("570x600+300+0")
            ventana_empanada_jyq.resizable(width=False, height=False)
            ventana_empanada_jyq.iconbitmap("Miniproyecto/UNIFICADO/IMAGENES/035cook_113744.ico")
            
            # Cargar la imagen de fondo
            imagen_fondo = Image.open("./Miniproyecto/UNIFICADO/IMAGENES/Empanadas de jyq.png")
            imagen_fondo = imagen_fondo.resize((570, 600), Image.Resampling.LANCZOS)
            fondo_ventana = ImageTk.PhotoImage(imagen_fondo)
            
            label_fondo = tk.Label(ventana_empanada_jyq, image=fondo_ventana)
            label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
            
            ventana_empanada_jyq.fondo_ventana = fondo_ventana

           # Botón Volver
            boton_volver = tk.Button(
                ventana_empanada_jyq,
                text="Volver",
                command=ventana_empanada_jyq.destroy,  # Cierra la ventana
                bg="#1979d8", 
                fg="white",
                font=("Roboto Condensed", 10, "bold")
            )
            boton_volver.place(x=15, y=25)  # Posiciona el botón en la parte inferior
        except Exception as e:
            print(f"Error enempanadas_jyq.: {e}")

    def tarta_espinaca():
        try:
            ventana_tarta_espinaca = tk.Toplevel()
            ventana_tarta_espinaca.title("Tarta de espinaca y queso")
            ventana_tarta_espinaca.geometry("570x600+300+0")
            ventana_tarta_espinaca.resizable(width=False, height=False)
            ventana_tarta_espinaca.iconbitmap("Miniproyecto/UNIFICADO/IMAGENES/035cook_113744.ico")
            
            # Cargar la imagen de fondo
            imagen_fondo = Image.open("./Miniproyecto/UNIFICADO/IMAGENES/Tarta de espinaca y queso.png")
            imagen_fondo = imagen_fondo.resize((570, 600), Image.Resampling.LANCZOS)
            fondo_ventana = ImageTk.PhotoImage(imagen_fondo)
            
            label_fondo = tk.Label(ventana_tarta_espinaca, image=fondo_ventana)
            label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
            
            ventana_tarta_espinaca.fondo_ventana = fondo_ventana

           # Botón Volver
            boton_volver = tk.Button(
                ventana_tarta_espinaca,
                text="Volver",
                command=ventana_tarta_espinaca.destroy,  # Cierra la ventana
                bg="#1979d8", 
                fg="white",
                font=("Roboto Condensed", 10, "bold")
            )
            boton_volver.place(x=15, y=25)  # Posiciona el botón en la parte inferior
        except Exception as e:
            print(f"Error en tarata_espinaca.: {e}")


    def guiso_res():
        try:
            ventana_guiso_res = tk.Toplevel()
            ventana_guiso_res.title("Guiso de res con papas")
            ventana_guiso_res.geometry("570x600+300+0")
            ventana_guiso_res.resizable(width=False, height=False)
            ventana_guiso_res.iconbitmap("Miniproyecto/UNIFICADO/IMAGENES/035cook_113744.ico")
            
            # Cargar la imagen de fondo
            imagen_fondo = Image.open("./Miniproyecto/UNIFICADO/IMAGENES/Guiso de res con papas.png")
            imagen_fondo = imagen_fondo.resize((570, 600), Image.Resampling.LANCZOS)
            fondo_ventana = ImageTk.PhotoImage(imagen_fondo)
            
            label_fondo = tk.Label(ventana_guiso_res, image=fondo_ventana)
            label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
            
            ventana_guiso_res.fondo_ventana = fondo_ventana

           # Botón Volver
            boton_volver = tk.Button(
                ventana_guiso_res,
                text="Volver",
                command=ventana_guiso_res.destroy,  # Cierra la ventana
                bg="#1979d8", 
                fg="white",
                font=("Roboto Condensed", 10, "bold")
            )
            boton_volver.place(x=15, y=25)  # Posiciona el botón en la parte inferior
        except Exception as e:
            print(f"Error en guiso_res.: {e}")

    def quiche_jyq(): 
        try: 
            ventana_quiche_jyq = tk.Toplevel()
            ventana_quiche_jyq.title("Quiche de jamon y queso")
            ventana_quiche_jyq.geometry("570x600+300+0")
            ventana_quiche_jyq.resizable(width=False, height=False)
            ventana_quiche_jyq.iconbitmap("Miniproyecto/UNIFICADO/IMAGENES/035cook_113744.ico")

            # Cargar la imagen de fondo
            imagen_fondo = Image.open("./Miniproyecto/UNIFICADO/IMAGENES/Quiche de jyq.png")
            imagen_fondo = imagen_fondo.resize((570, 600), Image.Resampling.LANCZOS)
            fondo_ventana = ImageTk.PhotoImage(imagen_fondo)
            
            label_fondo = tk.Label(ventana_quiche_jyq, image=fondo_ventana)
            label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
            
            ventana_quiche_jyq.fondo_ventana = fondo_ventana

            # Botón Volver
            boton_volver = tk.Button(
                ventana_quiche_jyq,
                text="Volver",
                command=ventana_quiche_jyq.destroy,  # Cierra la ventana
                bg="#1979d8", 
                fg="white",
                font=("Roboto Condensed", 10, "bold")
            )
            boton_volver.place(x=15, y=25)  # Posiciona el botón en la parte inferior
        except Exception as e:
            print(f"Error en quiche_jyq.: {e}")

    def fideos_tuco():
        try:
            ventana_fideos_tuco = tk.Toplevel()
            ventana_fideos_tuco.title("Fideos con tuco")
            ventana_fideos_tuco.geometry("570x600+300+0")
            ventana_fideos_tuco.resizable(width=False, height=False)
            ventana_fideos_tuco.iconbitmap("Miniproyecto/UNIFICADO/IMAGENES/035cook_113744.ico")

            # Cargar la imagen de fondo
            imagen_fondo = Image.open("./Miniproyecto/UNIFICADO/IMAGENES/Fideos con tuco.png")
            imagen_fondo = imagen_fondo.resize((570, 600), Image.Resampling.LANCZOS)
            fondo_ventana = ImageTk.PhotoImage(imagen_fondo)
            
            label_fondo = tk.Label(ventana_fideos_tuco, image=fondo_ventana)
            label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
            
            ventana_fideos_tuco.fondo_ventana = fondo_ventana

            # Botón Volver
            boton_volver = tk.Button(
                ventana_fideos_tuco,
                text="Volver",
                command=ventana_fideos_tuco.destroy,  # Cierra la ventana
                bg="#1979d8", 
                fg="white",
                font=("Roboto Condensed", 10, "bold")
            )
            boton_volver.place(x=15, y=25)  # Posiciona el botón en la parte inferior
        except Exception as e:
            print(f"Error en fideos_tuco.: {e}")


#----------------------------------------------------- Botones de recetas saladas----------------------------------------------------------------

    STYLES_salado = {
    "font": ("Roboto Condensed", 12),
    "width": 16,
    "height": 2,
    "fg": "white",
    "bg": "#1B1270",
    "borderwidth": 0,
    "relief": "flat",
    "activebackground": "#1B1270",
    "activeforeground": "gold"
}

    # Boton 1: Milanesas a la napo
    boton_receta_uno = tk.Button(
        ventana_saludo,
        text="""Milanesas a la 
    napolitana""",
        command=milanesa_napo,
        **STYLES_salado
    )
    boton_receta_uno.pack()  
    boton_receta_uno.place(x=40, y=175)

    # Boton 2: Empanadas de carne
    boton_receta_dos = tk.Button(
        ventana_saludo,
        text="""Empanadas de 
    carne""",
        command=empanadas_carne,
        **STYLES_salado
    )
    boton_receta_dos.pack() 
    boton_receta_dos.place(x=218, y=175)
    
    # Boton 3: Milanesas de poll
    boton_receta_tres = tk.Button(
        ventana_saludo,
        text="""Milanesas de 
    pollo""",
        command=milanesa_pollo,
        **STYLES_salado 
    )
    boton_receta_tres.pack()  
    boton_receta_tres.place(x=395, y=175)

    # Boton 4: Asado con ensalada criolla
    boton_receta_cuatro = tk.Button(
        ventana_saludo,
        text="""Asado con 
    ensalada criolla""",
        command=asado_ensalada,
        **STYLES_salado
    )
    boton_receta_cuatro.pack()
    boton_receta_cuatro.place(x=40, y=265)

    # Boton 5: Lentejas guisadas
    boton_receta_cinco = tk.Button(
        ventana_saludo,
        text="Lentejas guisadas",
        command=lentejas_guisadas,
        **STYLES_salado
    )
    boton_receta_cinco.pack() 
    boton_receta_cinco.place(x=218, y=265)

    # Boton 6: Pastas con salsa bolognesa
    boton_receta_seis = tk.Button(
        ventana_saludo,
        text="""Pastas con 
    salsa bolognesa""",
        command=pastas_bolognesa,
        **STYLES_salado
    )
    boton_receta_seis.pack() 
    boton_receta_seis.place(x=395, y=265)

    # Boton 7: Pollo al horno con papas
    boton_receta_siete = tk.Button(
        ventana_saludo,
        text="""Pollo al horno 
    con papas""",
        command=pollo_papas,
        **STYLES_salado
    )
    boton_receta_siete.pack() 
    boton_receta_siete.place(x=40, y=350)

    # Boton 8: Empanadas de jamon y queso
    boton_receta_ocho = tk.Button(
        ventana_saludo,
        text="""Empanadas de 
    jamon y queso""",
        command=empanadas_jyq,
        **STYLES_salado
    )
    boton_receta_ocho.pack() 
    boton_receta_ocho.place(x=220, y=350)

    # Boton 9: Tarta de espinaca y queso
    boton_receta_nueve = tk.Button(
        ventana_saludo,
        text="""Tarta espinaca 
    y queso""",
        command=tarta_espinaca,
        **STYLES_salado
    )
    boton_receta_nueve.pack() 
    boton_receta_nueve.place(x=395, y=350)

    # Boton 10: Guiso de res con papas
    boton_receta_diez = tk.Button(
        ventana_saludo,
        text="""Guiso de res 
    con papas""",
        command=guiso_res,
        **STYLES_salado
    )
    boton_receta_diez.pack() 
    boton_receta_diez.place(x=40, y=440)


    # Boton 11: Quiche de jamon y queso
    boton_receta_once = tk.Button(
        ventana_saludo,
        text="""Quiche de 
    jamon y queso""",
        command=quiche_jyq,
        **STYLES_salado
    )
    boton_receta_once.pack()  
    boton_receta_once.place(x=215, y=440)

    # Boton 12: Fideos con tuco
    boton_receta_doce = tk.Button(
        ventana_saludo,
        text="Fideos con tuco",
        command=fideos_tuco,
        **STYLES_salado
    )
    boton_receta_doce.pack() 
    boton_receta_doce.place(x=395, y=440)


    # ---------------------------------------------------------RECETAS DULCES (Ile) -----------------------------------------------------------------------------

# abre ventana de DULCE
def abrir_ventana_dulce():
    ventana_saludo = tk.Toplevel()
    ventana_saludo.title("Ventana de Dulce")
    ventana_saludo.geometry("570x600+300+0")
    ventana_saludo.resizable(width=False, height=False)
    ventana_saludo.iconbitmap("Miniproyecto/UNIFICADO/IMAGENES/035cook_113744.ico")

# Cargar la imagen de fondo
    try:
        imagen_fondo = Image.open("./Miniproyecto/UNIFICADO/IMAGENES/FONDO DULCE2.png")
        imagen_fondo = imagen_fondo.resize((570, 600), Image.Resampling.LANCZOS)
        fondo_ventana_saludo = ImageTk.PhotoImage(imagen_fondo)
        
        # Crear un label para la imagen de fondo y agregarlo a la ventana
        label_fondo = tk.Label(ventana_saludo, image=fondo_ventana_saludo)
        label_fondo.place(relwidth=1, relheight=1)
        
        # Mantener una referencia a la imagen
        ventana_saludo.fondo_ventana_saludo = fondo_ventana_saludo
    except Exception as e:
        print(f"Error al cargar la imagen: {e}")
        # Si hay un error, continúa sin la imagen de fondo
        
         # Botón Volver
    boton_volver = tk.Button(
        ventana_saludo,  # Aquí debe ser la ventana que creaste
        text="Volver",
        command=ventana_saludo.destroy,  # Cierra la ventana ventana_saludo
        bg="#9c3c0f", 
        fg="white",
        font=("Roboto Condensed", 15, "bold")
    )
    boton_volver.place(x=250, y=550)  

    # ------------------------------------------------------FUNCIONES RECETAS DULCES -------------------------------------------------------------------------

    def cremaDeLimon():
        try:
            cremaDeLimon = tk.Toplevel()
            cremaDeLimon.title("Crema de Limón🍋")
            cremaDeLimon.geometry("570x600+300+0")
            cremaDeLimon.focus()
            cremaDeLimon.resizable(width=False, height=False)
            cremaDeLimon.iconbitmap("Miniproyecto/UNIFICADO/IMAGENES/035cook_113744.ico")

            # Cargar la imagen de fondo
            imagen_fondo = Image.open("./Miniproyecto/UNIFICADO/IMAGENES/Crema de limon.png")
            imagen_fondo = imagen_fondo.resize((570, 600), Image.Resampling.LANCZOS)
            fondo_ventana = ImageTk.PhotoImage(imagen_fondo)
            
            label_fondo = tk.Label(cremaDeLimon, image=fondo_ventana)
            label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
            
            cremaDeLimon.fondo_ventana = fondo_ventana

            # Botón Volver
            boton_volver = tk.Button(
                cremaDeLimon,
                text="Volver",
                command=cremaDeLimon.destroy,  # Cierra la ventana
                bg="#a9111f", 
                fg="white",
                font=("Roboto Condensed", 10, "bold")
            )
            boton_volver.place(x=15, y=25)  # Posiciona el botón en la parte inferior
        except Exception as e:
            print(f"Error en cremaDeLimon.: {e}")


    def VasitoOreo():
        try:
            VasitoOreo = tk.Toplevel()
            VasitoOreo.title("Vasito Oreo🍪")
            VasitoOreo.geometry("570x600+300+0")
            VasitoOreo.focus()
            VasitoOreo.resizable(width=False, height=False)
            VasitoOreo.iconbitmap("Miniproyecto/UNIFICADO/IMAGENES/035cook_113744.ico")

            # Cargar la imagen de fondo
            imagen_fondo = Image.open("./Miniproyecto/UNIFICADO/IMAGENES/Vasito oreo.png")
            imagen_fondo = imagen_fondo.resize((570, 600), Image.Resampling.LANCZOS)
            fondo_ventana = ImageTk.PhotoImage(imagen_fondo)
            
            label_fondo = tk.Label(VasitoOreo, image=fondo_ventana)
            label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
            
            VasitoOreo.fondo_ventana = fondo_ventana

           # Botón Volver
            boton_volver = tk.Button(
                VasitoOreo,
                text="Volver",
                command=VasitoOreo.destroy,  # Cierra la ventana
                bg="#a9111f", 
                fg="white",
                font=("Roboto Condensed", 10, "bold")
            )
            boton_volver.place(x=15, y=25)  # Posiciona el botón en la parte inferior
        except Exception as e:
            print(f"Error en VasitoOreo.: {e}")


    def Trufas_de_chocolate():
        try:
            Trufas_de_chocolate = tk.Toplevel()
            Trufas_de_chocolate.title("Trufas de chocolate")
            Trufas_de_chocolate.geometry("570x600+300+0")
            Trufas_de_chocolate.focus()
            Trufas_de_chocolate.resizable(width=False, height=False)
            Trufas_de_chocolate.iconbitmap("Miniproyecto/UNIFICADO/IMAGENES/035cook_113744.ico")
            
            # Cargar la imagen de fondo
            imagen_fondo = Image.open("./Miniproyecto/UNIFICADO/IMAGENES/Trufas de chocolate.png")
            imagen_fondo = imagen_fondo.resize((570, 600), Image.Resampling.LANCZOS)
            fondo_ventana = ImageTk.PhotoImage(imagen_fondo)
            
            label_fondo = tk.Label(Trufas_de_chocolate, image=fondo_ventana)
            label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
            
            Trufas_de_chocolate.fondo_ventana = fondo_ventana

           # Botón Volver
            boton_volver = tk.Button(
                Trufas_de_chocolate,
                text="Volver",
                command=Trufas_de_chocolate.destroy,  # Cierra la ventana
                bg="#a9111f", 
                fg="white",
                font=("Roboto Condensed", 10, "bold")
            )
            boton_volver.place(x=15, y=25)  # Posiciona el botón en la parte inferior
        except Exception as e:
            print(f"Error en Trufas_de_chocolate.: {e}")


    def galletasDeAvena():
        try:
            galletasDeAvena = tk.Toplevel()
            galletasDeAvena.title("Galletas de banana y avena🍪")
            galletasDeAvena.geometry("570x600+300+0")
            galletasDeAvena.focus()
            galletasDeAvena.resizable(width=False, height=False)
            galletasDeAvena.iconbitmap("Miniproyecto/UNIFICADO/IMAGENES/035cook_113744.ico")
            
            # Cargar la imagen de fondo
            imagen_fondo = Image.open("./Miniproyecto/UNIFICADO/IMAGENES/Galletas de banana y avena.png")
            imagen_fondo = imagen_fondo.resize((570, 600), Image.Resampling.LANCZOS)
            fondo_ventana = ImageTk.PhotoImage(imagen_fondo)
            
            label_fondo = tk.Label(galletasDeAvena, image=fondo_ventana)
            label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
            
            galletasDeAvena.fondo_ventana = fondo_ventana

            # Botón Volver
            boton_volver = tk.Button(
               galletasDeAvena,
                text="Volver",
                command=galletasDeAvena.destroy,  # Cierra la ventana
                bg="#a9111f", 
                fg="white",
                font=("Roboto Condensed", 10, "bold")
            )
            boton_volver.place(x=15, y=25)  # Posiciona el botón en la parte inferior
        except Exception as e:
            print(f"Error en galletasDeAvena.: {e}")


    def bocaditosDeAvenaYMiel():
        try:
            bocaditosDeAvenaYMiel = tk.Toplevel()
            bocaditosDeAvenaYMiel.title("Bocaditos de avena y miel🍮")
            bocaditosDeAvenaYMiel.geometry("570x600+300+0")
            bocaditosDeAvenaYMiel.focus()
            bocaditosDeAvenaYMiel.resizable(width=False, height=False)
            bocaditosDeAvenaYMiel.iconbitmap("Miniproyecto/UNIFICADO/IMAGENES/035cook_113744.ico")
        
            # Cargar la imagen de fondo
            imagen_fondo = Image.open("./Miniproyecto/UNIFICADO/IMAGENES/Bocaditos de miel y avena.png")
            imagen_fondo = imagen_fondo.resize((570, 600), Image.Resampling.LANCZOS)
            fondo_ventana = ImageTk.PhotoImage(imagen_fondo)
            
            label_fondo = tk.Label(bocaditosDeAvenaYMiel, image=fondo_ventana)
            label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
            
            bocaditosDeAvenaYMiel.fondo_ventana = fondo_ventana

            # Botón Volver
            boton_volver = tk.Button(
                bocaditosDeAvenaYMiel,
                text="Volver",
                command= bocaditosDeAvenaYMiel.destroy,  # Cierra la ventana
                bg="#a9111f", 
                fg="white",
                font=("Roboto Condensed", 10, "bold")
            )
            boton_volver.place(x=15, y=25)  # Posiciona el botón en la parte inferior
        except Exception as e:
            print(f"Error en bocaditosDeAvenaYMiel.: {e}")


    def flan():
        try:
            flan = tk.Toplevel()
            flan.title("Flan🍮")
            flan.geometry("570x600+300+0")
            flan.focus()
            flan.resizable(width=False, height=False)
            flan.iconbitmap("Miniproyecto/UNIFICADO/IMAGENES/035cook_113744.ico")
            
            # Cargar la imagen de fondo
            imagen_fondo = Image.open("./Miniproyecto/UNIFICADO/IMAGENES/Flan.png")
            imagen_fondo = imagen_fondo.resize((570, 600), Image.Resampling.LANCZOS)
            fondo_ventana = ImageTk.PhotoImage(imagen_fondo)
            
            label_fondo = tk.Label(flan, image=fondo_ventana)
            label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
            
            flan.fondo_ventana = fondo_ventana

           # Botón Volver
            boton_volver = tk.Button(
                flan,
                text="Volver",
                command=flan.destroy,  # Cierra la ventana
                bg="#a9111f", 
                fg="white",
                font=("Roboto Condensed", 10, "bold")
            )
            boton_volver.place(x=15, y=25)  # Posiciona el botón en la parte inferior
        except Exception as e:
            print(f"Error en flan.: {e}")


    def tartaDeYogur():
        try:
            tartaDeYogur = tk.Toplevel()
            tartaDeYogur.title("Tarta de Yogur🥧")
            tartaDeYogur.geometry("570x600+300+0")
            tartaDeYogur.focus()
            tartaDeYogur.resizable(width=False, height=False)
            tartaDeYogur.iconbitmap("Miniproyecto/UNIFICADO/IMAGENES/035cook_113744.ico")

            # Cargar la imagen de fondo
            imagen_fondo = Image.open("./Miniproyecto/UNIFICADO/IMAGENES/Tarta de yogur.png")
            imagen_fondo = imagen_fondo.resize((570, 600), Image.Resampling.LANCZOS)
            fondo_ventana = ImageTk.PhotoImage(imagen_fondo)
            
            label_fondo = tk.Label(tartaDeYogur, image=fondo_ventana)
            label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
            
            tartaDeYogur.fondo_ventana = fondo_ventana

            # Botón Volver
            boton_volver = tk.Button(
                tartaDeYogur,
                text="Volver",
                command=tartaDeYogur.destroy,  # Cierra la ventana
                bg="#a9111f", 
                fg="white",
                font=("Roboto Condensed", 10, "bold")
            )
            boton_volver.place(x=15, y=25)  # Posiciona el botón en la parte inferior
        except Exception as e:
            print(f"Error en tartaDeYogur.: {e}")


    def tartaDeNaranja():
        try:
            tartaDeNaranja = tk.Toplevel()
            tartaDeNaranja.title("Tarta de Naranja🍊")
            tartaDeNaranja.geometry("570x600+300+0")
            tartaDeNaranja.focus()
            tartaDeNaranja.resizable(width=False, height=False)
            tartaDeNaranja.iconbitmap("Miniproyecto/UNIFICADO/IMAGENES/035cook_113744.ico")
        
            # Cargar la imagen de fondo
            imagen_fondo = Image.open("./Miniproyecto/UNIFICADO/IMAGENES/Tarta de naranja.png")
            imagen_fondo = imagen_fondo.resize((570, 600), Image.Resampling.LANCZOS)
            fondo_ventana = ImageTk.PhotoImage(imagen_fondo)
            
            label_fondo = tk.Label(tartaDeNaranja, image=fondo_ventana)
            label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
            
            tartaDeNaranja.fondo_ventana = fondo_ventana

            # Botón Volver
            boton_volver = tk.Button(
                tartaDeNaranja,
                text="Volver",
                command=tartaDeNaranja.destroy,  # Cierra la ventana
                bg="#a9111f", 
                fg="white",
                font=("Roboto Condensed", 10, "bold")
            )
            boton_volver.place(x=15, y=25)  # Posiciona el botón en la parte inferior
        except Exception as e:
            print(f"Error en tartaDeNaranja.: {e}")


    def choco():
        try:
            choco = tk.Toplevel()
            choco.title("Postre de Chocolate🍫")
            choco.geometry("570x600+300+0")
            choco.focus()
            choco.resizable(width=False, height=False)
            choco.iconbitmap("Miniproyecto/UNIFICADO/IMAGENES/035cook_113744.ico")

            # Cargar la imagen de fondo
            imagen_fondo = Image.open("./Miniproyecto/UNIFICADO/IMAGENES/Postre de chocolate.png")
            imagen_fondo = imagen_fondo.resize((570, 600), Image.Resampling.LANCZOS)
            fondo_ventana = ImageTk.PhotoImage(imagen_fondo)
            
            label_fondo = tk.Label(choco, image=fondo_ventana)
            label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
            
            choco.fondo_ventana = fondo_ventana

           # Botón Volver
            boton_volver = tk.Button(
                choco,
                text="Volver",
                command=choco.destroy,  # Cierra la ventana
                bg="#a9111f", 
                fg="white",
                font=("Roboto Condensed", 10, "bold")
            )
            boton_volver.place(x=15, y=25)  # Posiciona el botón en la parte inferior
        except Exception as e:
            print(f"Error en choco.: {e}")

    def arrozCLeche():
        try:
            arrozCLeche = tk.Toplevel()
            arrozCLeche.title("Arroz con Leche🥣")
            arrozCLeche.geometry("570x600+300+0")
            arrozCLeche.focus()
            arrozCLeche.resizable(width=False, height=False)
            arrozCLeche.iconbitmap("Miniproyecto/UNIFICADO/IMAGENES/035cook_113744.ico")

            # Cargar la imagen de fondo
            imagen_fondo = Image.open("./Miniproyecto/UNIFICADO/IMAGENES/Arroz con leche.png")
            imagen_fondo = imagen_fondo.resize((570, 600), Image.Resampling.LANCZOS)
            fondo_ventana = ImageTk.PhotoImage(imagen_fondo)
            
            label_fondo = tk.Label(arrozCLeche, image=fondo_ventana)
            label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
            
            arrozCLeche.fondo_ventana = fondo_ventana

            # Botón Volver
            boton_volver = tk.Button(
                arrozCLeche,
                text="Volver",
                command=arrozCLeche.destroy,  # Cierra la ventana
                bg="#a9111f", 
                fg="white",
                font=("Roboto Condensed", 10, "bold")
            )
            boton_volver.place(x=15, y=25)  # Posiciona el botón en la parte inferior
        except Exception as e:
            print(f"Error en arrozCLeche.: {e}")


    def gelatina():
        try:
            gelatina = tk.Toplevel()
            gelatina.title("Gelatina de Fresa🍓")
            gelatina.geometry("570x600+300+0")
            gelatina.focus()
            gelatina.resizable(width=False, height=False)

            # Cargar la imagen de fondo
            imagen_fondo = Image.open("./Miniproyecto/UNIFICADO/IMAGENES/Gelatina de fresa.png")
            imagen_fondo = imagen_fondo.resize((570, 600), Image.Resampling.LANCZOS)
            fondo_ventana = ImageTk.PhotoImage(imagen_fondo)
            
            label_fondo = tk.Label(gelatina, image=fondo_ventana)
            label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
            
            gelatina.fondo_ventana = fondo_ventana

            # Botón Volver
            boton_volver = tk.Button(
                gelatina,
                text="Volver",
                command=gelatina.destroy,  # Cierra la ventana
                bg="#a9111f", 
                fg="white",
                font=("Roboto Condensed", 10, "bold")
            )
            boton_volver.place(x=15, y=25)  # Posiciona el botón en la parte inferior
        except Exception as e:
            print(f"Error en gelatina.: {e}")


    def brownie():
        try:
            brownie = tk.Toplevel()
            brownie.title("Brownie 🍫")
            brownie.geometry("570x600+300+0")
            brownie.focus()
            brownie.resizable(width=False, height=False)
            brownie.iconbitmap("Miniproyecto/UNIFICADO/IMAGENES/035cook_113744.ico")

            # Cargar la imagen de fondo
            imagen_fondo = Image.open("./Miniproyecto/UNIFICADO/IMAGENES/Brownie.png")
            imagen_fondo = imagen_fondo.resize((570, 600), Image.Resampling.LANCZOS)
            fondo_ventana = ImageTk.PhotoImage(imagen_fondo)
            
            label_fondo = tk.Label(brownie, image=fondo_ventana)
            label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
            
            brownie.fondo_ventana = fondo_ventana

           # Botón Volver
            boton_volver = tk.Button(
                brownie,
                text="Volver",
                command=brownie.destroy,  # Cierra la ventana
                bg="#a9111f", 
                fg="white",
                font=("Roboto Condensed", 10, "bold")
            )
            boton_volver.place(x=15, y=25)  # Posiciona el botón en la parte inferior
        except Exception as e:
            print(f"Error en brownie.: {e}")


#----------------------------------------------------- Botones de recetas dulces----------------------------------------------------------------

    STYLES_boton_dulce = {
    "font": ("Roboto Condensed", 12),
    "width": 16,
    "height": 2,
    "fg": "white",
    "bg": "#863808",
    "borderwidth": 0,
    "relief": "flat",
    "activebackground": "#863808",
    "activeforeground": "gold"
}

# Boton 1: 'Crema de Limón 🍋
    boton_receta_uno = tk.Button(ventana_saludo, 
                                text='''Crema de Limón''',
                                command=cremaDeLimon,
                                **STYLES_boton_dulce)
    boton_receta_uno.pack()  
    boton_receta_uno.place(x=40, y=178)


# Boton 2: Vasito Oreo 🍪
    boton_receta_dos = tk.Button(ventana_saludo, 
                                text='''Vasito Oreo''', 
                                command=VasitoOreo,
                                **STYLES_boton_dulce)
    boton_receta_dos.pack()  
    boton_receta_dos.place(x=218, y=178)


# Boton 3: Crepes 🫓
    boton_receta_tres = tk.Button(ventana_saludo, 
                            text='''Trufas de choclate''',
                            command=Trufas_de_chocolate,
                            **STYLES_boton_dulce)
    boton_receta_tres.pack()  
    boton_receta_tres.place(x=395, y=178)


# Boton 4: Galletas de Avena🍪
    boton_receta_cuatro = tk.Button(ventana_saludo, 
                                text='''Galletas de Avena''', 
                                command=galletasDeAvena,
                                **STYLES_boton_dulce)
    boton_receta_cuatro.pack()  
    boton_receta_cuatro.place(x=40, y=265)


# Boton 5: Bocaditos de miel y avena🍮
    button_text = "Bocados de miel y avena"
    truncated_text = truncate_text(button_text)

    boton_receta_cinco = tk.Button(ventana_saludo, 
                            text=truncated_text, 
                            command=bocaditosDeAvenaYMiel,
                               **STYLES_boton_dulce)
    boton_receta_cinco.pack()  
    boton_receta_cinco.place(x=218, y=265)

# Boton 6: Flan🍮
    boton_receta_seis = tk.Button(ventana_saludo, 
                                text='''Flan''', 
                                command=flan,
                                **STYLES_boton_dulce)
    boton_receta_seis.pack()  
    boton_receta_seis.place(x=395, y=265)

# Boton 7: Tarta de yogur al Horno 🥧
    boton_receta_siete = tk.Button(ventana_saludo, 
                                text='''Tarta de yogur''', 
                                command=tartaDeYogur,
                                **STYLES_boton_dulce)
    boton_receta_siete.pack()  
    boton_receta_siete.place(x=40, y=355)

# Boton 8: Tarta de Naranja🍊
    boton_receta_ocho = tk.Button(ventana_saludo, 
                                text='''Tarta de Naranja''', 
                                command=tartaDeNaranja,
                                **STYLES_boton_dulce)
    boton_receta_ocho.pack()  
    boton_receta_ocho.place(x=215, y=355)

# Boton 9: Postrecito de Chocolate🍫
    boton_receta_nueve = tk.Button(ventana_saludo, 
                                text='''Postre de Chocolate''', 
                                command=choco,
                                **STYLES_boton_dulce)
    boton_receta_nueve.pack()  
    boton_receta_nueve.place(x=395, y=355)

# Boton 10: Arroz con Leche 🥣
    boton_receta_diez = tk.Button(ventana_saludo, 
                                text='''Arroz con Leche''', 
                                command=arrozCLeche,
                                **STYLES_boton_dulce)
    boton_receta_diez.pack()  
    boton_receta_diez.place(x=40, y=445)

# Boton 11: Gelatina de Frutilla 🍓
    boton_receta_once = tk.Button(ventana_saludo, 
                                text='''Gelatina de Frutilla''', 
                                command=gelatina,
                                **STYLES_boton_dulce)
    boton_receta_once.pack()  
    boton_receta_once.place(x=218, y=445)

# Boton 12: 'Brownie 🍫'
    boton_receta_doce = tk.Button(ventana_saludo, 
                                text='Brownie ', 
                                command=brownie,
                                **STYLES_boton_dulce)
    boton_receta_doce.pack()  
    boton_receta_doce.place(x=395, y=445)


# Estilos para los botones mis recetas
STYLES_misRecetas = {
    "width": 20,
    "height": 5,
    "fg": "black",
    "bg": "#00E099",
    "borderwidth": 0,
    "relief": "flat",
    "activebackground": "#19B583",
    "activeforeground": "gold"
}

# abre ventana de MIS RECETAS

def abrir_ventana_mis_rece():
    ventana_saludo = tk.Toplevel()
    ventana_saludo.title("Mis Recetas")
    ventana_saludo.geometry("570x600+300+0")
    ventana_saludo.resizable(width=False, height=False)
    ventana_saludo.iconbitmap("Miniproyecto/UNIFICADO/IMAGENES/035cook_113744.ico")
    
    # Cargar la imagen de fondo
    try:
        imagen_fondo = Image.open("./Miniproyecto/UNIFICADO/IMAGENES/FONDO5.png")
        imagen_fondo = imagen_fondo.resize((570, 600), Image.Resampling.LANCZOS)
        fondo_ventana_saludo = ImageTk.PhotoImage(imagen_fondo)
        
        # Crear un label para la imagen de fondo y agregarlo a la ventana
        label_fondo = tk.Label(ventana_saludo, image=fondo_ventana_saludo)
        label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Mantener una referencia a la imagen
        ventana_saludo.fondo_ventana_saludo = fondo_ventana_saludo
        
        print("Imagen de fondo cargada con éxito")
    except Exception as e:
        print(f"Error al cargar la imagen: {e}")
        
             # Botón Volver
    boton_volver = tk.Button(
        ventana_saludo,  # Aquí debe ser la ventana que creaste
        text="Volver",
        command=ventana_saludo.destroy,  # Cierra la ventana ventana_saludo
        bg="#4bc40b", 
        fg="white",
        font=("Roboto Condensed", 12, "bold")
    )
    boton_volver.place(x=55, y=65)  


    recetas = {}  # las recetas que se agreguen se añaden en este conjunto

    # Creamos el frame de la ventana y lo asociamos a ventana_saludo
    frame = tk.Frame(ventana_saludo, bg='#2DC0A3')
    frame.place(x=42.5, y=140, width=493, height=440)
    

    # Usamos canvas para modificar de forma más fácil el diseño del marco
    canvas = tk.Canvas(frame, bg='#2DC0A3')
    scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollbar_marco = tk.Frame(canvas, bg='#2DC0A3')

    scrollbar_marco.bind(
        "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollbar_marco, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    title_label = tk.Label(
        scrollbar_marco,
        bg='white',
        fg='white' 
    )
    title_label.grid(row=0, column=0, columnspan=3, pady=10)
    def pedir_nombre_receta():
        # Crear una ventana Toplevel personalizada para pedir el nombre de la receta
        dialogo = tk.Toplevel(ventana_saludo)
        dialogo.title("Nueva Receta")
        dialogo.config(bg= "#2DC0A3")
        dialogo.iconbitmap("Miniproyecto/UNIFICADO/IMAGENES/035cook_113744.ico")
        dialogo.geometry("250x200")  

        tk.Label(dialogo,bg="#2DC0A3",text="Nombre de la receta:",font=("Arial")).pack(pady=10)
        
        nombre_receta_var = tk.StringVar()
        tk.Entry(dialogo,bg="#C3E8E6",textvariable=nombre_receta_var).pack(pady=10)
        
        def enviar():
            nombre_receta = nombre_receta_var.get()
            nombre_receta = nombre_receta[:18] + '...' if len(nombre_receta) > 18 else nombre_receta
            if nombre_receta:
                recetas[nombre_receta] = ""
                actualizar_recetas()
            dialogo.destroy()

        tk.Button(dialogo,bg="#C3E8E6", text="Aceptar", command=enviar).pack(pady=10)

    añadir_boton = tk.Button(
        scrollbar_marco,
        text="Agregar recetas",
        command=pedir_nombre_receta,
        **STYLES_misRecetas
    )
    añadir_boton.grid(row=1, column=1, pady=10)

    def actualizar_recetas():
        for widget in scrollbar_marco.winfo_children():
            if isinstance(widget, tk.Button) and widget != añadir_boton:
                widget.destroy()

        row, column = 1, 0
        for recipe in recetas:
            button = tk.Button(
                scrollbar_marco,
                font=("Roboto Condensed", 10),
                text=recipe,
                command=lambda r=recipe: editar_receta(r),
                **STYLES_misRecetas
            )
            button.grid(row=row, column=column, padx=5, pady=5)
            column += 1
            if column == 3:
                column = 0
                row += 1

        añadir_boton.grid(row=row, column=column, padx=5, pady=10)

    def editar_receta(nombre_receta):
        editar_ventana = tk.Toplevel(ventana_saludo)
        editar_ventana.title(nombre_receta)
        editar_ventana.geometry("570x600+300+0")
        editar_ventana.resizable(False, False)
        editar_ventana.configure(bg="#2DC0A3")
        editar_ventana.iconbitmap("Miniproyecto/UNIFICADO/IMAGENES/035cook_113744.ico")

        bloc_notas = tk.Text(editar_ventana, bg="#C3E8E6", font=("Arial"))
        bloc_notas.insert(tk.END, recetas[nombre_receta])
        bloc_notas.pack(expand=True, fill=tk.BOTH)

        boton_guardar = tk.Button(
            editar_ventana,
            text="Guardar",
            command=lambda: guardar_receta(
                nombre_receta, bloc_notas.get("1.0", tk.END)
            ),
            bg="#009A92", 
            activebackground="white",
            relief=tk.FLAT
        )
        boton_guardar.pack(side=tk.LEFT, padx=10, pady=10)

        boton_borrar = tk.Button(
            editar_ventana,
            text="Eliminar",
            command=lambda: eliminar_receta(nombre_receta, editar_ventana),
            bg="#009A92", 
            activebackground="white",
            relief=tk.FLAT
        )
        boton_borrar.pack(side=tk.RIGHT, padx=10, pady=10)

    def guardar_receta(nombre_receta, contenido):
        recetas[nombre_receta] = contenido
        messagebox.showinfo("Guardar", f"Receta '{nombre_receta}' guardada.")

    def eliminar_receta(nombre_receta, ventana):
        del recetas[nombre_receta]
        ventana.destroy()
        actualizar_recetas()

    print("Ventana 'Mis Recetas' creada")

# Cierra ventana mis recetas
def botonvolver():
    pass


# Función para abrir la ventana de saludo
def abrir_ventana_saludo(nombre):
    # Crear la ventana secundaria
    ventana_saludo = tk.Toplevel()
    ventana_saludo.title("Entrada")
    ventana_saludo.geometry("570x600+300+0")
    nombre_capitalizado = nombre.capitalize()
    ventana_saludo.resizable(width=False, height=False)
    ventana_saludo.iconbitmap("./Miniproyecto/UNIFICADO/IMAGENES/035cook_113744.ico") 

    #Cargar la imagen de fondo
    from PIL import Image, ImageTk

    try:
        fondo2 = Image.open("./Miniproyecto/UNIFICADO/IMAGENES/FONDO ENTRADA.png").resize((570, 600))
        fondo2_tk = ImageTk.PhotoImage(fondo2)

    except Exception as e:
        print(f"Error al cargar la imagen de fondo: {e}")
        return  # sale de la función si no se puede cargar la imagen

    # Crear y empaquetar la imagen de fondo
    label_fondo2 = tk.Label(ventana_saludo, image=fondo2_tk)
    label_fondo2.place(
        relwidth=1, relheight=1
    )  # Esto hace que el label de fondo cubra toda la ventana
    ventana_saludo.fondo2_tk = fondo2_tk

    saludo = tk.StringVar()

    def agregar_puntos_suspensivos(*args):
        texto = saludo.get()
        # Cortar el texto a 18 caracteres y añadir puntos suspensivos si es necesario
        if len(texto) > 22:
            saludo.set(texto[:18] + "...")
        else:
            saludo.set(texto)

    saludo.trace("w", agregar_puntos_suspensivos)
    saludo.set(nombre_capitalizado)  #Inicializar StringVar con el valor del nombre

#Crear el Label que usa el StringVar
    etiqueta_saludo = tk.Label(
        ventana_saludo,
        textvariable=saludo,
        font=("Roboto Condensed", 16),
        bg="#2B0E54",
        fg="#FFFFFF",
        wraplength=600, 
    )
    etiqueta_saludo.place(x=205, y=2)

#Creación de la barra de menú
    barra_menu = tk.Menu(ventana_saludo)
    ventana_saludo.config(menu=barra_menu)

#Creación del menú principal
    menu_principal = tk.Menu(barra_menu, bg="#D8BFD8", tearoff=0)
    barra_menu.add_cascade(label="MENU", menu=menu_principal)

#Creación del submenú
    submenu = tk.Menu(menu_principal, bg="#D8BFD8", tearoff=0)
    menu_principal.add_cascade(label="Opciones", menu=submenu)

#Añadir la opción "Acerca de" al menú desplegable
    submenu.add_command(label="Acerca de", command=mostrar_acerca_de)
    submenu.add_command(label="Temporizador", command=mostrar_temporizador)

#Botones de ventana principal
    btn_salado = tk.Button(
        ventana_saludo,
        text="Salado",
        bg="#2B0E54",
        fg="white",
        font=("Roboto Condensed", 12, "bold"),
        borderwidth=0,
        activebackground="#2B0E54",
        activeforeground="gold",
        relief="flat",
        width=10,
        height=4,
        command=abrir_ventana_salado,
    )
    btn_salado.place(x=45, y=365)

    btn_dulce = tk.Button(
        ventana_saludo,
        text="Dulce",
        bg="#2B0E54",
        fg="white",
        font=("Roboto Condensed", 12, "bold"),
        borderwidth=0,
        activebackground="#2B0E54",
        activeforeground="gold",
        relief="flat",
        width=10,
        height=4,
        command=abrir_ventana_dulce,
    )
    btn_dulce.place(x=230, y=365)

    btn_mis_rece = tk.Button(
        ventana_saludo,
        text="Mis recetas",
        bg="#2B0E54",
        fg="white",
        font=("Roboto Condensed", 12, "bold"),
        borderwidth=0,
        activebackground="#2B0E54",
        activeforeground="gold",
        relief="flat",
        width=10,
        height=4,
        command=abrir_ventana_mis_rece,
    )
    btn_mis_rece.place(x=410, y=365)


# Función para mostrar el temporizador
def mostrar_temporizador():
    temporizador_ventana = tk.Toplevel()  # Usar Toplevel en lugar de Tk
    temporizador_ventana.title("Temporizador")
    temporizador_ventana.geometry("300x300+300+0")
    temporizador_ventana.config(bg="#D8BFD8")
    temporizador_ventana.resizable(width=False, height=False)
    temporizador_ventana.iconbitmap("Miniproyecto/UNIFICADO/IMAGENES/activity.ico")

    hora = tk.StringVar(value="00")
    minuto = tk.StringVar(value="00")
    segundo = tk.StringVar(value="00")

    horaEntry = tk.Entry(temporizador_ventana, width=3, font=("Arial", 18), textvariable=hora, bg="#c799e1")
    horaEntry.place(x=80, y=20)
    minutoEntry = tk.Entry(temporizador_ventana, width=3, font=("Arial", 18), textvariable=minuto, bg="#c799e1")
    minutoEntry.place(x=130, y=20)
    segundoEntry = tk.Entry(temporizador_ventana, width=3, font=("Arial", 18), textvariable=segundo, bg="#c799e1")
    segundoEntry.place(x=180, y=20)

    tiempo_total = 0
    no_pausado = True

    def submit():
        nonlocal tiempo_total, no_pausado
        no_pausado = True

        try:
            h = int(hora.get())
            m = int(minuto.get())
            s = int(segundo.get())
            tiempo_total = h * 3600 + m * 60 + s
            if tiempo_total <= 0:
                raise ValueError("El tiempo debe ser mayor que cero")
            countdown()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def countdown():
        nonlocal tiempo_total
        if tiempo_total > 0 and no_pausado:
            mins, secs = divmod(tiempo_total, 60)
            horas, mins = divmod(mins, 60)
            hora.set(f"{horas:02d}")
            minuto.set(f"{mins:02d}")
            segundo.set(f"{secs:02d}")
            tiempo_total -= 1
            temporizador_ventana.after(1000, countdown)
        elif tiempo_total <= 0:
            messagebox.showinfo("Tiempo terminado", "¡El tiempo se ha agotado!")
            reset()

    def stop():
        nonlocal no_pausado
        no_pausado = False

    def reset():
        nonlocal tiempo_total, no_pausado
        tiempo_total = 0
        no_pausado = False
        hora.set("00")
        minuto.set("00")
        segundo.set("00")

    def pausa():
        nonlocal no_pausado
        no_pausado = not no_pausado
        if no_pausado:
            countdown()

    btn_start = tk.Button(temporizador_ventana, text="Iniciar", bd="5", command=submit)
    btn_stop = tk.Button(temporizador_ventana, text="Detener", bd="5", command=stop)
    btn_reset = tk.Button(temporizador_ventana, text="Reiniciar", bd="5", command=reset)

    btn_start.place(x=90, y=60)
    btn_stop.place(x=90, y=100)
    btn_reset.place(x=90, y=140)
    

# Función para cerrar una ventana
def cerrar_ventana(ventana):
    ventana.destroy()


# Función para mostrar la ventana "Acerca de"
def mostrar_acerca_de():
    ventana_acerca_de = tk.Toplevel()
    ventana_acerca_de.title("Acerca de")
    ventana_acerca_de.geometry("570x600+300+0")
    ventana_acerca_de.resizable(width=False, height=False)
    ventana_acerca_de.iconbitmap("Miniproyecto/UNIFICADO/IMAGENES/035cook_113744.ico")

    # Cargar la imagen de fondo
    try:
        imagen_fondo = Image.open("./Miniproyecto/UNIFICADO/IMAGENES/FONDO7.png")
        imagen_fondo = imagen_fondo.resize((570, 600), Image.Resampling.LANCZOS)
        fondo_ventana = ImageTk.PhotoImage(imagen_fondo)
        
        label_fondo = tk.Label(ventana_acerca_de, image=fondo_ventana)
        label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Mantener una referencia a la imagen
        ventana_acerca_de.fondo_ventana = fondo_ventana
        
        print("Imagen de fondo cargada con éxito")
    except Exception as e:
        print(f"Error al cargar la imagen de fondo: {e}")

    # Crear un Frame para el texto con scroll
    frame_texto = tk.Frame(ventana_acerca_de, bg='#300039')
    frame_texto.place(x=42.5, y=140, width=493, height=440)

    # Crear un Text con Scrollbar
    texto_container = tk.Frame(frame_texto, bg='#300039')
    texto_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    scrollbar = tk.Scrollbar(texto_container)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    texto = tk.Text(
        texto_container,
        height=20,
        width=60,
        wrap=tk.WORD,
        yscrollcommand=scrollbar.set,
        font=("Roboto Condensed", 12),
        bg='#300039',
        fg='white',
        border=0
    )
    texto.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=texto.yview)

    # Agregar el contenido
    contenido = """Somos COWORKING, una empresa joven y dinámica dedicada al desarrollo web, compuesta por un talentoso equipo de estudiantes del Informatorio, quienes representan las nuevas promesas en la industria de la programación.

Nuestro Equipo:
Pablo Sabadini: Con una pasión por la innovación y el desarrollo front-end, Pablo se asegura de que cada proyecto tenga una interfaz intuitiva y atractiva.

Camila Ledesma Falschini: Experta en diseño UX/UI, Camila transforma ideas en experiencias de usuario fluidas y visualmente impactantes.

Aguirre Eugenio Nicolás: Focalizado en la lógica y el desarrollo back-end, Eugenio asegura que cada solución sea sólida, escalable y eficiente.

Anabela Maciel: Especialista en bases de datos, Anabela se encarga de que la información sea gestionada de manera segura y óptima.

Darío Merentiel: Con un ojo crítico para los detalles, Darío trabaja en el aseguramiento de la calidad, asegurando que cada proyecto cumpla con los más altos estándares.

Ileana Fontana: Amante del código limpio y bien estructurado, Ileana es nuestra desarrolladora full-stack, integrando las mejores prácticas en cada etapa del desarrollo.

Roberto Galeano: Roberto es nuestro ingeniero de software, que combina conocimiento técnico con una visión estratégica para crear soluciones a medida.

Eduina Nicole Dellamea: Experta en gestión de proyectos, Eduina coordina al equipo para asegurar que cada entrega sea oportuna y cumpla con los objetivos del cliente.

Nuestra Misión:
En COWORKING, nuestra misión es desarrollar soluciones web que no solo cumplan, sino que superen las expectativas de nuestros clientes. Trabajamos en equipo para combinar nuestras fortalezas y crear productos que son funcionales, estéticamente agradables y de alta calidad.

Nuestros Valores:
Innovación: Estamos comprometidos a estar a la vanguardia de la tecnología, adoptando las últimas tendencias y herramientas en desarrollo web.

Colaboración: Creemos que las mejores soluciones nacen de un esfuerzo conjunto, tanto dentro de nuestro equipo como en estrecha colaboración con nuestros clientes.

Calidad: Nos enorgullece entregar productos que son confiables, seguros y construidos para durar.

Crecimiento Continuo: Como estudiantes del Informatorio, estamos en un aprendizaje constante, lo que nos permite adaptarnos rápidamente a las necesidades cambiantes del mercado.

Lo Que Nos Diferencia:
Compromiso con la Excelencia: Cada miembro de COWORKING aporta su experiencia y dedicación, lo que nos permite ofrecer soluciones de desarrollo web que destacan por su calidad y creatividad.

Enfoque Personalizado: Nos aseguramos de entender las necesidades específicas de cada cliente, brindando soluciones hechas a medida.

Futuro Prometedor: Como jóvenes talentos en la programación, nuestro enfoque fresco y actualizado nos permite abordar los desafíos desde una perspectiva innovadora.

Gracias por confiar en COWORKING. Estamos emocionados de llevar sus proyectos al siguiente nivel con nuestra pasión y habilidades en desarrollo web. ¡Juntos, construiremos el futuro digital!"""

    texto.insert(tk.END, contenido)
    texto.config(state=tk.DISABLED)

    # Botón Volver
    btn_volver = tk.Button(
        frame_texto,
        text="Volver",
        command=ventana_acerca_de.destroy,
        bg="white", 
        fg="black",
        activebackground="#5C1262", 
        activeforeground="white",
        font=("Roboto Condensed", 8, "bold"),
        relief=tk.FLAT,
        pady=2,
        padx=2
    )
    btn_volver.place(x=200, y=415)

    # Asegurarse de que la ventana se mantenga en primer plano
    ventana_acerca_de.transient(ventana_acerca_de.master)
    ventana_acerca_de.grab_set()
    ventana_acerca_de.wait_window(ventana_acerca_de)



# Configuración de la ventana principal (ANA)
ventana = tk.Tk()
ventana.title("Recetario")
ventana.geometry("570x600+300+0")
ventana.resizable(width=False, height=False)
ventana.iconbitmap("./Miniproyecto/UNIFICADO/IMAGENES/035cook_113744.ico")

# Carga la imagen de fondo
fondo = ImageTk.PhotoImage(
    Image.open("./Miniproyecto/UNIFICADO/IMAGENES/FONDO RECETARIO.png").resize((570, 600))
)


# Crea y empaqueta la imagen de fondo para que no se rompa en caso de que tkinter no cargue la imagen
label_fondo = tk.Label(ventana, image=fondo)
label_fondo.place(relwidth=1, relheight=1)

# Ejemplo de entrada de usuario
entrada_usuario = PlaceholderEntry(
    ventana,
    placeholder="Ej: Juan",
    foreground="white",
    bg="#300039",
    borderwidth=0,
    relief="flat",
    font=("Roboto Condensed", 14),
)
# Ajusta la posición y tamaño de la entrada
entrada_usuario.place(x=195, y=445, width=190, height=50)


# MANEJO DEL BOTON "OK"
def manejar_boton_ok():
    nombre = entrada_usuario.get()
    if (
        nombre != entrada_usuario.placeholder and nombre
    ):  # Verifica que no sea el placeholder ni esté vacío
        abrir_ventana_saludo(nombre)


# BOTON "OK"
boton_ok = tk.Button(
    ventana,
    text="OK",
    command=manejar_boton_ok,
    foreground="white",
    bg="#380039",
    borderwidth=0,
    relief="flat",
    activebackground="#380039",
    activeforeground="white",
    font=("Roboto Condensed", 15),
)
boton_ok.place(x=445, y=445, width=50, height=50)  # Ajusta la posición del botón


# Correr la ventana
ventana.mainloop()
