from io import StringIO
from logging import config
import tkinter as tk
import time
from PIL import Image, ImageTk
from typing import Self
from tkinter import messagebox, simpledialog
from tkinter import Scrollbar, Text

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

    # Crear ventana de saludo


# Crea una nueva ventana que recibe el nombre de usuario
# abre ventana de SALADO

def abrir_ventana_salado():
    ventana_saludo = tk.Toplevel()
    ventana_saludo.title("Ventana de Salado")
    ventana_saludo.geometry("670x700+300+0")
    ventana_saludo.resizable(width=False, height=False)

# Cargar la imagen de fondo
    try:
        imagen_fondo = Image.open("./Miniproyecto/UNIFICADO/IMAGENES/FONDO3.png")
        imagen_fondo = imagen_fondo.resize((670, 700), Image.Resampling.LANCZOS)
        fondo_ventana_saludo = ImageTk.PhotoImage(imagen_fondo)
        
        # Crear un label para la imagen de fondo y agregarlo a la ventana
        label_fondo = tk.Label(ventana_saludo, image=fondo_ventana_saludo)
        label_fondo.place(relwidth=1, relheight=1)
        
        # Mantener una referencia a la imagen
        ventana_saludo.fondo_ventana_saludo = fondo_ventana_saludo
    except Exception as e:
        print(f"Error al cargar la imagen: {e}")
        # Si hay un error, continúa sin la imagen de fondo

    # ------------------------------------------------------- RECETAS SALADAS (Cami) ---------------------------------------------------------------------------

    def milanesa_napo():
        ventana_mila_napo = tk.Toplevel()
        ventana_mila_napo.title("Milanesas a la napolitana")
        ventana_mila_napo.geometry("670x700+300+0")
        ventana_mila_napo.resizable(width=False, height=False)

        #   TITULO DE LA RECETA
        titulo = tk.Label(
            ventana_mila_napo,
            text="""Milanesas a la napolitana 🍕""",
            font=("Roboto Condensed", 18),
            foreground="black"
        )
        titulo.pack()
        titulo.place(x=195, y=40)

        #   INGREDIENTES
        ingredientes = tk.Label(
            ventana_mila_napo,
            text="""Ingredientes:

4 milanesas de carne de res
1 taza de pan rallado
1/2 taza de queso rallado
1 huevo
1 taza de salsa de tomate
100 g de jamón cocido
Aceite para freír
Sal y pimienta al gusto""",
            justify="left",
            font=("nunito", 12),
        )
        ingredientes.pack()
        ingredientes.place(x=15, y=100)

        #   PREPARACIÓN
        preparación = tk.Label(
            ventana_mila_napo,
            text="""Preparación:

Batir el huevo en un plato y mezclar el pan rallado con el queso rallado en otro.
Pasar las milanesas por el huevo y luego por la mezcla de pan rallado y queso.
Freír en aceite caliente hasta dorar y cocinar completamente. Colocar sobre papel 
absorbente.
Precalentar el horno a 180°C. Colocar las milanesas en una fuente para horno, cubrir 
con salsa de tomate, una loncha de jamón y más queso rallado.
Hornear durante 10-15 minutos o hasta que el queso esté fundido y dorado.""",
            justify="left",
            font=("nunito", 12),
        )
        preparación.pack()
        preparación.place(x=15, y=350)

    def empanadas_carne():
        ventana_empanadas_carne = tk.Toplevel()
        ventana_empanadas_carne.title("Empanadas de carne")
        ventana_empanadas_carne.geometry("670x700+300+0")
        ventana_empanadas_carne.resizable(width=False, height=False)

        #   TITULO DE LA RECETA
        titulo = tk.Label(
            ventana_empanadas_carne,
            text="""Empanadas de carne 🥟""",
            font=("nunito", 20),
        )
        titulo.pack()
        titulo.place(x=195, y=40)
        #   INGREDIENTES
        ingredientes = tk.Label(
            ventana_empanadas_carne,
            text="""Ingredientes:

500 g de carne de res picada
1 cebolla picada
1 pimiento rojo picado
2 huevos duros picados
10 aceitunas verdes picadas
1 cucharadita de comino
1 cucharadita de pimentón
Sal y pimienta al gusto
Masa para empanadas (puedes comprarla ya hecha o hacerla en casa)""",
            justify="left",
            font=("nunito", 12),
        )
        ingredientes.pack()
        ingredientes.place(x=15, y=100)

        #   PREPARACIÓN
        preparacion = tk.Label(
            ventana_empanadas_carne,
            text="""Preparación:

Sofreír la cebolla y el pimiento en una sartén con un poco de aceite hasta que 
estén tiernos.
Añadir la carne y cocinar hasta que esté bien dorada. Incorporar los huevos, 
aceitunas, comino, pimentón, sal y pimienta. Mezclar bien.
Dejar enfriar el relleno. Colocar una cucharada del relleno en cada disco de 
masa para empanadas, cerrar y sellar los bordes con un tenedor.
Hornear a 200°C durante 15-20 minutos o hasta que estén doradas.""",
            justify="left",
            font=("nunito", 12),
        )
        preparacion.pack()
        preparacion.place(x=15, y=350)

    def milanesa_pollo():
        ventana_milanesas_pollo = tk.Toplevel()
        ventana_milanesas_pollo.title("Milanesas de pollo")
        ventana_milanesas_pollo.geometry("670x700+300+0")
        ventana_milanesas_pollo.resizable(width=False, height=False)

        #   TITULO DE LA RECETA
        titulo = tk.Label(
            ventana_milanesas_pollo,
            text="""Milanesas de pollo 🍗""",
            font=("nunito", 20),
        )
        titulo.pack()
        titulo.place(x=195, y=40)

        #   INGREDIENTES
        ingredientes = tk.Label(
            ventana_milanesas_pollo,
            text="""Ingredientes:

4 pechugas de pollo
1 taza de pan rallado
1/2 taza de queso rallado
1 huevo
Sal y pimienta al gusto
Aceite para freír""",
            justify="left",
            font=("nunito", 12),
        )
        ingredientes.pack()
        ingredientes.place(x=15, y=100)

        #   PREPARACIÓN
        preparacion = tk.Label(
            ventana_milanesas_pollo,
            text="""Preparación:

Aplastar las pechugas de pollo para que queden más finas. Salpimentar.
Batir el huevo y mezclar el pan rallado con el queso rallado.
Pasar las pechugas por el huevo y luego por la mezcla de pan rallado.
Freír en aceite caliente hasta dorar y cocinar completamente. Servir con limón.
""",
            justify="left",
            font=("nunito", 12),
        )
        preparacion.pack()
        preparacion.place(x=15, y=350)

    def asado_ensalada():
        ventana_asado_con_ensalada = tk.Toplevel()
        ventana_asado_con_ensalada.title("Asado con ensalada criolla")
        ventana_asado_con_ensalada.geometry("670x700+300+0")
        ventana_asado_con_ensalada.resizable(width=False, height=False)

        #   TITULO DE LA RECETA
        titulo = tk.Label(
            ventana_asado_con_ensalada,
            text="""Asado con ensalada criolla 🥩""",
            font=("nunito", 20),
        )
        titulo.pack()
        titulo.place(x=195, y=40)

        #   INGREDIENTES
        ingredientes = tk.Label(
            ventana_asado_con_ensalada,
            text="""Ingredientes:

1 kg de costillas de res
Sal y pimienta al gusto
1 cucharada de pimentón
Ensalada Criolla:

2 tomates grandes, picados
1 cebolla, picada
1 pimiento verde, picado
1 pepino, picado
2 cucharadas de vinagre
3 cucharadas de aceite de oliva
Sal y pimienta al gusto""",
            justify="left",
            font=("nunito", 12),
        )
        ingredientes.pack()
        ingredientes.place(x=15, y=100)

        #   PREPARACIÓN
        preparacion = tk.Label(
            ventana_asado_con_ensalada,
            text="""Preparación:

Salpimentar las costillas y espolvorear con pimentón. Cocinar a la parrilla a fuego 
medio durante 40-50 minutos, girando ocasionalmente.
Para la ensalada, mezclar los tomates, cebolla, pimiento y pepino en un bol.
Añadir vinagre, aceite, sal y pimienta. Mezclar bien y servir con el asado.""",
            justify="left",
            font=("nunito", 12),
        )
        preparacion.pack()
        preparacion.place(x=15, y=440)

    def lentejas_guisadas():
        ventana_lentejas_guisadas = tk.Toplevel()
        ventana_lentejas_guisadas.title("Lentejas guisadas")
        ventana_lentejas_guisadas.geometry("670x700+300+0")
        ventana_lentejas_guisadas.resizable(width=False, height=False)

        #   TITULO DE LA RECETA
        titulo = tk.Label(
            ventana_lentejas_guisadas,
            text="""Lentejas guisadas 🍵""",
            font=("nunito", 20),
        )
        titulo.pack()
        titulo.place(x=195, y=40)

        #   INGREDIENTES
        ingredientes = tk.Label(
            ventana_lentejas_guisadas,
            text="""Ingredientes:

1 taza de lentejas
1 cebolla picada
1 zanahoria picada
2 dientes de ajo picados
1 pimiento verde picado
1 litro de caldo de verduras
1 cucharada de pimentón
Sal y pimienta al gusto
Aceite de oliva""",
            justify="left",
            font=("nunito", 12),
        )
        ingredientes.pack()
        ingredientes.place(x=15, y=100)

        #   PREPARACIÓN
        preparacion = tk.Label(
            ventana_lentejas_guisadas,
            text="""Preparación:

Sofreír la cebolla, zanahoria, ajo y pimiento en aceite hasta que 
estén tiernos.
Añadir las lentejas, el pimentón, el caldo, sal y pimienta. Cocinar a 
fuego lento durante 30-40 minutos, o hasta que las lentejas estén 
tiernas. Ajustar la sazón.""",
            justify="left",
            font=("nunito", 12),
        )
        preparacion.pack()
        preparacion.place(x=15, y=350)

    def pastas_bolognesa():
        ventana_pastas_bolognesa = tk.Toplevel()
        ventana_pastas_bolognesa.title("Pastas con salsa bolognesa")
        ventana_pastas_bolognesa.geometry("670x700+300+0")
        ventana_pastas_bolognesa.resizable(width=False, height=False)

        #   TITULO DE LA RECETA
        titulo = tk.Label(
            ventana_pastas_bolognesa,
            text="""Pastas con salsa bolognesa 🍝""",
            font=("nunito", 20),
        )
        titulo.pack()
        titulo.place(x=195, y=40)

        #   INGREDIENTES
        ingredientes = tk.Label(
            ventana_pastas_bolognesa,
            text="""Ingredientes:

250 g de pasta (espaguetis, penne, etc.)
300 g de carne picada de res
1 cebolla picada
2 dientes de ajo picados
1 zanahoria picada
400 g de salsa de tomate
1 cucharadita de orégano
Sal y pimienta al gusto
Queso rallado para servir""",
            justify="left",
            font=("nunito", 12),
        )
        ingredientes.pack()
        ingredientes.place(x=15, y=100)

        #   PREPARACIÓN
        preparacion = tk.Label(
            ventana_pastas_bolognesa,
            text="""Preparación:

Cocinar la pasta según las instrucciones del paquete.
Sofreír la cebolla, ajo y zanahoria en una sartén con aceite hasta que 
estén tiernos. Añadir la carne y cocinar hasta dorar.
Incorporar la salsa de tomate, orégano, sal y pimienta. Cocinar a fuego 
lento durante 20 minutos.
Mezclar con la pasta cocida y servir con queso rallado.""",
            justify="left",
            font=("nunito", 12),
        )
        preparacion.pack()
        preparacion.place(x=15, y=350)

    def pollo_papas():
        ventana_pollo_papas = tk.Toplevel()
        ventana_pollo_papas.title("Pollo al horno con papas")
        ventana_pollo_papas.geometry("670x700+300+0")
        ventana_pollo_papas.resizable(width=False, height=False)

        #   TITULO DE LA RECETA
        titulo = tk.Label(
            ventana_pollo_papas,
            text="""Pollo al horno con papas 🍗""",
            font=("nunito", 20),
        )
        titulo.pack()
        titulo.place(x=195, y=40)

        #   INGREDIENTES
        ingredientes = tk.Label(
            ventana_pollo_papas,
            text="""Ingredientes:

4 muslos de pollo
4 papas, peladas y cortadas en trozos
1 cucharadita de romero seco
3 dientes de ajo picados
3 cucharadas de aceite de oliva
Sal y pimienta al gusto""",
            justify="left",
            font=("nunito", 12),
        )
        ingredientes.pack()
        ingredientes.place(x=15, y=100)

        #   PREPARACIÓN
        preparacion = tk.Label(
            ventana_pollo_papas,
            text="""Preparación:

Precalentar el horno a 200°C.
Mezclar el aceite, romero, ajo, sal y pimienta. Frotar la mezcla 
sobre el pollo y las papas.
Colocar en una fuente para horno y hornear durante 40-50 minutos, 
o hasta que el pollo esté bien cocido y las papas estén tiernas.""",
            justify="left",
            font=("nunito", 12),
        )
        preparacion.pack()
        preparacion.place(x=15, y=350)

    def empanadas_jyq():
        ventana_empanada_jyq = tk.Toplevel()
        ventana_empanada_jyq.title("Empanadas de jamon y queso")
        ventana_empanada_jyq.geometry("670x700+300+0")
        ventana_empanada_jyq.resizable(width=False, height=False)

        #   TITULO DE LA RECETA
        titulo = tk.Label(
            ventana_empanada_jyq,
            text="""Empanadas de jamon y queso 🥟""",
            font=("nunito", 20),
        )
        titulo.pack()
        titulo.place(x=150, y=40)

        #   INGREDIENTES
        ingredientes = tk.Label(
            ventana_empanada_jyq,
            text="""Ingredientes:

Masa para empanadas
200 g de jamón cocido picado
200 g de queso mozzarella rallado
1 huevo (para pincelar)""",
            justify="left",
            font=("nunito", 12),
        )
        ingredientes.pack()
        ingredientes.place(x=15, y=100)

        #   PREPARACIÓN
        preparacion = tk.Label(
            ventana_empanada_jyq,
            text="""Preparación:

Colocar una cucharada de jamón y queso en cada disco de masa para 
empanadas. Cerrar y sellar los bordes.
Pincelar con huevo batido y hornear a 200°C durante 15-20 minutos o 
hasta que estén doradas.""",
            justify="left",
            font=("nunito", 12),
        )
        preparacion.pack()
        preparacion.place(x=15, y=350)

    def tarta_espinaca():
        ventana_tarta_espinaca = tk.Toplevel()
        ventana_tarta_espinaca.title("Tarta de espinaca y queso")
        ventana_tarta_espinaca.geometry("670x700+300+0")
        ventana_tarta_espinaca.resizable(width=False, height=False)

        #   TITULO DE LA RECETA
        titulo = tk.Label(
            ventana_tarta_espinaca,
            text="""Tarta de espinaca y queso 🥧""",
            font=("nunito", 20),
        )
        titulo.pack()
        titulo.place(x=150, y=40)

        #   INGREDIENTES
        ingredientes = tk.Label(
            ventana_tarta_espinaca,
            text="""Ingredientes:

Masa para tarta
300 g de espinacas frescas
200 g de queso ricota
100 g de queso parmesano rallado
2 huevos
Sal y pimienta al gusto
Aceite de oliva""",
            justify="left",
            font=("nunito", 12),
        )
        ingredientes.pack()
        ingredientes.place(x=15, y=100)

        #   PREPARACIÓN
        preparacion = tk.Label(
            ventana_tarta_espinaca,
            text="""Preparación:

Precalentar el horno a 180°C.
Sofreír las espinacas en un poco de aceite hasta que se reduzcan. 
Escurrir el exceso de agua.
Mezclar las espinacas con el queso ricota, parmesano, huevos, 
sal y pimienta.
Extender la masa en una fuente para tarta, rellenar con la mezcla 
de espinacas y hornear durante 30-35 minutos.""",
            justify="left",
            font=("nunito", 12),
        )
        preparacion.pack()
        preparacion.place(x=15, y=350)

    def guiso_res():
        ventana_guiso_res = tk.Toplevel()
        ventana_guiso_res.title("Guiso de res con papas")
        ventana_guiso_res.geometry("670x700+300+0")
        ventana_guiso_res.resizable(width=False, height=False)

        #   TITULO DE LA RECETA
        titulo = tk.Label(
            ventana_guiso_res, text="""Guiso de res con papas 🍵""", font=("nunito", 20)
        )
        titulo.pack()
        titulo.place(x=195, y=40)

        #   INGREDIENTES
        ingredientes = tk.Label(
            ventana_guiso_res,
            text="""Ingredientes:

500 g de carne de res en cubos
2 papas, peladas y cortadas en cubos
1 cebolla picada
1 zanahoria picada
2 dientes de ajo picados
1 litro de caldo de carne
1 cucharadita de comino
Sal y pimienta al gusto
Aceite para cocinar""",
            justify="left",
            font=("nunito", 12),
        )
        ingredientes.pack()
        ingredientes.place(x=15, y=100)

        #   PREPARACIÓN
        preparacion = tk.Label(
            ventana_guiso_res,
            text="""Preparación:

Sofreír la cebolla, zanahoria y ajo en aceite hasta que estén 
tiernos. Añadir la carne y dorar.
Incorporar las papas, caldo, comino, sal y pimienta. 
Cocinar a fuego lento durante 1 hora, o hasta que la carne y 
las papas estén tiernas.""",
            justify="left",
            font=("nunito", 12),
        )
        preparacion.pack()
        preparacion.place(x=15, y=350)

    def quiche_jyq():
        ventana_quiche_jyq = tk.Toplevel()
        ventana_quiche_jyq.title("Quiche de jamon y queso")
        ventana_quiche_jyq.geometry("670x700+300+0")
        ventana_quiche_jyq.resizable(width=False, height=False)


        #   TITULO DE LA RECETA
        titulo = tk.Label(
            ventana_quiche_jyq,
            text="""Quiche de jamon y queso 🥧""",
            font=("nunito", 20),
        )
        titulo.pack()
        titulo.place(x=195, y=40)

        #   INGREDIENTES
        ingredientes = tk.Label(
            ventana_quiche_jyq,
            text="""Ingredientes:

Masa para quiche
200 g de jamón picado
200 g de queso cheddar rallado
3 huevos
200 ml de crema de leche
Sal y pimienta al gusto""",
            justify="left",
            font=("nunito", 12),
        )
        ingredientes.pack()
        ingredientes.place(x=15, y=100)

        #   PREPARACIÓN
        preparacion = tk.Label(
            ventana_quiche_jyq,
            text="""Preparación:

Precalentar el horno a 180°C.
Mezclar los huevos con la crema, sal y pimienta. Agregar el 
jamón y queso.
Extender la masa en una fuente para quiche, verter la 
mezcla y hornear durante 35-40 minutos.
""",
            justify="left",
            font=("nunito", 12),
        )
        preparacion.pack()
        preparacion.place(x=15, y=350)

    def fideos_tuco():
        ventana_fideos_tuco = tk.Toplevel()
        ventana_fideos_tuco.title("Fideos con tuco")
        ventana_fideos_tuco.geometry("670x700+300+0")
        ventana_fideos_tuco.resizable(width=False, height=False)


        #   TITULO DE LA RECETA
        titulo = tk.Label(
            ventana_fideos_tuco, text="""Fideos con tuco 🍝""", font=("nunito", 20)
        )
        titulo.pack()
        titulo.place(x=195, y=40)

        #   INGREDIENTES
        ingredientes = tk.Label(
            ventana_fideos_tuco,
            text="""Ingredientes:

250 g de fideos (espaguetis, penne, etc.)
500 g de carne picada (res o cerdo)
1 cebolla picada
2 dientes de ajo picados
1 zanahoria picada
1 pimiento verde picado
400 g de salsa de tomate
1 taza de caldo de carne (o agua)
1 cucharadita de orégano
Sal y pimienta al gusto
Aceite de oliva
Queso rallado para servir""",
            justify="left",
            font=("nunito", 12),
        )
        ingredientes.pack()
        ingredientes.place(x=15, y=100)

        #   PREPARACIÓN
        preparacion = tk.Label(
            ventana_fideos_tuco,
            text="""Preparación:

Cocinar los fideos según las instrucciones del paquete.
En una sartén grande, calentar aceite de oliva y sofreír la 
cebolla, el ajo, la zanahoria y el pimiento hasta que 
estén tiernos.
Añadir la carne picada y cocinar hasta dorar.
Incorporar la salsa de tomate, el caldo, el orégano, la sal 
y la pimienta. Cocinar a fuego lento durante 20-30 minutos, 
hasta que la salsa espese.
Mezclar con los fideos cocidos y servir con queso rallado.""",
            justify="left",
            font=("nunito", 12),
        )
        preparacion.pack()
        preparacion.place(x=15, y=430)

