import tkinter as tk
from tkinter import *

# ------------ ventana principal de recetas saladas ------------
ventana = tk.Tk()
ventana.title('ventana_salado')
ventana.geometry('670x700+1200+100')
ventana.resizable(False,False)

# ------------ Titulo "Recetas saladas" ------------
texto_recetas_saladas = tk.Label(ventana, text= 'Recetas saladas', font=('nunito', 28,'bold' ))
texto_recetas_saladas.pack()
texto_recetas_saladas.place(x=195, y=40)

# ------------ Subtitulo "Elige la receta" ------------
texto_elige_receta = tk.Label(ventana, text='Elige la receta:', font=('nunito', 20))
texto_elige_receta.pack()
texto_elige_receta.place(x=250, y=120)



# -------------------- FUNCIONES CON LAS RECETAS--------------------


def milanesa_napo():
    ventana_mila_napo = tk.Toplevel()
    ventana_mila_napo.title('Milanesas a la napolitana')
    ventana_mila_napo.geometry('670x700+1200+100')

    #   TITULO DE LA RECETA 
    titulo = tk.Label(ventana_mila_napo, text='''Milanesas a la napolitana 🍕''', font=('nunito', 20))
    titulo.pack()
    titulo.place(x=195, y=40)
#   INGREDIENTES
    ingredientes = tk.Label(ventana_mila_napo, text='''Ingredientes:

4 milanesas de carne de res
1 taza de pan rallado
1/2 taza de queso rallado
1 huevo
1 taza de salsa de tomate
100 g de jamón cocido
Aceite para freír
Sal y pimienta al gusto''', justify='left', font=('nunito', 12))
    ingredientes.pack()
    ingredientes.place(x=15, y=100)

#   PREPARACIÓN
    preparación = tk.Label(ventana_mila_napo, text='''Preparación:

Batir el huevo en un plato y mezclar el pan rallado con el queso rallado en otro.
Pasar las milanesas por el huevo y luego por la mezcla de pan rallado y queso.
Freír en aceite caliente hasta dorar y cocinar completamente. Colocar sobre papel 
absorbente.
Precalentar el horno a 180°C. Colocar las milanesas en una fuente para horno, cubrir 
con salsa de tomate, una loncha de jamón y más queso rallado.
Hornear durante 10-15 minutos o hasta que el queso esté fundido y dorado.''', justify='left', font=('nunito', 12))
    preparación.pack()
    preparación.place(x=15, y=350)    

 # ERROR  
    scrol_vertical = tk.Scrollbar(ventana_mila_napo,orient='vertical', command=preparación.yview)
    scrol_vertical.pack(side='right',fill='y')
    #scrol_vertical.config()
    scrol_vertical.mainloop()    


                        


def empanadas_carne():
    ventana_empanadas_carne = tk.Toplevel()
    ventana_empanadas_carne.title('Empanadas de carne')
    ventana_empanadas_carne.geometry('670x700+1200+100')

#   TITULO DE LA RECETA 
    titulo = tk.Label(ventana_empanadas_carne, text='''Empanadas de carne 🥟''', font=('nunito', 20))
    titulo.pack()
    titulo.place(x=195, y=40)
#   INGREDIENTES
    ingredientes = tk.Label(ventana_empanadas_carne, text='''Ingredientes:

500 g de carne de res picada
1 cebolla picada
1 pimiento rojo picado
2 huevos duros picados
10 aceitunas verdes picadas
1 cucharadita de comino
1 cucharadita de pimentón
Sal y pimienta al gusto
Masa para empanadas (puedes comprarla ya hecha o hacerla en casa)''', justify='left', font=('nunito', 12))
    ingredientes.pack()
    ingredientes.place(x=15, y=100)

