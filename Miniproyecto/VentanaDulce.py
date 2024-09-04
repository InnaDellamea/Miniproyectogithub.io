import tkinter as tk
from tkinter import font

ventana = tk.Tk()
ventana.title("🧁Recetas Dulces🧁")
ventana.geometry('670x700+50+10')
ventana.config(bg="pink", cursor="heart")


titulo = tk.Label(
ventana, text="🧁 Recetas Dulces 🧁", bg="pink", font=('candara', 28, "bold"))
titulo.pack()
titulo.place(x=180, y=80)

subtitulo = tk.Label(
    ventana, text='Selecciona una opción:', bg="pink", font=('candara', 20, "bold"))
subtitulo.pack()
subtitulo.place(x=200, y=150)


def cremaDeLimon():
    cremaDeLimon = tk.Toplevel()
    cremaDeLimon.title('Crema de Limón🍋')
    cremaDeLimon.geometry('670x700+50+10')
    cremaDeLimon.focus()
    cremaDeLimon.grab_set()
    cremaDeLimon.config(cursor="heart")

    nombreReceta = tk.Label(
        cremaDeLimon, text='"Crema de Limón🍋''', font=('candara', 20))
    nombreReceta.pack()
    nombreReceta.place(x=195, y=40)

    ingredientes = tk.Label(cremaDeLimon, text='''Ingredientes:

 1)  50 gramos de mantequilla sin sal
 2)  100 gramos de azucar glass
 3)  2 limones ''', justify='left', font=('candara', 12))
    ingredientes.pack()
    ingredientes.place(x=15, y=100)

    preparación = tk.Label(cremaDeLimon, text='''Preparación:

 1) En un bowl, mezclar la mantequilla blanda con el azucar glass tamizada.
    El resultado debe ser una crema blanda de consistencia homogénea.                          
 2) Agregar el zumo de limon y mezclar de nuevo.
    Comprueba la acidez, y si es necesario agrega mas zumo.
    Dejar enfriar y disfrutar!! ''', justify='left', font=('candara', 12))
    preparación.pack()
    preparación.place(x=15, y=250)
    boton_cerrar = tk.Button(
        cremaDeLimon,
        text="Cerrar ventana", bg="pink",
        command=cremaDeLimon.destroy
    )
    boton_cerrar.place(x=450, y=550)


def VasitoOreo():
    VasitoOreo = tk.Toplevel()
    VasitoOreo.title('Vasito Oreo🍪')
    VasitoOreo.geometry('670x700+50+10')
    VasitoOreo.focus()
    VasitoOreo.grab_set()
    VasitoOreo.config(cursor="heart")

    nombreReceta = tk.Label(
        VasitoOreo, text='"Vasito Oreo🍪''', font=('candara', 20))
    nombreReceta.pack()
    nombreReceta.place(x=195, y=40)
#   INGREDIENTES
    ingredientes = tk.Label(VasitoOreo, text='''Ingredientes:

1)	Restos de bizcochuelo, magdalena o vainillas
2)	250 g de leche condensada
3)	1 yogur
4)	1 cda. de azúcar negra
5)	1 trozo de chocolate negro
 ''', justify='left', font=('candara', 12))
    ingredientes.pack()
    ingredientes.place(x=15, y=100)

#   PREPARACIÓN
    preparación = tk.Label(VasitoOreo, text='''Preparación:

1)  Desmenuza el bizcochuelo y colócalo como base en los vasitos.
2)	Espolvorea azúcar negra para darle un toque terroso.
3)	Bate el yogur y pon una cucharada en cada vasito.
4)	Alterna cucharadas de leche condensada y yogur hasta llenar los vasitos.
5)	Ralla el chocolate encima y listo! ''', justify='left', font=('candara', 12))
    preparación.pack()
    preparación.place(x=15, y=250)
    boton_cerrar = tk.Button(
        VasitoOreo,
        text="Cerrar ventana", bg="pink",
        command=VasitoOreo.destroy
    )
    boton_cerrar.place(x=450, y=550)