#----------------------------------------------------- Botones de recetas saladas----------------------------------------------------------------

    STYLES_salado = {
    "font": ("Roboto Condensed", 12),
    "width": 20,
    "height": 3,
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
    boton_receta_uno.pack()  # para que se vea
    # para que aparezca dentro de la ventana
    boton_receta_uno.place(x=55, y=205)

    # Boton 2: Empanadas de carne
    boton_receta_dos = tk.Button(
        ventana_saludo,
        text="""Empanadas de 
    carne""",
        command=empanadas_carne,
        **STYLES_salado
    )
    boton_receta_dos.pack()  # para que se vea
    # para que aparezca dentro de la ventana
    boton_receta_dos.place(x=260, y=205)

    # Boton 3: Milanesas de poll
    boton_receta_tres = tk.Button(
        ventana_saludo,
        text="""Milanesas de 
    pollo""",
        command=milanesa_pollo,
        **STYLES_salado 
    )
    boton_receta_tres.pack()  # para que se vea
    # para que aparezca dentro de la ventana
    boton_receta_tres.place(x=460, y=205)

    # Boton 4: Asado con ensalada criolla
    boton_receta_cuatro = tk.Button(
        ventana_saludo,
        text="""Asado con 
    ensalada criolla""",
        command=asado_ensalada,
        **STYLES_salado
    )
    boton_receta_cuatro.pack()  # para que se vea
    # para que aparezca dentro de la ventana
    boton_receta_cuatro.place(x=55, y=305)

    # Boton 5: Lentejas guisadas
    boton_receta_cinco = tk.Button(
        ventana_saludo,
        text="Lentejas guisadas",
        command=lentejas_guisadas,
        **STYLES_salado
    )
    boton_receta_cinco.pack()  # para que se vea
    # para que aparezca dentro de la ventana
    boton_receta_cinco.place(x=260, y=305)

    # Boton 6: Pastas con salsa bolognesa
    boton_receta_seis = tk.Button(
        ventana_saludo,
        text="""Pastas con 
    salsa bolognesa""",
        command=pastas_bolognesa,
        **STYLES_salado
    )
    boton_receta_seis.pack()  # para que se vea
    # para que aparezca dentro de la ventana
    boton_receta_seis.place(x=460, y=305)

    # Boton 7: Pollo al horno con papas
    boton_receta_siete = tk.Button(
        ventana_saludo,
        text="""Pollo al horno 
    con papas""",
        command=pollo_papas,
        **STYLES_salado
    )
    boton_receta_siete.pack()  # para que se vea
    # para que aparezca dentro de la ventana
    boton_receta_siete.place(x=55, y=405)

    # Boton 8: Empanadas de jamon y queso
    boton_receta_ocho = tk.Button(
        ventana_saludo,
        text="""Empanadas de 
    jamon y queso""",
        command=empanadas_jyq,
        **STYLES_salado
    )
    boton_receta_ocho.pack()  # para que se vea
    # para que aparezca dentro de la ventana
    boton_receta_ocho.place(x=260, y=405)

    # Boton 9: Tarta de espinaca y queso
    boton_receta_nueve = tk.Button(
        ventana_saludo,
        text="""Tarta espinaca 
    y queso""",
        command=tarta_espinaca,
        **STYLES_salado
    )
    boton_receta_nueve.pack()  # para que se vea
    # para que aparezca dentro de la ventana
    boton_receta_nueve.place(x=465, y=410)

    # Boton 10: Guiso de res con papas
    boton_receta_diez = tk.Button(
        ventana_saludo,
        text="""Guiso de res 
    con papas""",
        command=guiso_res,
        **STYLES_salado
    )
    boton_receta_diez.pack()  # para que se vea
    # para que aparezca dentro de la ventana
    boton_receta_diez.place(x=55, y=508)

    # Boton 11: Quiche de jamon y queso
    boton_receta_once = tk.Button(
        ventana_saludo,
        text="""Quiche de 
    jamon y queso""",
        command=quiche_jyq,
        **STYLES_salado
    )
    boton_receta_once.pack()  # para que se vea
    # para que aparezca dentro de la ventana
    boton_receta_once.place(x=260, y=510)

    # Boton 12: Fideos con tuco
    boton_receta_doce = tk.Button(
        ventana_saludo,
        text="Fideos con tuco",
        command=fideos_tuco,
        **STYLES_salado
    )
    boton_receta_doce.pack()  # para que se vea
    # para que aparezca dentro de la ventana
    boton_receta_doce.place(x=460, y=510)


    # ---------------------------------------------------------RECETAS DULCES (Ile) -----------------------------------------------------------------------------

# abre ventana de DULCE
def abrir_ventana_dulce():
    ventana_saludo = tk.Toplevel()
    ventana_saludo.title("Ventana de Dulce")
    ventana_saludo.geometry("670x700+300+0")
    ventana_saludo.resizable(width=False, height=False)

# Cargar la imagen de fondo
    try:
        imagen_fondo = Image.open("./Miniproyecto/UNIFICADO/IMAGENES/FONDO4.png")
        imagen_fondo = imagen_fondo.resize((670, 700), Image.Resampling.LANCZOS)
        fondo_ventana_saludo = ImageTk.PhotoImage(imagen_fondo)
        
        # Crear un label para la imagen de fondo y agregarlo a la ventana
        label_fondo = tk.Label(ventana_saludo, image=fondo_ventana_saludo)
        label_fondo.place(relwidth=1, relheight=1)
        
        # Mantener una referencia a la imagen
        ventana_saludo.fondo_ventana_saludo = fondo_ventana_saludo
    except Exception as e:
        print(f"Error al cargar la imagen: {e}")
        # Si hay un error, continúa sin la imagen de fondo

    # ------------------------------------------------------FUNCIONES RECETAS DULCES -------------------------------------------------------------------------

    def cremaDeLimon():
        cremaDeLimon = tk.Toplevel()
        cremaDeLimon.title("Crema de Limón🍋")
        cremaDeLimon.geometry("670x700+300+0")
        cremaDeLimon.focus()
        cremaDeLimon.grab_set()
        cremaDeLimon.config(cursor="heart")
        cremaDeLimon.resizable(width=False, height=False)

        nombreReceta = tk.Label(
            cremaDeLimon, text='"Crema de Limón🍋' "", font=("candara", 20)
        )
        nombreReceta.pack()
        nombreReceta.place(x=195, y=40)

        ingredientes = tk.Label(
            cremaDeLimon,
            text="""Ingredientes:

 1)  50 gramos de mantequilla sin sal
 2)  100 gramos de azucar glass
 3)  2 limones """,
            justify="left",
            font=("candara", 12),
        )
        ingredientes.pack()
        ingredientes.place(x=15, y=100)

        preparación = tk.Label(
            cremaDeLimon,
            text="""Preparación:

 1) En un bowl, mezclar la mantequilla blanda con el azucar glass tamizada.
    El resultado debe ser una crema blanda de consistencia homogénea.                          
 2) Agregar el zumo de limon y mezclar de nuevo.
    Comprueba la acidez, y si es necesario agrega mas zumo.
    Dejar enfriar y disfrutar!! """,
            justify="left",
            font=("candara", 12),
        )
        preparación.pack()
        preparación.place(x=15, y=250)
        boton_cerrar = tk.Button(
            cremaDeLimon, text="Cerrar ventana", bg="pink", command=cremaDeLimon.destroy
        )
        boton_cerrar.place(x=450, y=550)

    def VasitoOreo():
        VasitoOreo = tk.Toplevel()
        VasitoOreo.title("Vasito Oreo🍪")
        VasitoOreo.geometry("670x700+300+0")
        VasitoOreo.focus()
        VasitoOreo.grab_set()
        VasitoOreo.config(cursor="heart")
        VasitoOreo.resizable(width=False, height=False)

        nombreReceta = tk.Label(
            VasitoOreo, text='"Vasito Oreo🍪' "", font=("candara", 20)
        )
        nombreReceta.pack()
        nombreReceta.place(x=195, y=40)
        #   INGREDIENTES
        ingredientes = tk.Label(
            VasitoOreo,
            text="""Ingredientes:

1)	Restos de bizcochuelo, magdalena o vainillas
2)	250 g de leche condensada
3)	1 yogur
4)	1 cda. de azúcar negra
5)	1 trozo de chocolate negro
 """,
            justify="left",
            font=("candara", 12),
        )
        ingredientes.pack()
        ingredientes.place(x=15, y=100)

        #   PREPARACIÓN
        preparación = tk.Label(
            VasitoOreo,
            text="""Preparación:

1)  Desmenuza el bizcochuelo y colócalo como base en los vasitos.
2)	Espolvorea azúcar negra para darle un toque terroso.
3)	Bate el yogur y pon una cucharada en cada vasito.
4)	Alterna cucharadas de leche condensada y yogur hasta llenar los vasitos.
5)	Ralla el chocolate encima y listo! """,
            justify="left",
            font=("candara", 12),
        )
        preparación.pack()
        preparación.place(x=15, y=250)
        boton_cerrar = tk.Button(
            VasitoOreo, text="Cerrar ventana", bg="pink", command=VasitoOreo.destroy
        )
        boton_cerrar.place(x=450, y=550)

    def Crepes():
        Crepes = tk.Toplevel()
        Crepes.title("Crepes")
        Crepes.geometry("670x700+300+0")
        Crepes.focus()
        Crepes.grab_set()
        Crepes.config(cursor="heart")
        Crepes.resizable(width=False, height=False)

        nombreReceta = tk.Label(Crepes, text='"Crepes 🫓"', font=("candara", 20))
        nombreReceta.pack()
        nombreReceta.place(x=150, y=20)
        #   INGREDIENTES
        ingredientes = tk.Label(
            Crepes,
            text="""Ingredientes:
                                
    1)  2 huevos
    2)  150 g de harina
    3)  1 cucharadita de azúcar (opcional)
    4)  1 pizca de sal
    5)  250 ml de leche
    7)  aceite para engrasar la sartén de bizcochuelo, magdalena o vainillas
    """,
            justify="left",
            font=("candara", 12),
        )
        ingredientes.pack()
        ingredientes.place(x=15, y=80)

        #   PREPARACIÓN
        preparación = tk.Label(
            Crepes,
            text="""Preparación:
                            
    1) En un bol ponemos los huevos, la pizca de sal, el azúcar, la harina y mezclamos bien.
    2) Vamos incorporando la leche poco a poco batiendo siempre con unas varillas manuales o 
    con la batidora eléctrica, hasta obtener un líquido denso.
    Si nos han quedado grumos pasamos por un colador.
    La consistencia tiene que ser líquida, pero con una cierta densidad: 
    ni tan líquida como el agua ni tan densa como una crema. 
    3) Dejamos reposar la mezcla en heladera 1 hora.
    4) Calentamos una crepera o una sartén antiadherente. 
    La engrasamos con apenas un chorrito de aceite que vamos a distribuir bien con papel 
    absorbente.
    Cuando la sartén esté caliente, con un cucharón vertemos la mezcla en el centro, 
    e inmediatamente lo movemos inclinándolo de un lado a otro para que la mezcla 
    se distribuya bien.
    Tiene que ser un movimiento rápido para que los crepes nos queden finos y de un 
    grosor homogéneo. 
    La cantidad de masa depende del tamaño de la sartén.
    Acompañalos con Dulce de Leche o Miel! y A Disfrutar!""",
            justify="left",
            font=("candara", 12),
        )
        preparación.pack()
        preparación.place(x=15, y=250)
        boton_cerrar = tk.Button(
            Crepes, text="Cerrar ventana", bg="pink", command=Crepes.destroy
        )
        boton_cerrar.place(x=550, y=600)

    def galletasDeAvena():
        galletasDeAvena = tk.Toplevel()
        galletasDeAvena.title("Galletas de Avena🍪")
        galletasDeAvena.geometry("670x700+300+0")
        galletasDeAvena.focus()
        galletasDeAvena.grab_set()
        galletasDeAvena.config(cursor="heart")
        galletasDeAvena.resizable(width=False, height=False)

        nombreReceta = tk.Label(
            galletasDeAvena, text='"Galletas de Avena🍪' "", font=("candara", 20)
        )
        nombreReceta.pack()
        nombreReceta.place(x=195, y=40)
        #   INGREDIENTES
        ingredientes = tk.Label(
            galletasDeAvena,
            text="""Ingredientes:

1)	2 plátanos maduros
2)	50 gramos pasas de uva
3)	150 gramos de copos de avena
4)	50 gramos de chips de chocolate negro

 """,
            justify="left",
            font=("candara", 12),
        )
        ingredientes.pack()
        ingredientes.place(x=15, y=100)

        #   PREPARACIÓN
        preparación = tk.Label(
            galletasDeAvena,
            text="""Preparación:

1)  Pela los plátanos, pártelos en trozos pequeños y pisalos con un tenedor.
2)  Corta las pasas de uva, añádelas a los plátanos pisados y mezcla.
3)  Agrega los copos de avena y mezcla bien.
    Para esta receta de galletas de avena en microondas usaremos los copos enteros, 
    ya que así la textura será más crujiente.
4)  Incorpora los chips de chocolate negro y repártelos bien por la masa.
5)  Toma pequeñas porciones de masa y dale forma redondeada con las manos.
    Ve poniendo las galletas en un plato apto para el microondas, 
    pero pon pocas a la vez para que se cocinen de manera uniforme.
6)  Cocina las galletas de avena en microondas a potencia máxima durante 30 segundos. 
    Con este tiempo debería ser suficiente, pero como cada microondas es distinto,
    recomendamos revisar su cocción y valorar si necesitan unos segundos más.
    Conforme se vayan haciendo, deja que se enfríen sobre una rejilla.
    Una vez frías, ¡ya podrás comerlas!
 """,
            justify="left",
            font=("candara", 12),
        )
        preparación.pack()
        preparación.place(x=15, y=250)
        boton_cerrar = tk.Button(
            galletasDeAvena,
            text="Cerrar ventana",
            bg="pink",
            command=galletasDeAvena.destroy,
        )
        boton_cerrar.place(x=450, y=550)

    def budinDePan():
        budinDePan = tk.Toplevel()
        budinDePan.title("Budín de Pan🍮")
        budinDePan.geometry("670x700+300+0")
        budinDePan.focus()
        budinDePan.grab_set()
        budinDePan.config(cursor="heart")
        budinDePan.resizable(width=False, height=False)

        nombreReceta = tk.Label(
            budinDePan, text='"Budín de Pan🍮' "", font=("candara", 20)
        )
        nombreReceta.pack()
        nombreReceta.place(x=195, y=40)
        #   INGREDIENTES
        ingredientes = tk.Label(
            budinDePan,
            text="""Ingredientes:
1)  3 huevos
2)  500 mililitros de leche
3)  1 cucharadita de esencia de vainilla
4)  150 gramos de pan de barra o pan de molde
5)  150 gramos de azúcar (¾ taza)
6)  1 limón (ralladura)
7)  200 gramos de azúcar (1 taza)
 """,
            justify="left",
            font=("candara", 12),
        )
        ingredientes.pack()
        ingredientes.place(x=15, y=100)

        #   PREPARACIÓN
        preparación = tk.Label(
            budinDePan,
            text="""Preparación:

1) Coloca la leche, la ralladura del limón, la esencia de vainilla y el azúcar
   en un recipiente y mézclalo bien.
2) Agrega el pan desmenuzado, remueve y deja que se empape bien.
3) Prepara el caramelo líquido colocando un poco de azúcar en una olla y cocínalo a fuego
   bajo-medio hasta que empiece a derretirse. Añade poco a poco más azúcar hasta acabar
   con todo para que se vaya derritiendo de forma homogénea y no queden grumos.
4) Bate los huevos enteros en otro recipiente y cuando estén listos agrégalos a la mezcla
   de leche y pan. Mézclalo todo con un tenedor hasta que el pan empiece a desmenuzarse 
   ligeramente o, si prefieres que no te queden grumos, con una batidora eléctrica. 
5) Con el caramelo aún líquido y caliente, cubre el molde por toda la base y las paredes
   de forma uniforme.
6) Una vez que se haya secado completamente el caramelo líquido, vierte la mezcla reposada
   y tápalo con film.
7) Lleva el budin de pan al microondas y cocínalo durante 7 minutos a la mitad de la potencia 
   Después, cocina otros 9 minutos a máxima potencia.
   Una vez bien cocido, retíralo y déjalo enfriar como mínimo 1 hora antes de servirlo. 
 """,
            justify="left",
            font=("candara", 12),
        )
        preparación.pack()
        preparación.place(x=15, y=260)
        boton_cerrar = tk.Button(
            budinDePan, text="Cerrar ventana", bg="pink", command=budinDePan.destroy
        )
        boton_cerrar.place(x=500, y=630)

    def flan():
        flan = tk.Toplevel()
        flan.title("Flan🍮")
        flan.geometry("670x700+300+0")
        flan.focus()
        flan.grab_set()
        flan.config(cursor="heart")
        flan.resizable(width=False, height=False)


        nombreReceta = tk.Label(flan, text='"Flan🍮' "", font=("candara", 20))
        nombreReceta.pack()
        nombreReceta.place(x=195, y=40)
        #   INGREDIENTES
        ingredientes = tk.Label(
            flan,
            text="""Ingredientes:

1)  300 mililitros de Leche (1¼ tazas)
2)	5 Huevos
3)  135 gramos de Azúcar blanco
4)  1 pizca de Esencia de vainilla
5)  100 gramos de Azúcar blanco para el caramelo

 """,
            justify="left",
            font=("candara", 12),
        )
        ingredientes.pack()
        ingredientes.place(x=15, y=100)

        #   PREPARACIÓN
        preparación = tk.Label(
            flan,
            text="""Preparación:

1) Caramelo: colocamos los 100 gramos de azúcar en una sartén. 
   Cuando observemos que comienza a derretirse, movemos con una espátula hasta que 
   se convierta en caramelo líquido.
2) Distribuimos el caramelo en moldes individuales, y reservamos.
3) En un bol  batimos los huevos con el azúcar. 
4) Colocamos en una olla, añadimos la leche, la esencia de vainilla y cocinamos 
   hasta que alcance el primer hervor. 
5) Cuando empiece a hervir la mezcla, la retiramos del fuego y la vertemos en los moldes
   que reservamos con el caramelo. 
6) Cocinamos durante 3 minutos a máxima potencia.
   Retiramos y dejamos enfriar. 
   Si observamos que el flan todavía no está listo, lo dejamos un minuto más y 
   volvemos a comprobarlo.¡Listo! 
 """,
            justify="left",
            font=("candara", 12),
        )
        preparación.pack()
        preparación.place(x=15, y=250)
        boton_cerrar = tk.Button(
            flan, text="Cerrar ventana", bg="pink", command=flan.destroy
        )
        boton_cerrar.place(x=450, y=550)

    def tartaDeYogur():
        tartaDeYogur = tk.Toplevel()
        tartaDeYogur.title("Tarta de Yogur🥧")
        tartaDeYogur.geometry("670x700+300+0")
        tartaDeYogur.focus()
        tartaDeYogur.grab_set()
        tartaDeYogur.config(cursor="heart")
        tartaDeYogur.resizable(width=False, height=False)


        nombreReceta = tk.Label(
            tartaDeYogur, text='"Tarta de Yogur🥧' "", font=("candara", 20)
        )
        nombreReceta.pack()
        nombreReceta.place(x=195, y=40)

        ingredientes = tk.Label(
            tartaDeYogur,
            text="""Ingredientes:

1) 	625 g yogur griego sin azúcar
2)	4 huevos 
3)	50 g edulcorante
4)	Unas gotitas de esencia de vainilla
 """,
            justify="left",
            font=("candara", 12),
        )
        ingredientes.pack()
        ingredientes.place(x=15, y=100)

        preparación = tk.Label(
            tartaDeYogur,
            text="""Preparación:

1)	Batimos todos los ingredientes en un bol.
2)	Vertemos la mezcla en un molde desmontable y forrado o engrasado.
3)	Con el horno previamente precalentado a 170ºC, horneamos durante unos 70-90min, 
    hasta que se doren los bordes.
4)	Dejamos reposar y enfriamos por completo en la heladera.
5)	Opcionalmente, podemos decorar con un poco de mermelada sin azúcar. 
                    ¡Y lista!
 """,
            justify="left",
            font=("candara", 12),
        )
        preparación.pack()
        preparación.place(x=15, y=250)
        boton_cerrar = tk.Button(
            tartaDeYogur, text="Cerrar ventana", bg="pink", command=tartaDeYogur.destroy
        )
        boton_cerrar.place(x=450, y=550)

    def tartaDeNaranja():
        tartaDeNaranja = tk.Toplevel()
        tartaDeNaranja.title("Tarta de Naranja🍊")
        tartaDeNaranja.geometry("670x700+300+0")
        tartaDeNaranja.focus()
        tartaDeNaranja.grab_set()
        tartaDeNaranja.config(cursor="heart")
        tartaDeNaranja.resizable(width=False, height=False)


        nombreReceta = tk.Label(
            tartaDeNaranja, text='"Tarta de Naranja🍊' "", font=("candara", 20)
        )
        nombreReceta.pack()
        nombreReceta.place(x=195, y=40)

        ingredientes = tk.Label(
            tartaDeNaranja,
            text="""Ingredientes:

1)  200 ml leche evaporada
2)	200 ml nata líquida para montar (crema de leche)
3)  100 ml zumo de naranja
4)	3 láminas gelatina neutra (o 7,5g de gelatina en polvo)
5)	Edulcorante al gusto (yo 60g eritritol)
6)	La ralladura de una naranja
""",
            justify="left",
            font=("candara", 12),
        )
        ingredientes.pack()
        ingredientes.place(x=15, y=100)

        preparación = tk.Label(
            tartaDeNaranja,
            text="""Preparación:

1) Hidratamos la gelatina en agua fría hasta que esté blandita.
2) En un cazo a fuego medio, ponemos el zumo de naranja. Escurrimos la gelatina 
   y la integramos en el zumo. Añadimos el edulcorante hasta que se integre bien. Reservamos.
3) En un bol, batimos la leche evaporada y la nata bien fría,añadimos la ralladura de 
   naranja y batimos un poco más.
4) Vertemos el zumo de naranja con gelatina, y lo integramos con movimientos envolventes.
5) Ponemos nuestra mezcla en un molde, mejor si es de silicona, y congelamos durante al
   menos 4 horas.
   Desmoldamos, ¡y lista!""",
            justify="left",
            font=("candara", 12),
        )
        preparación.pack()
        preparación.place(x=15, y=270)
        boton_cerrar = tk.Button(
            tartaDeNaranja,
            text="Cerrar ventana",
            bg="pink",
            command=tartaDeNaranja.destroy,
        )
        boton_cerrar.place(x=450, y=550)

    def choco():
        choco = tk.Toplevel()
        choco.title("Postre de Chocolate🍫")
        choco.geometry("670x700+300+0")
        choco.focus()
        choco.grab_set()
        choco.config(cursor="heart")
        choco.resizable(width=False, height=False)


        nombreReceta = tk.Label(
            choco, text='"Postre de Chocolate🍫"', font=("candara", 20)
        )
        nombreReceta.pack()
        nombreReceta.place(x=195, y=40)

        ingredientes = tk.Label(
            choco,
            text="""Ingredientes:

1) 125 ml. yogurt natural sin azúcar
2) 1 sobrecito de sucralosa
3) 1 cda. de semillas de chía
4) 1 cda. de cacao en polvo sin azúcar
5) Galletas de arroz
6) Menta o hierba buena
7) Almendras """,
            justify="left",
            font=("candara", 12),
        )
        ingredientes.pack()
        ingredientes.place(x=15, y=100)

        preparación = tk.Label(
            choco,
            text="""Preparación:
                           
1)  Colocá el yogur natural sin azúcar en un bol.
2)  Vamos a endulzar el yogur con un sobre de sucralosa o stevia 
3)  Agregar una cucharada de semillas de chia y mezclar.
4)  Añadir una cucharada de cacao sin azúcar y mezclar bien con una cuchara 
    hasta que esté totalmente integrado.                    
5)  Cortar las galletas de arroz en trozos pequeños y colocarlas en vasitos.
6)  Encima de las galletas de arroz vamos a agregar nuestro postre de chocolate 
7)  Así como está vamos a llevarlo a la heladera como mínimo media hora. 
8)  Decorado: le añadimos encima unas hojitas de menta o hierba buena. 
    Después unos trocitos de galletita.
    Por ultimo algunas almendras, que rico!""",
            justify="left",
            font=("candara", 12),
        )
        preparación.pack()
        preparación.place(x=15, y=290)
        boton_cerrar = tk.Button(
            choco, text="Cerrar ventana", bg="pink", command=choco.destroy
        )
        boton_cerrar.place(x=450, y=550)

    def arrozCLeche():
        arrozCLeche = tk.Toplevel()
        arrozCLeche.title("Arroz con Leche🥣")
        arrozCLeche.geometry("670x700+300+0")
        arrozCLeche.focus()
        arrozCLeche.grab_set()
        arrozCLeche.config(cursor="heart")
        arrozCLeche.resizable(width=False, height=False)


        nombreReceta = tk.Label(
            arrozCLeche, text='"Arroz con Leche🥣' "", font=("candara", 20)
        )
        nombreReceta.pack()
        nombreReceta.place(x=195, y=40)

        ingredientes = tk.Label(
            arrozCLeche,
            text="""Ingredientes:

1) 100g. de arroz (preferentemente para risotto)
2) 1 litro de leche
3) 150g. de azúcar
4) canela (en rama y en polvo)
5) cáscara de limón
 """,
            justify="left",
            font=("candara", 12),
        )
        ingredientes.pack()
        ingredientes.place(x=15, y=100)

        preparación = tk.Label(
            arrozCLeche,
            text="""Preparación:

1)	Ponemos en una olla el arroz junto con el litro de leche.
2)  Luego vamos a cortar unos pedazos de cáscara de limón y los vamos a agregar a la olla.
3)  Agregar una ramita de canela. 
4)  Esta mezcla, antes de ponerla al fuego, la vamos a dejar reposar entre 30 y 60 minutos.
5)  Ponemos la mezcla a fuego bajo y lo vamos a tapar hasta que esté cerquita de hervir.
6)  Una vez que esté cerca del hervor, destapamos y comenzamos a revolver cuidadosamente.
7)  El momento de agregar el azúcar, es cuando prueben el arroz y sientan que está al dente.
    Hay que seguir revolviendo el arroz con leche hasta que la misma comienza a evaporarse y 
    el azúcar comienza a generar que la mezcla se ponga más espesa.
8)  Cuando veamos que el arroz con leche esté cocido, apagamos el fuego, sacamos los pedazos
    de canela y de cáscara de limón, y lo dejamos reposar unos minutos en la olla mientras
    lo batimos un poco más intensamente para que se termine de evaporar el líquido que queda.
9)  Reposo en heladera por 20 o 30 minutos y listo!  
    
 """,
            justify="left",
            font=("candara", 12),
        )
        preparación.pack()
        preparación.place(x=15, y=250)
        boton_cerrar = tk.Button(
            arrozCLeche, text="Cerrar ventana", bg="pink", command=arrozCLeche.destroy
        )
        boton_cerrar.place(x=450, y=550)

    def gelatina():
        gelatina = tk.Toplevel()
        gelatina.title("Gelatina de Fresa🍓")
        gelatina.geometry("670x700+300+0")
        gelatina.focus()
        gelatina.grab_set()
        gelatina.config(cursor="heart")
        gelatina.resizable(width=False, height=False)


        nombreReceta = tk.Label(
            gelatina, text='"Gelatina de Fresa🍓' "", font=("candara", 20)
        )
        nombreReceta.pack()
        nombreReceta.place(x=195, y=40)

        ingredientes = tk.Label(
            gelatina,
            text="""Ingredientes:

1) 	3 sobres de gelatina sabor fresa de 120 gramos cada uno 
2)  1 lata de media crema de 225 gramos 
3)  1.5 litros de agua mas aparte otros 750 mililitros 
 """,
            justify="left",
            font=("candara", 12),
        )
        ingredientes.pack()
        ingredientes.place(x=15, y=100)

        preparación = tk.Label(
            gelatina,
            text="""Preparación:

1) Vierte en un recipiente amplio de por lo menos 2 litros de capacidad el polvo de 2 sobres
   de gelatina y agrega 1.5 litros de agua muy caliente, revuelve hasta disolver y deja enfriar 
2) Cuando el liquido de la gelatina este frío lleva el recipiente al refrigerador por
   tres horas aproximadamente.  
3) Vierte el tercer sobre de gelatina en un recipiente y añade 750 mililitros de agua 
   muy caliente, revuelve hasta disolver por completo y deja enfriar.
4) Cuando el liquido de la gelatina este frío agrega la media crema y revuelve hasta mezclar
   muy bien, lo puedes hacer mezclando a mano con un batidor o en la licuadora.
5) Cuando la primer gelatina este con una consistencia firme corta en cubos pequeños y 
   coloca cubos de gelatina hasta tres cuartas partes de capacidad, en recipientes individuales
6) Agrega en cada vaso la mezcla que preparamos con el tercer sobre de gelatina y la media crema 
   hasta llenar cada recipiente donde previamente colocaste los cubos de gelatina 
7) Lleva al refrigerador y cuando las gelatinas de mosaico tengan una consistencia firme
   estarán listas!

 """,
            justify="left",
            font=("candara", 12),
        )
        preparación.pack()
        preparación.place(x=15, y=250)
        boton_cerrar = tk.Button(
            gelatina, text="Cerrar ventana", bg="pink", command=gelatina.destroy
        )
        boton_cerrar.place(x=450, y=550)

    def brownie():
        brownie = tk.Toplevel()
        brownie.title("Brownie 🍫")
        brownie.geometry("670x700+300+0")
        brownie.focus()
        brownie.grab_set()
        brownie.config(cursor="heart")
        brownie.resizable(width=False, height=False)


        nombreReceta = tk.Label(brownie, text='"Brownie 🍫' "", font=("candara", 20))
        nombreReceta.pack()
        nombreReceta.place(x=195, y=40)

        ingredientes = tk.Label(
            brownie,
            text="""Ingredientes:

1) 3 huevos
2) 1 taza azúcar
3) 1/2 taza aceite
4) 1 taza cacao
5) 1/2 taza harina 0000
 """,
            justify="left",
            font=("candara", 12),
        )
        ingredientes.pack()
        ingredientes.place(x=15, y=100)

        preparación = tk.Label(
            brownie,
            text="""Preparación:

1)  En un bol batir los tres huevos con el azúcar hasta espumar.
2)  Agregar el aceite y batir.
3)  Integrar la taza de cacao a la mezcla anterior.
4)  Agregar la media taza de harina mientras batimos.
5)  Llevar a horno precalentando por unos 30/40 minutos en un molde previamente
    enmantecado. Y Listo!
 """,
            justify="left",
            font=("candara", 12),
        )
        preparación.pack()
        preparación.place(x=15, y=250)
        boton_cerrar = tk.Button(
            brownie, text="Cerrar ventana", bg="pink", command=brownie.destroy
        )
        boton_cerrar.place(x=450, y=550)


#----------------------------------------------------- Botones de recetas dulces----------------------------------------------------------------

    STYLES = {
    "font": ("Roboto Condensed", 12),
    "width": 20,
    "height": 3,
    "fg": "white",
    "bg": "#863808",
    "borderwidth": 0,
    "relief": "flat",
    "activebackground": "#863808",
    "activeforeground": "gold"
}

# Boton 1: 'Crema de Limón 🍋
    boton_receta_uno = tk.Button(ventana_saludo, 
                                text=''''Crema de Limón 🍋''',
                                command=cremaDeLimon,
                                **STYLES)
    boton_receta_uno.pack()  # para que se vea
# para que aparezca dentro de la ventana
    boton_receta_uno.place(x=55, y=205)


# Boton 2: Vasito Oreo 🍪
    boton_receta_dos = tk.Button(ventana_saludo, 
                                text='''Vasito Oreo 🍪''', 
                                command=VasitoOreo,
                                **STYLES)
    boton_receta_dos.pack()  # para que se vea
# para que aparezca dentro de la ventana
    boton_receta_dos.place(x=258, y=205)


# Boton 3: Crepes 🫓
    boton_receta_tres = tk.Button(ventana_saludo, 
                            text='''Crepes 🫓''',
                            command=Crepes,
                            **STYLES)
    boton_receta_tres.pack()  # para que se vea
# para que aparezca dentro de la ventana
    boton_receta_tres.place(x=460, y=205)


# Boton 4: Galletas de Avena🍪
    boton_receta_cuatro = tk.Button(ventana_saludo, 
                                text='''Galletas de Avena🍪''', 
                                command=galletasDeAvena,
                                **STYLES)
    boton_receta_cuatro.pack()  # para que se vea
# para que aparezca dentro de la ventana
    boton_receta_cuatro.place(x=55, y=305)

# Boton 5: Budín de Pan🍮
    boton_receta_cinco = tk.Button(ventana_saludo, 
                                text="Budín de Pan🍮", 
                                command=budinDePan,
                                **STYLES)
    boton_receta_cinco.pack()  # para que se vea
# para que aparezca dentro de la ventana
    boton_receta_cinco.place(x=258, y=305)

# Boton 6: Flan🍮
    boton_receta_seis = tk.Button(ventana_saludo, 
                                text='''Flan🍮''', 
                                command=flan,
                                **STYLES)
    boton_receta_seis.pack()  # para que se vea
# para que aparezca dentro de la ventana
    boton_receta_seis.place(x=460, y=305)

# Boton 7: Tarta de yogur al Horno 🥧
    boton_receta_siete = tk.Button(ventana_saludo, 
                                text='''Tarta de yogur al Horno 🥧''', 
                                command=tartaDeYogur,
                                **STYLES)
    boton_receta_siete.pack()  # para que se vea
# para que aparezca dentro de la ventana
    boton_receta_siete.place(x=55, y=406)

# Boton 8: Tarta de Naranja🍊
    boton_receta_ocho = tk.Button(ventana_saludo, 
                                text='''Tarta de Naranja🍊''', 
                                command=tartaDeNaranja,
                                **STYLES)
    boton_receta_ocho.pack()  # para que se vea
# para que aparezca dentro de la ventana
    boton_receta_ocho.place(x=258, y=405)

# Boton 9: Postrecito de Chocolate🍫
    boton_receta_nueve = tk.Button(ventana_saludo, 
                                text='''Postrecito de Chocolate🍫''', 
                                command=choco,
                                **STYLES)
    boton_receta_nueve.pack()  # para que se vea
# para que aparezca dentro de la ventana
    boton_receta_nueve.place(x=460, y=405)

# Boton 10: Arroz con Leche 🥣
    boton_receta_diez = tk.Button(ventana_saludo, 
                                text='''Arroz con Leche 🥣''', 
                                command=arrozCLeche,
                                **STYLES)
    boton_receta_diez.pack()  # para que se vea
# para que aparezca dentro de la ventana
    boton_receta_diez.place(x=55, y=510)

# Boton 11: Gelatina de Frutilla 🍓
    boton_receta_once = tk.Button(ventana_saludo, 
                                text='''Gelatina de Frutilla 🍓''', 
                                command=gelatina,
                                **STYLES)
    boton_receta_once.pack()  # para que se vea
# para que aparezca dentro de la ventana
    boton_receta_once.place(x=258, y=510)

# Boton 12: 'Brownie 🍫'
    boton_receta_doce = tk.Button(ventana_saludo, 
                                text='Brownie 🍫', 
                                command=brownie,
                                **STYLES)
    boton_receta_doce.pack()  # para que se vea
# para que aparezca dentro de la ventana
    boton_receta_doce.place(x=460, y=510)


# abre ventana de MIS RECETAS
def abrir_ventana_mis_rece():
    ventana_saludo = tk.Toplevel()
    ventana_saludo.title("Mis Recetas")
    ventana_saludo.geometry("670x700+300+0")
    ventana_saludo.resizable(width=False, height=False)

    recetas = {}  # las recetas que se agreguen se añaden en este conjunto

    # creamos el frame de la ventana y lo asociamos a ventana_saludo
    frame = tk.Frame(ventana_saludo, bg="#E6E6E6")
    frame.pack(fill=tk.BOTH, expand=True)

    # usamos canvas para modificar de forma más facil el diseño del marco
    canvas = tk.Canvas(frame, bg="#E6E6E6")
    scrollbar = tk.Scrollbar(
        frame, orient="vertical", command=canvas.yview
    )  # el scrollbar
    scrollbar_marco = tk.Frame(canvas, bg="#E6E6E6")

    scrollbar_marco.bind(
        "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollbar_marco, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    title_label = tk.Label(
        scrollbar_marco,
        text="MIS RECETAS",
        padx=200,
        pady=30,
        font=("Roboto Condensed", 30),
        bg="#E6E6E6",
    )  # label mis recetas
    title_label.grid(row=0, column=0, columnspan=3, pady=10)

    def añadir_receta():
        nombre_receta = simpledialog.askstring("Nueva Receta", "Nombre de la receta:")
        if nombre_receta:
            recetas[nombre_receta] = ""
            actualizar_recetas()

    añadir_boton = tk.Button(
        scrollbar_marco,
        text="+",
        width=14,
        height=4,
        command=añadir_receta,
        font= ("Roboto Condensed", 12),
        fg= "black",
        bg= "#FFFFFF",
        borderwidth= 2,
        activeforeground= "gold"
    )
    añadir_boton.grid(row=1, column=0, pady=10)

    def actualizar_recetas():  # cuando se crea la receta se actualiza la cantidad ya creadas y se agrega el boton
        for widget in scrollbar_marco.winfo_children():
            if isinstance(widget, tk.Button) and widget != añadir_boton:
                widget.destroy()

        row, column = 1, 0  #coloca en orden los botones
        for recipe in recetas:
            button = tk.Button(
                scrollbar_marco,
                text=recipe,
                width=16,
                height=5,
                command=lambda r=recipe: editar_receta(r),
                bg="#7585F1",
            )
            button.grid(row=row, column=column, padx=5, pady=5)
            column += 1
            if column == 3:
                column = 0
                row += 1

        añadir_boton.grid(row=row, column=column, padx=5, pady=10)

# esta funcion permite al entrar a la receta creada, poder editarla como si fuera un bloc de notas
    def editar_receta(nombre_receta):
        editar_ventana = tk.Toplevel(ventana_saludo)
        editar_ventana.title(nombre_receta)
        editar_ventana.geometry("670x700+300+0")
        editar_ventana.resizable(False, False)
        editar_ventana.configure(bg="#adaaa8")
        ventana.resizable(width=False, height=False)

        bloc_notas = tk.Text(editar_ventana, bg="#E6E6E6", font=("Arial"))
        bloc_notas.insert(tk.END, recetas[nombre_receta])
        bloc_notas.pack(expand=True, fill=tk.BOTH)

        boton_guardar = tk.Button(
            editar_ventana,
            text="Guardar",
            command=lambda: guardar_receta(
                nombre_receta, bloc_notas.get("1.0", tk.END)
            ),
        )
        boton_guardar.pack(side=tk.LEFT, padx=10, pady=10)

        boton_borrar = tk.Button(
            editar_ventana,
            text="Eliminar",
            command=lambda: eliminar_receta(nombre_receta, editar_ventana),
        )
        boton_borrar.pack(side=tk.RIGHT, padx=10, pady=10)

    def guardar_receta(nombre_receta, contenido):
        recetas[nombre_receta] = contenido
        messagebox.showinfo("Guardar", f"Receta '{nombre_receta}' guardada.")

    def eliminar_receta(nombre_receta, ventana):
        del recetas[nombre_receta]
        ventana.destroy()
        actualizar_recetas()


# Cierra ventana mis recetas
def botonvolver():
    pass


# Función para abrir la ventana de saludo


def abrir_ventana_saludo(nombre):
    # Crear la ventana secundaria
    ventana_saludo = tk.Toplevel()
    ventana_saludo.title("Entrada")
    ventana_saludo.geometry("670x700+300+0")
    nombre_capitalizado = nombre.capitalize()
    ventana_saludo.resizable(width=False, height=False)

    #Cargar la imagen de fondo
    from PIL import Image, ImageTk

    try:
        fondo2 = Image.open("./Miniproyecto/UNIFICADO/IMAGENES/FONDO2.png").resize(
            (670, 700)
        )
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
        font=("Roboto Condensed", 18),
        bg="#2B0E54",
        fg="#FFFFFF",
        wraplength=600,  #Ajustar el wraplength si es necesario
    )
    etiqueta_saludo.place(x=240, y=15)

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
        width=15,
        height=5,
        command=abrir_ventana_salado,
    )
    btn_salado.place(x=58, y=432)
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
        width=15,
        height=5,
        command=abrir_ventana_dulce,
    )
    btn_dulce.place(x=272, y=432)
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
        width=15,
        height=5,
        command=abrir_ventana_mis_rece,
    )
    btn_mis_rece.place(x=483, y=432)