#   PREPARACIÓN
    preparacion = tk.Label(ventana_empanadas_carne, text='''Preparación:

Sofreír la cebolla y el pimiento en una sartén con un poco de aceite hasta que 
estén tiernos.
Añadir la carne y cocinar hasta que esté bien dorada. Incorporar los huevos, 
aceitunas, comino, pimentón, sal y pimienta. Mezclar bien.
Dejar enfriar el relleno. Colocar una cucharada del relleno en cada disco de 
masa para empanadas, cerrar y sellar los bordes con un tenedor.
Hornear a 200°C durante 15-20 minutos o hasta que estén doradas.''', justify='left', font=('nunito', 12))
    preparacion.pack()
    preparacion.place(x=15, y=350)


def milanesa_pollo():
    ventana_milanesas_pollo = tk.Toplevel()
    ventana_milanesas_pollo.title('Milanesas de pollo')
    ventana_milanesas_pollo.geometry('670x700+1200+100')

#   TITULO DE LA RECETA 
    titulo = tk.Label(ventana_milanesas_pollo, text='''Milanesas de pollo 🍗''', font=('nunito', 20))
    titulo.pack()
    titulo.place(x=195, y=40)
    
#   INGREDIENTES
    ingredientes = tk.Label(ventana_milanesas_pollo, text='''Ingredientes:

4 pechugas de pollo
1 taza de pan rallado
1/2 taza de queso rallado
1 huevo
Sal y pimienta al gusto
Aceite para freír''', justify='left', font=('nunito', 12))
    ingredientes.pack()
    ingredientes.place(x=15, y=100)

#   PREPARACIÓN
    preparacion = tk.Label(ventana_milanesas_pollo, text='''Preparación:

Aplastar las pechugas de pollo para que queden más finas. Salpimentar.
Batir el huevo y mezclar el pan rallado con el queso rallado.
Pasar las pechugas por el huevo y luego por la mezcla de pan rallado.
Freír en aceite caliente hasta dorar y cocinar completamente. Servir con limón.
''', justify='left', font=('nunito', 12))
    preparacion.pack()
    preparacion.place(x=15, y=350)


def asado_ensalada():
    ventana_asado_con_ensalada = tk.Toplevel()
    ventana_asado_con_ensalada.title('Asado con ensalada criolla')
    ventana_asado_con_ensalada.geometry('670x700+1200+100')

#   TITULO DE LA RECETA 
    titulo = tk.Label(ventana_asado_con_ensalada, text='''Asado con ensalada criolla 🥩''', font=('nunito', 20))
    titulo.pack()
    titulo.place(x=195, y=40)
    
#   INGREDIENTES
    ingredientes = tk.Label(ventana_asado_con_ensalada, text='''Ingredientes:

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
Sal y pimienta al gusto''', justify='left', font=('nunito', 12))
    ingredientes.pack()
    ingredientes.place(x=15, y=100)

#   PREPARACIÓN
    preparacion = tk.Label(ventana_asado_con_ensalada, text='''Preparación:

Salpimentar las costillas y espolvorear con pimentón. Cocinar a la parrilla a fuego 
medio durante 40-50 minutos, girando ocasionalmente.
Para la ensalada, mezclar los tomates, cebolla, pimiento y pepino en un bol.
Añadir vinagre, aceite, sal y pimienta. Mezclar bien y servir con el asado.''', justify='left', font=('nunito', 12))
    preparacion.pack()
    preparacion.place(x=15, y=440)


def lentejas_guisadas():
    ventana_lentejas_guisadas = tk.Toplevel()
    ventana_lentejas_guisadas.title('Lentejas guisadas')
    ventana_lentejas_guisadas.geometry('670x700+1200+100')

#   TITULO DE LA RECETA 
    titulo = tk.Label(ventana_lentejas_guisadas, text='''Lentejas guisadas 🍵''', font=('nunito', 20))
    titulo.pack()
    titulo.place(x=195, y=40)
    