def Crepes():
    Crepes = tk.Toplevel()
    Crepes.title('Crepes')
    Crepes.geometry('670x700+50+10')
    Crepes.focus()
    Crepes.grab_set()
    Crepes.config(cursor="heart")

    nombreReceta = tk.Label(
        Crepes, text='"Crepes 🫓"', font=('candara', 20))
    nombreReceta.pack()
    nombreReceta.place(x=150, y=20)
#   INGREDIENTES
    ingredientes = tk.Label(Crepes, text='''Ingredientes:
                            
1)  2 huevos
2)  150 g de harina
3)  1 cucharadita de azúcar (opcional)
4)  1 pizca de sal
5)  250 ml de leche
7)  aceite para engrasar la sartén de bizcochuelo, magdalena o vainillas
 ''', justify='left', font=('candara', 12))
    ingredientes.pack()
    ingredientes.place(x=15, y=80)

#   PREPARACIÓN
    preparación = tk.Label(Crepes, text='''Preparación:
                           
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
   Acompañalos con Dulce de Leche o Miel! y A Disfrutar!''', justify='left', font=('candara', 12))
    preparación.pack()
    preparación.place(x=15, y=250)
    boton_cerrar = tk.Button(
        Crepes,
        text="Cerrar ventana", bg="pink",
        command=Crepes.destroy
    )
    boton_cerrar.place(x=550, y=600)


def galletasDeAvena():
    galletasDeAvena = tk.Toplevel()
    galletasDeAvena.title('Galletas de Avena🍪')
    galletasDeAvena.geometry('670x700+50+10')
    galletasDeAvena.focus()
    galletasDeAvena.grab_set()
    galletasDeAvena.config(cursor="heart")

    nombreReceta = tk.Label(
        galletasDeAvena, text='"Galletas de Avena🍪''', font=('candara', 20))
    nombreReceta.pack()
    nombreReceta.place(x=195, y=40)
#   INGREDIENTES
    ingredientes = tk.Label(galletasDeAvena, text='''Ingredientes:

1)	2 plátanos maduros
2)	50 gramos pasas de uva
3)	150 gramos de copos de avena
4)	50 gramos de chips de chocolate negro

 ''', justify='left', font=('candara', 12))
    ingredientes.pack()
    ingredientes.place(x=15, y=100)

#   PREPARACIÓN
    preparación = tk.Label(galletasDeAvena, text='''Preparación:

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
 ''', justify='left', font=('candara', 12))
    preparación.pack()
    preparación.place(x=15, y=250)
    boton_cerrar = tk.Button(
        galletasDeAvena,
        text="Cerrar ventana", bg="pink",
        command=galletasDeAvena.destroy
    )
    boton_cerrar.place(x=450, y=550)


def budinDePan():
    budinDePan = tk.Toplevel()
    budinDePan.title('Budín de Pan🍮')
    budinDePan.geometry('670x700+50+10')
    budinDePan.focus()
    budinDePan.grab_set()
    budinDePan.config(cursor="heart")

    nombreReceta = tk.Label(
        budinDePan, text='"Budín de Pan🍮''', font=('candara', 20))
    nombreReceta.pack()
    nombreReceta.place(x=195, y=40)
#   INGREDIENTES
    ingredientes = tk.Label(budinDePan, text='''Ingredientes:
1)  3 huevos
2)  500 mililitros de leche
3)  1 cucharadita de esencia de vainilla
4)  150 gramos de pan de barra o pan de molde
5)  150 gramos de azúcar (¾ taza)
6)  1 limón (ralladura)
7)  200 gramos de azúcar (1 taza)
 ''', justify='left', font=('candara', 12))
    ingredientes.pack()
    ingredientes.place(x=15, y=100)

#   PREPARACIÓN
    preparación = tk.Label(budinDePan, text='''Preparación:

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
 ''', justify='left', font=('candara', 12))
    preparación.pack()
    preparación.place(x=15, y=260)
    boton_cerrar = tk.Button(
        budinDePan,
        text="Cerrar ventana", bg="pink",
        command=budinDePan.destroy
    )
    boton_cerrar.place(x=500, y=630)


