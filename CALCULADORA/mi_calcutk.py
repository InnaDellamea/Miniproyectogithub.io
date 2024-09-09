import tkinter 

from tkinter import *



ventana = Tk()
ventana.title("CalculinPro 2024")
#ventana.iconbitmap("imagen/calcu.ico")
ventana.geometry("570x600+100+200")
ventana.resizable(False,False)
ventana.configure(bg="#7E57C2")

operacion = ""

def show(value):
    global operacion
    
    if operacion != "" and operacion[0] == "0":
        operacion = ""
    operacion +=value
    label_result.config(text=operacion)

def borrar():
    global operacion
    operacion = ""
    label_result.config(text=operacion)

def calcular():
    global operacion
    result = ""
    if operacion != "":
        try: 
            result= eval(operacion)
        except: 
            result = "error"
            operacion = ""
    label_result.config(text=result)



label_result = Label(ventana, width=25, text="", font=("arial",30),bg= "#FCE4EC")
label_result.pack()

Button (ventana, text= "C" , width=11, height=1, font=("arial",30,"bold"), bd=1, fg= "#fff", bg= "#26C6DA", command=lambda:borrar()).place(x=10,y=100)
Button (ventana, text= "/" , width=5, height=1, font=("arial",30,"bold"), bd=1, fg= "#fff", bg= "#B39DDB", command=lambda: show("/")).place(x=290,y=100)
Button (ventana, text= "x" , width=5, height=1, font=("arial",30,"bold"), bd=1, fg= "#fff", bg= "#B39DDB", command=lambda: show("*")).place(x=430,y=100)

Button (ventana, text= "7" , width=5, height=1, font=("arial",30,"bold"), bd=1, fg= "#fff", bg= "#B39DDB", command=lambda: show("7")).place(x=10,y=200)
Button (ventana, text= "8" , width=5, height=1, font=("arial",30,"bold"), bd=1, fg= "#fff", bg= "#B39DDB", command=lambda: show("8")).place(x=150,y=200)
Button (ventana, text= "9" , width=5, height=1, font=("arial",30,"bold"), bd=1, fg= "#fff", bg= "#B39DDB", command=lambda: show("9")).place(x=290,y=200)
Button (ventana, text= "-" , width=5, height=1, font=("arial",30,"bold"), bd=1, fg= "#fff", bg= "#B39DDB", command=lambda: show("-")).place(x=430,y=200)

Button (ventana, text= "4" , width=5, height=1, font=("arial",30,"bold"), bd=1, fg= "#fff", bg= "#B39DDB", command=lambda: show("4")).place(x=10,y=300)
Button (ventana, text= "5" , width=5, height=1, font=("arial",30,"bold"), bd=1, fg= "#fff", bg= "#B39DDB", command=lambda: show("5")).place(x=150,y=300)
Button (ventana, text= "6" , width=5, height=1, font=("arial",30,"bold"), bd=1, fg= "#fff", bg= "#B39DDB", command=lambda: show("6")).place(x=290,y=300)
Button (ventana, text= "+" , width=5, height=1, font=("arial",30,"bold"), bd=1, fg= "#fff", bg= "#B39DDB", command=lambda: show("+")).place(x=430,y=300)

Button (ventana, text= "1" , width=5, height=1, font=("arial",30,"bold"), bd=1, fg= "#fff", bg= "#B39DDB", command=lambda: show("1")).place(x=10,y=400)
Button (ventana, text= "2" , width=5, height=1, font=("arial",30,"bold"), bd=1, fg= "#fff", bg= "#B39DDB", command=lambda: show("2")).place(x=150,y=400)
Button (ventana, text= "3" , width=5, height=1, font=("arial",30,"bold"), bd=1, fg= "#fff", bg= "#B39DDB", command=lambda: show("3")).place(x=290,y=400)
Button (ventana, text= "0" , width=11, height=1, font=("arial",30,"bold"), bd=1, fg= "#fff", bg= "#B39DDB", command=lambda: show("0")).place(x=10,y=500)

Button (ventana, text= "." , width=5, height=1, font=("arial",30,"bold"), bd=1, fg= "#fff", bg= "#B39DDB", command=lambda: show(".")).place(x=290,y=500)
Button (ventana, text= "=" , width=5, height=3, font=("arial",30,"bold"), bd=1, fg= "#fff", bg= "#EC407A", command=lambda: calcular()).place(x=430,y=400)


ventana.mainloop()