#   INGREDIENTES
    ingredientes = tk.Label(ventana_lentejas_guisadas, text='''Ingredientes:

1 taza de lentejas
1 cebolla picada
1 zanahoria picada
2 dientes de ajo picados
1 pimiento verde picado
1 litro de caldo de verduras
1 cucharada de pimentón
Sal y pimienta al gusto
Aceite de oliva''', justify='left', font=('nunito', 12))
    ingredientes.pack()
    ingredientes.place(x=15, y=100)

#   PREPARACIÓN
    preparacion = tk.Label(ventana_lentejas_guisadas, text='''Preparación:

Sofreír la cebolla, zanahoria, ajo y pimiento en aceite hasta que 
estén tiernos.
Añadir las lentejas, el pimentón, el caldo, sal y pimienta. Cocinar a 
fuego lento durante 30-40 minutos, o hasta que las lentejas estén 
tiernas. Ajustar la sazón.''', justify='left', font=('nunito', 12))
    preparacion.pack()
    preparacion.place(x=15, y=350)


def pastas_bolognesa():
    ventana_pastas_bolognesa = tk.Toplevel()
    ventana_pastas_bolognesa.title('Pastas con salsa bolognesa')
    ventana_pastas_bolognesa.geometry('670x700+1200+100')

#   TITULO DE LA RECETA 
    titulo = tk.Label(ventana_pastas_bolognesa, text='''Pastas con salsa bolognesa 🍝''', font=('nunito', 20))
    titulo.pack()
    titulo.place(x=195, y=40)
    
#   INGREDIENTES
    ingredientes = tk.Label(ventana_pastas_bolognesa, text='''Ingredientes:

250 g de pasta (espaguetis, penne, etc.)
300 g de carne picada de res
1 cebolla picada
2 dientes de ajo picados
1 zanahoria picada
400 g de salsa de tomate
1 cucharadita de orégano
Sal y pimienta al gusto
Queso rallado para servir''', justify='left', font=('nunito', 12))
    ingredientes.pack()
    ingredientes.place(x=15, y=100)

#   PREPARACIÓN
    preparacion = tk.Label(ventana_pastas_bolognesa, text='''Preparación:

Cocinar la pasta según las instrucciones del paquete.
Sofreír la cebolla, ajo y zanahoria en una sartén con aceite hasta que 
estén tiernos. Añadir la carne y cocinar hasta dorar.
Incorporar la salsa de tomate, orégano, sal y pimienta. Cocinar a fuego 
lento durante 20 minutos.
Mezclar con la pasta cocida y servir con queso rallado.''', justify='left', font=('nunito', 12))
    preparacion.pack()
    preparacion.place(x=15, y=350)


def pollo_papas():
    ventana_pollo_papas = tk.Toplevel()
    ventana_pollo_papas.title('Pollo al horno con papas')
    ventana_pollo_papas.geometry('670x700+1200+100')

#   TITULO DE LA RECETA 
    titulo = tk.Label(ventana_pollo_papas, text='''Pollo al horno con papas 🍗''', font=('nunito', 20))
    titulo.pack()
    titulo.place(x=195, y=40)
    
#   INGREDIENTES
    ingredientes = tk.Label(ventana_pollo_papas, text='''Ingredientes:

4 muslos de pollo
4 papas, peladas y cortadas en trozos
1 cucharadita de romero seco
3 dientes de ajo picados
3 cucharadas de aceite de oliva
Sal y pimienta al gusto''', justify='left', font=('nunito', 12))
    ingredientes.pack()
    ingredientes.place(x=15, y=100)

#   PREPARACIÓN
    preparacion = tk.Label(ventana_pollo_papas, text='''Preparación:

Precalentar el horno a 200°C.
Mezclar el aceite, romero, ajo, sal y pimienta. Frotar la mezcla 
sobre el pollo y las papas.
Colocar en una fuente para horno y hornear durante 40-50 minutos, 
o hasta que el pollo esté bien cocido y las papas estén tiernas.''', justify='left', font=('nunito', 12))
    preparacion.pack()
    preparacion.place(x=15, y=350)