# Función para mostrar el temporizador


def mostrar_temporizador():
    temporizador_ventana = tk.Toplevel()  # Usar Toplevel en lugar de Tk
    temporizador_ventana.title("Temporizador")
    temporizador_ventana.geometry("300x300+300+0")
    temporizador_ventana.config(bg="#D8BFD8")
    temporizador_ventana.resizable(width=False, height=False)

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
    btn_pause = tk.Button(temporizador_ventana, text="Pausar/Reanudar", bd="5", command=pausa)
    btn_reset = tk.Button(temporizador_ventana, text="Reiniciar", bd="5", command=reset)

    btn_start.place(x=90, y=60)
    btn_stop.place(x=90, y=100)
    btn_pause.place(x=90, y=140)
    btn_reset.place(x=90, y=180)

# Función para cerrar una ventana


def cerrar_ventana(ventana):
    ventana.destroy()


# Función para mostrar la ventana "Acerca de"


def mostrar_acerca_de():
    # Crear la ventana "Acerca de"
    ventana_acerca_de = tk.Tk()
    ventana_acerca_de.title("Acerca de")
    ventana_acerca_de.geometry("670x700+300+0")
    ventana_acerca_de.resizable(width=False, height=False)

    # Crear un Frame para el texto con scroll
    frame_texto = tk.Frame(ventana_acerca_de)
    # Posiciona el Frame en el centro
    frame_texto.place(relx=0.5, rely=0.5, anchor="center")

    # Crear un Text con Scrollbar
    scrollbar = Scrollbar(frame_texto)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    texto = Text(
        frame_texto, height=25, width=70, wrap=tk.WORD, yscrollcommand=scrollbar.set
    )
    texto.pack(side=tk.LEFT, fill=tk.BOTH)
    scrollbar.config(command=texto.yview)

    # Agregar un texto de ejemplo
    texto.insert(
        tk.END,
        """Somos COWORKING, una empresa joven y dinámica dedicada al desarrollo web, compuesta por un talentoso equipo de estudiantes del Informatorio, quienes representan las nuevas promesas en la industria de la programación.

Nuestro Equipo:
Pablo Sabadini: Con una pasión por la innovación y el desarrollo front-end, Pablo se asegura de que cada proyecto tenga una interfaz intuitiva y atractiva.

Camila Ledesma Falschini: Experta en diseño UX/UI, Camila transforma ideas en experiencias de usuario fluidas y visualmente impactantes.

Aguirre Eugenio Nicolás: Focalizado en la lógica y el desarrollo back-end, Eugenio asegura que cada solución sea sólida, escalable y eficiente.

Anabela Maciel: Especialista en bases de datos, Anabela se encarga de que la información sea gestionada de manera segura y óptima.

Darío Merentiel: Con un ojo crítico para los detalles, Darío trabaja en el aseguramiento de la calidad, asegurando que cada proyecto cumpla con los más altos estándares.

Ileana Fontana: Amante del código limpio y bien estructurado, Ileana es nuestra desarrolladora full-stack, integrando las mejores prácticas en cada etapa del desarrollo.

Roberto Galeano: Roberto es nuestro ingeniero de software, que combina conocimiento técnico con una visión estratégica para crear soluciones a medida.

Eduina Nicole Dellamea: Experta en gestión de proyectos, Eduina coordina al equipo para asegurar que cada entrega sea oportuna y cumpla con los objetivos del cliente.

Nuestra Misión
En COWORKING, nuestra misión es desarrollar soluciones web que no solo cumplan, sino que superen las expectativas de nuestros clientes. Trabajamos en equipo para combinar nuestras fortalezas y crear productos que son funcionales, estéticamente agradables y de alta calidad.

Nuestros Valores
Innovación: Estamos comprometidos a estar a la vanguardia de la tecnología, adoptando las últimas tendencias y herramientas en desarrollo web.

Colaboración: Creemos que las mejores soluciones nacen de un esfuerzo conjunto, tanto dentro de nuestro equipo como en estrecha colaboración con nuestros clientes.

Calidad: Nos enorgullece entregar productos que son confiables, seguros y construidos para durar.

Crecimiento Continuo: Como estudiantes del Informatorio, estamos en un aprendizaje constante, lo que nos permite adaptarnos rápidamente a las necesidades cambiantes del mercado.

Lo Que Nos Diferencia
Compromiso con la Excelencia: Cada miembro de COWORKING aporta su experiencia y dedicación, lo que nos permite ofrecer soluciones de desarrollo web que destacan por su calidad y creatividad.

Enfoque Personalizado: Nos aseguramos de entender las necesidades específicas de cada cliente, brindando soluciones hechas a medida.

Futuro Prometedor: Como jóvenes talentos en la programación, nuestro enfoque fresco y actualizado nos permite abordar los desafíos desde una perspectiva innovadora.

Gracias por confiar en COWORKING. Estamos emocionados de llevar sus proyectos al siguiente nivel con nuestra pasión y habilidades en desarrollo web. ¡Juntos, construiremos el futuro digital!""",
    )
    texto.config(font=("arial", 11), state=tk.DISABLED)

    # Botón Volver (cierra la ventana "Acerca de")
    btn_cerrar = tk.Button(
        ventana_acerca_de,
        text="Volver",
        command=lambda: cerrar_ventana(ventana_acerca_de),
    )
    btn_cerrar.place(relx=0.8, rely=0.9, anchor="center")