def flan():
    flan = tk.Toplevel()
    flan.title('Flan🍮')
    flan.geometry('670x700+50+10')
    flan.focus()
    flan.grab_set()
    flan.config(cursor="heart")

    nombreReceta = tk.Label(
        flan, text='"Flan🍮''', font=('candara', 20))
    nombreReceta.pack()
    nombreReceta.place(x=195, y=40)
#   INGREDIENTES
    ingredientes = tk.Label(flan, text='''Ingredientes:

1)  300 mililitros de Leche (1¼ tazas)
2)	5 Huevos
3)  135 gramos de Azúcar blanco
4)  1 pizca de Esencia de vainilla
5)  100 gramos de Azúcar blanco para el caramelo

 ''', justify='left', font=('candara', 12))
    ingredientes.pack()
    ingredientes.place(x=15, y=100)

#   PREPARACIÓN
    preparación = tk.Label(flan, text='''Preparación:

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
 ''', justify='left', font=('candara', 12))
    preparación.pack()
    preparación.place(x=15, y=250)
    boton_cerrar = tk.Button(
        flan,
        text="Cerrar ventana", bg="pink",
        command=flan.destroy
    )
    boton_cerrar.place(x=450, y=550)


def tartaDeYogur():
    tartaDeYogur = tk.Toplevel()
    tartaDeYogur.title('Tarta de Yogur🥧')
    tartaDeYogur.geometry('670x700+50+10')
    tartaDeYogur.focus()
    tartaDeYogur.grab_set()
    tartaDeYogur.config(cursor="heart")

    nombreReceta = tk.Label(
        tartaDeYogur, text='"Tarta de Yogur🥧''', font=('candara', 20))
    nombreReceta.pack()
    nombreReceta.place(x=195, y=40)

    ingredientes = tk.Label(tartaDeYogur, text='''Ingredientes:

1) 	625 g yogur griego sin azúcar
2)	4 huevos 
3)	50 g edulcorante
4)	Unas gotitas de esencia de vainilla
 ''', justify='left', font=('candara', 12))
    ingredientes.pack()
    ingredientes.place(x=15, y=100)

    preparación = tk.Label(tartaDeYogur, text='''Preparación:

1)	Batimos todos los ingredientes en un bol.
2)	Vertemos la mezcla en un molde desmontable y forrado o engrasado.
3)	Con el horno previamente precalentado a 170ºC, horneamos durante unos 70-90min, 
    hasta que se doren los bordes.
4)	Dejamos reposar y enfriamos por completo en la heladera.
5)	Opcionalmente, podemos decorar con un poco de mermelada sin azúcar. 
                    ¡Y lista!
 ''', justify='left', font=('candara', 12))
    preparación.pack()
    preparación.place(x=15, y=250)
    boton_cerrar = tk.Button(
        tartaDeYogur,
        text="Cerrar ventana", bg="pink",
        command=tartaDeYogur.destroy
    )
    boton_cerrar.place(x=450, y=550)


def tartaDeNaranja():
    tartaDeNaranja = tk.Toplevel()
    tartaDeNaranja.title('Tarta de Naranja🍊')
    tartaDeNaranja.geometry('670x700+50+10')
    tartaDeNaranja.focus()
    tartaDeNaranja.grab_set()
    tartaDeNaranja.config(cursor="heart")

    nombreReceta = tk.Label(
        tartaDeNaranja, text='"Tarta de Naranja🍊''', font=('candara', 20))
    nombreReceta.pack()
    nombreReceta.place(x=195, y=40)

    ingredientes = tk.Label(tartaDeNaranja, text='''Ingredientes:

1)  200 ml leche evaporada
2)	200 ml nata líquida para montar (crema de leche)
3)  100 ml zumo de naranja
4)	3 láminas gelatina neutra (o 7,5g de gelatina en polvo)
5)	Edulcorante al gusto (yo 60g eritritol)
6)	La ralladura de una naranja
''', justify='left', font=('candara', 12))
    ingredientes.pack()
    ingredientes.place(x=15, y=100)

    preparación = tk.Label(tartaDeNaranja, text='''Preparación:

1) Hidratamos la gelatina en agua fría hasta que esté blandita.
2) En un cazo a fuego medio, ponemos el zumo de naranja. Escurrimos la gelatina 
   y la integramos en el zumo. Añadimos el edulcorante hasta que se integre bien. Reservamos.
3) En un bol, batimos la leche evaporada y la nata bien fría,añadimos la ralladura de 
   naranja y batimos un poco más.
4) Vertemos el zumo de naranja con gelatina, y lo integramos con movimientos envolventes.
5) Ponemos nuestra mezcla en un molde, mejor si es de silicona, y congelamos durante al
   menos 4 horas.
   Desmoldamos, ¡y lista!''', justify='left', font=('candara', 12))
    preparación.pack()
    preparación.place(x=15, y=270)
    boton_cerrar = tk.Button(
        tartaDeNaranja,
        text="Cerrar ventana", bg="pink",
        command=tartaDeNaranja.destroy
    )
    boton_cerrar.place(x=450, y=550)