def empanadas_jyq():
    ventana_empanada_jyq = tk.Toplevel()
    ventana_empanada_jyq.title('Empanadas de jamon y queso')
    ventana_empanada_jyq.geometry('670x700+1200+100')

#   TITULO DE LA RECETA 
    titulo = tk.Label(ventana_empanada_jyq, text='''Empanadas de jamon y queso 🥟''', font=('nunito', 20))
    titulo.pack()
    titulo.place(x=150, y=40)
    
#   INGREDIENTES
    ingredientes = tk.Label(ventana_empanada_jyq, text='''Ingredientes:

Masa para empanadas
200 g de jamón cocido picado
200 g de queso mozzarella rallado
1 huevo (para pincelar)''', justify='left', font=('nunito', 12))
    ingredientes.pack()
    ingredientes.place(x=15, y=100)

#   PREPARACIÓN
    preparacion = tk.Label(ventana_empanada_jyq, text='''Preparación:

Colocar una cucharada de jamón y queso en cada disco de masa para 
empanadas. Cerrar y sellar los bordes.
Pincelar con huevo batido y hornear a 200°C durante 15-20 minutos o 
hasta que estén doradas.''', justify='left', font=('nunito', 12))
    preparacion.pack()
    preparacion.place(x=15, y=350)


def tarta_espinaca():
    ventana_tarta_espinaca = tk.Toplevel()
    ventana_tarta_espinaca.title('Tarta de espinaca y queso')
    ventana_tarta_espinaca.geometry('670x700+1200+100')

#   TITULO DE LA RECETA 
    titulo = tk.Label(ventana_tarta_espinaca, text='''Tarta de espinaca y queso 🥧''', font=('nunito', 20))
    titulo.pack()
    titulo.place(x=150, y=40)
    
#   INGREDIENTES
    ingredientes = tk.Label(ventana_tarta_espinaca, text='''Ingredientes:

Masa para tarta
300 g de espinacas frescas
200 g de queso ricota
100 g de queso parmesano rallado
2 huevos
Sal y pimienta al gusto
Aceite de oliva''', justify='left', font=('nunito', 12))
    ingredientes.pack()
    ingredientes.place(x=15, y=100)

#   PREPARACIÓN
    preparacion = tk.Label(ventana_tarta_espinaca, text='''Preparación:

Precalentar el horno a 180°C.
Sofreír las espinacas en un poco de aceite hasta que se reduzcan. 
Escurrir el exceso de agua.
Mezclar las espinacas con el queso ricota, parmesano, huevos, 
sal y pimienta.
Extender la masa en una fuente para tarta, rellenar con la mezcla 
de espinacas y hornear durante 30-35 minutos.''', justify='left', font=('nunito', 12))
    preparacion.pack()
    preparacion.place(x=15, y=350)


def guiso_res():
    ventana_guiso_res = tk.Toplevel()
    ventana_guiso_res.title('Guiso de res con papas')
    ventana_guiso_res.geometry('670x700+1200+100')

#   TITULO DE LA RECETA 
    titulo = tk.Label(ventana_guiso_res, text='''Guiso de res con papas 🍵''', font=('nunito', 20))
    titulo.pack()
    titulo.place(x=195, y=40)
    
#   INGREDIENTES
    ingredientes = tk.Label(ventana_guiso_res, text='''Ingredientes:

500 g de carne de res en cubos
2 papas, peladas y cortadas en cubos
1 cebolla picada
1 zanahoria picada
2 dientes de ajo picados
1 litro de caldo de carne
1 cucharadita de comino
Sal y pimienta al gusto
Aceite para cocinar''', justify='left', font=('nunito', 12))
    ingredientes.pack()
    ingredientes.place(x=15, y=100)