# btn.pack(x=150, y=400)


# Crear la ventana principal (Lobby)

# Configuración de la ventana principal (ANA)
ventana = tk.Tk()
ventana.title("Recetario")
ventana.geometry("670x700+300+0")
ventana.resizable(width=False, height=False)


# Carga la imagen de fondo
fondo = ImageTk.PhotoImage(
    Image.open("./Miniproyecto/UNIFICADO/IMAGENES/FONDO1.png").resize((670, 700))
)


# Crea y empaqueta la imagen de fondo
label_fondo = tk.Label(ventana, image=fondo)
label_fondo.place(relwidth=1, relheight=1)

# Ejemplo de entrada de usuario
entrada_usuario = PlaceholderEntry(
    ventana,
    placeholder="Ej: Juan",
    foreground="white",
    bg="#380039",
    borderwidth=0,
    relief="flat",
    font=("Roboto Condensed", 14),
)
# Ajusta la posición y tamaño de la entrada
entrada_usuario.place(x=230, y=500, width=190, height=50)

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
    foreground="black",
    bg="#380039",
    borderwidth=0,
    relief="flat",
    activebackground="#380039",
    activeforeground="white",
    font=("Roboto Condensed", 15),
)
boton_ok.place(x=482, y=500, width=50, height=50)  # Ajusta la posición del botón


# Correr la ventana
ventana.mainloop()