def choco():
    choco = tk.Toplevel()
    choco.title('Postre de Chocolate🍫')
    choco.geometry('670x700+50+10')
    choco.focus()
    choco.grab_set()
    choco.config(cursor="heart")

    nombreReceta = tk.Label(
        choco, text='"Postre de Chocolate🍫"', font=('candara', 20))
    nombreReceta.pack()
    nombreReceta.place(x=195, y=40)

    ingredientes = tk.Label(choco, text='''Ingredientes:

1) 125 ml. yogurt natural sin azúcar
2) 1 sobrecito de sucralosa
3) 1 cda. de semillas de chía
4) 1 cda. de cacao en polvo sin azúcar
5) Galletas de arroz
6) Menta o hierba buena
7) Almendras ''', justify='left', font=('candara', 12))
    ingredientes.pack()
    ingredientes.place(x=15, y=100)

    preparación = tk.Label(choco, text='''Preparación:
                           
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
    Por ultimo algunas almendras, que rico!''', justify='left', font=('candara', 12))
    preparación.pack()
    preparación.place(x=15, y=290)
    boton_cerrar = tk.Button(
        choco,
        text="Cerrar ventana", bg="pink",
        command=choco.destroy
    )
    boton_cerrar.place(x=450, y=550)


def arrozCLeche():
    arrozCLeche = tk.Toplevel()
    arrozCLeche.title('Arroz con Leche🥣')
    arrozCLeche.geometry('670x700+50+10')
    arrozCLeche.focus()
    arrozCLeche.grab_set()
    arrozCLeche.config(cursor="heart")

    nombreReceta = tk.Label(
        arrozCLeche, text='"Arroz con Leche🥣''', font=('candara', 20))
    nombreReceta.pack()
    nombreReceta.place(x=195, y=40)

    ingredientes = tk.Label(arrozCLeche, text='''Ingredientes:

1) 100g. de arroz (preferentemente para risotto)
2) 1 litro de leche
3) 150g. de azúcar
4) canela (en rama y en polvo)
5) cáscara de limón
 ''', justify='left', font=('candara', 12))
    ingredientes.pack()
    ingredientes.place(x=15, y=100)

    preparación = tk.Label(arrozCLeche, text='''Preparación:

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
    
 ''', justify='left', font=('candara', 12))
    preparación.pack()
    preparación.place(x=15, y=250)
    boton_cerrar = tk.Button(
        arrozCLeche,
        text="Cerrar ventana", bg="pink",
        command=arrozCLeche.destroy
    )
    boton_cerrar.place(x=450, y=550)


def gelatina():
    gelatina = tk.Toplevel()
    gelatina.title('Gelatina de Fresa🍓')
    gelatina.geometry('670x700+50+10')
    gelatina.focus()
    gelatina.grab_set()
    gelatina.config(cursor="heart")

    nombreReceta = tk.Label(
        gelatina, text='"Gelatina de Fresa🍓''', font=('candara', 20))
    nombreReceta.pack()
    nombreReceta.place(x=195, y=40)

    ingredientes = tk.Label(gelatina, text='''Ingredientes:

1) 	3 sobres de gelatina sabor fresa de 120 gramos cada uno 
2)  1 lata de media crema de 225 gramos 
3)  1.5 litros de agua mas aparte otros 750 mililitros 
 ''', justify='left', font=('candara', 12))
    ingredientes.pack()
    ingredientes.place(x=15, y=100)

    preparación = tk.Label(gelatina, text='''Preparación:

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

 ''', justify='left', font=('candara', 12))
    preparación.pack()
    preparación.place(x=15, y=250)
    boton_cerrar = tk.Button(
        gelatina,
        text="Cerrar ventana", bg="pink",
        command=gelatina.destroy
    )
    boton_cerrar.place(x=450, y=550)