#   PREPARACIÓN
    preparacion = tk.Label(ventana_guiso_res, text='''Preparación:

Sofreír la cebolla, zanahoria y ajo en aceite hasta que estén 
tiernos. Añadir la carne y dorar.
Incorporar las papas, caldo, comino, sal y pimienta. 
Cocinar a fuego lento durante 1 hora, o hasta que la carne y 
las papas estén tiernas.''', justify='left', font=('nunito', 12))
    preparacion.pack()
    preparacion.place(x=15, y=350)


def quiche_jyq():
    ventana_quiche_jyq = tk.Toplevel()
    ventana_quiche_jyq.title('Quiche de jamon y queso')
    ventana_quiche_jyq.geometry('670x700+1200+100')

#   TITULO DE LA RECETA 
    titulo = tk.Label(ventana_quiche_jyq, text='''Quiche de jamon y queso 🥧''', font=('nunito', 20))
    titulo.pack()
    titulo.place(x=195, y=40)
    
#   INGREDIENTES
    ingredientes = tk.Label(ventana_quiche_jyq, text='''Ingredientes:

Masa para quiche
200 g de jamón picado
200 g de queso cheddar rallado
3 huevos
200 ml de crema de leche
Sal y pimienta al gusto''', justify='left', font=('nunito', 12))
    ingredientes.pack()
    ingredientes.place(x=15, y=100)

#   PREPARACIÓN
    preparacion = tk.Label(ventana_quiche_jyq, text='''Preparación:

Precalentar el horno a 180°C.
Mezclar los huevos con la crema, sal y pimienta. Agregar el 
jamón y queso.
Extender la masa en una fuente para quiche, verter la 
mezcla y hornear durante 35-40 minutos.
''', justify='left', font=('nunito', 12))
    preparacion.pack()
    preparacion.place(x=15, y=350)


def fideos_tuco():
    ventana_fideos_tuco = tk.Toplevel()
    ventana_fideos_tuco.title('Fideos con tuco')
    ventana_fideos_tuco.geometry('670x700+1200+100')

#   TITULO DE LA RECETA 
    titulo = tk.Label(ventana_fideos_tuco, text='''Fideos con tuco 🍝''', font=('nunito', 20))
    titulo.pack()
    titulo.place(x=195, y=40)
    
#   INGREDIENTES
    ingredientes = tk.Label(ventana_fideos_tuco, text='''Ingredientes:

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
Queso rallado para servir''', justify='left', font=('nunito', 12))
    ingredientes.pack()
    ingredientes.place(x=15, y=100)

#   PREPARACIÓN
    preparacion = tk.Label(ventana_fideos_tuco, text='''Preparación:

Cocinar los fideos según las instrucciones del paquete.
En una sartén grande, calentar aceite de oliva y sofreír la 
cebolla, el ajo, la zanahoria y el pimiento hasta que 
estén tiernos.
Añadir la carne picada y cocinar hasta dorar.
Incorporar la salsa de tomate, el caldo, el orégano, la sal 
y la pimienta. Cocinar a fuego lento durante 20-30 minutos, 
hasta que la salsa espese.
Mezclar con los fideos cocidos y servir con queso rallado.''', justify='left', font=('nunito', 12))
    preparacion.pack()
    preparacion.place(x=15, y=430)



# -------------------- BOTONES DE RECETAS --------------------

# ------------ Boton 1: Milanesas a la napo ------------
boton_receta_uno = tk.Button(ventana, text= '''Milanesas a la 
napolitana''', font= ('nunito',12), width=20, height=3, command=milanesa_napo)
boton_receta_uno.pack() # para que se vea
boton_receta_uno.place(x=50, y=200) # para que aparezca dentro de la ventana

# ------------ Boton 2: Empanadas de carne ------------
boton_receta_dos = tk.Button(ventana, text='''Empanadas de 
carne''', font= ('nunito',12), width=20, height=3, command=empanadas_carne)
boton_receta_dos.pack() # para que se vea
boton_receta_dos.place(x=250, y=200) # para que aparezca dentro de la ventana

# ------------ Boton 3: Milanesas de pollo ------------
boton_receta_tres = tk.Button(ventana, text='''Milanesas de 
pollo''', font= ('nunito',12), width=20, height=3, command=milanesa_pollo)
boton_receta_tres.pack() # para que se vea
boton_receta_tres.place(x=450, y=200) # para que aparezca dentro de la ventana

# ------------ Boton 4: Asado con ensalada criolla ------------
boton_receta_cuatro = tk.Button(ventana, text='''Asado con 
ensalada criolla''', font= ('nunito',12), width=20, height=3, command=asado_ensalada)
boton_receta_cuatro.pack() # para que se vea
boton_receta_cuatro.place(x=50, y=300) # para que aparezca dentro de la ventana

# ------------ Boton 5: Lentejas guisadas ------------
boton_receta_cinco = tk.Button(ventana, text="Lentejas guisadas", font= ('nunito',12), width=20, height=3, command=lentejas_guisadas)
boton_receta_cinco.pack() # para que se vea
boton_receta_cinco.place(x=250, y=300) # para que aparezca dentro de la ventana

# ------------ Boton 6: Pastas con salsa bolognesa ------------
boton_receta_seis = tk.Button(ventana, text='''Pastas con 
salsa bolognesa''', font= ('nunito',12), width=20, height=3, command=pastas_bolognesa)
boton_receta_seis.pack() # para que se vea
boton_receta_seis.place(x=450, y=300) # para que aparezca dentro de la ventana

# ------------ Boton 7: Pollo al horno con papas ------------
boton_receta_siete = tk.Button(ventana, text='''Pollo al horno 
con papas''', font= ('nunito',12), width=20, height=3, command=pollo_papas)
boton_receta_siete.pack() # para que se vea
boton_receta_siete.place(x=50, y=400) # para que aparezca dentro de la ventana

# ------------ Boton 8: Empanadas de jamon y queso ------------
boton_receta_ocho = tk.Button(ventana, text='''Empanadas de 
jamon y queso''', font= ('nunito',12), width=20, height=3, command=empanadas_jyq)
boton_receta_ocho.pack() # para que se vea
boton_receta_ocho.place(x=250, y=400) # para que aparezca dentro de la ventana

# ------------ Boton 9: Tarta de espinaca y queso ------------
boton_receta_nueve = tk.Button(ventana, text='''Tarta espinaca 
y queso''', font= ('nunito',12), width=20, height=3, command=tarta_espinaca)
boton_receta_nueve.pack() # para que se vea
boton_receta_nueve.place(x=450, y=400) # para que aparezca dentro de la ventana

# ------------ Boton 10: Guiso de res con papas ------------
boton_receta_diez = tk.Button(ventana, text='''Guiso de res 
con papas''', font= ('nunito',12), width=20, height=3, command=guiso_res)
boton_receta_diez.pack() # para que se vea
boton_receta_diez.place(x=50, y=500) # para que aparezca dentro de la ventana

# ------------ Boton 11: Quiche de jamon y queso ------------
boton_receta_once = tk.Button(ventana, text='''Quiche de 
jamon y queso''', font= ('nunito',12), width=20, height=3,command=quiche_jyq)
boton_receta_once.pack() # para que se vea
boton_receta_once.place(x=250, y=500) # para que aparezca dentro de la ventana

# ------------ Boton 12: Fideos con tuco ------------
boton_receta_doce = tk.Button(ventana, text="Fideos con tuco", font= ('nunito',12), width=20, height=3, command=fideos_tuco)
boton_receta_doce.pack() # para que se vea
boton_receta_doce.place(x=450, y=500) # para que aparezca dentro de la ventana


# ------------ ejecutando la ventana ------------
ventana.mainloop()