def brownie():
    brownie = tk.Toplevel()
    brownie.title('Brownie 🍫')
    brownie.geometry('670x700+50+10')
    brownie.focus()
    brownie.grab_set()
    brownie.config(cursor="heart")

    nombreReceta = tk.Label(
        brownie, text='"Brownie 🍫''', font=('candara', 20))
    nombreReceta.pack()
    nombreReceta.place(x=195, y=40)

    ingredientes = tk.Label(brownie, text='''Ingredientes:

1) 3 huevos
2) 1 taza azúcar
3) 1/2 taza aceite
4) 1 taza cacao
5) 1/2 taza harina 0000
 ''', justify='left', font=('candara', 12))
    ingredientes.pack()
    ingredientes.place(x=15, y=100)

    preparación = tk.Label(brownie, text='''Preparación:

1)  En un bol batir los tres huevos con el azúcar hasta espumar.
2)  Agregar el aceite y batir.
3)  Integrar la taza de cacao a la mezcla anterior.
4)  Agregar la media taza de harina mientras batimos.
5)  Llevar a horno precalentando por unos 30/40 minutos en un molde previamente
    enmantecado. Y Listo!
 ''', justify='left', font=('candara', 12))
    preparación.pack()
    preparación.place(x=15, y=250)
    boton_cerrar = tk.Button(
        brownie,
        text="Cerrar ventana", bg="pink",
        command=brownie.destroy
    )
    boton_cerrar.place(x=450, y=550)


boton1 = tk.Menubutton(ventana, text="1) Sin Horno🍧",
                       font=("candara", 20), bd=5)
boton1.place(x=250, y=220)
menu = tk.Menu(boton1)
boton1.config(menu=menu, bg="pink")
menu.add_command(label='Crema de Limón 🍋', font=(
    'candara', 12), command=cremaDeLimon)
menu.add_command(label='Vasito Oreo 🍪', font=(
    'candara', 12), command=VasitoOreo)
menu.add_command(label='Crepes 🫓', font=('candara', 12), command=Crepes)


boton2 = tk.Menubutton(ventana, text="2) Al Micro🍮",
                       font=("candara", 20), bd=5)
boton2.place(x=250, y=290)
menu = tk.Menu(boton2)
boton2.config(menu=menu, bg="pink")
menu.add_command(label='Galletas de Avena🍪', font=(
    'candara', 12), command=galletasDeAvena)
menu.add_command(label='Budín de Pan🍮', font=(
    'candara', 12), command=budinDePan)
menu.add_command(label='Flan🍮', font=(
    'candara', 12), command=flan)

boton3 = tk.Menubutton(ventana, text="3) Sin Azúcar🍰",
                       font=("candara", 20), bd=5)
boton3.place(x=250, y=370)
menu = tk.Menu(boton3)
boton3.config(menu=menu, bg="pink")
menu.add_command(label="Tarta de yogur al Horno 🥧", font=(
    'candara', 12), command=tartaDeYogur)
menu.add_command(label='Tarta de Naranja🍊', font=(
    'candara', 12), command=tartaDeNaranja)
menu.add_command(label='Postrecito de Chocolate🍫', font=(
    'candara', 12), command=choco)

boton4 = tk.Menubutton(ventana, text="4) Económicas🥐",
                       font=("candara", 20), bd=5)
boton4.place(x=250, y=450)
menu = tk.Menu(boton4)
boton4.config(menu=menu, bg="pink")
menu.add_command(label='Arroz con Leche 🥣', font=(
    'candara', 12), command=arrozCLeche)
menu.add_command(label='Gelatina de Fresa 🍓', font=(
    'candara', 12), command=gelatina)
menu.add_command(label='Brownie 🍫', font=(
    'candara', 12), command=brownie)

ventana.mainloop()
