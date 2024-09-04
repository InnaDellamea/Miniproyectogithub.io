import tkinter as tk

class Cronometro:
    def __init__(self, master):
        self.master = master
        self.horas = 0
        self.minutos = 0
        self.segundos = 0
        self.milisegundos = 0
        self.corriendo = False
        self.display = tk.StringVar()               #Tipo texto, donde guarda los numeros.
        self.actualizar_display ("00:00:00:000")     #va a ir actualizando la pantalla.
        
        
        #configuracion de la interfaz grafica
        self.master.title("Cronometro")
        self.master.configure(bg="#BCA9F5")
        self.master.geometry("570x600+300+100")
        self.display_label = tk.Label(master, width=100, height=2, textvariable=self.display, font=("Arial",50), bg="#D8CEF6",fg="#ffffff") #etiqueta donde van los numero (000000)
        
        self.display_label.pack()  #pack, asegura que la etiqeuta este adentro de la interfaz
        self.button_frame = tk.Frame(master,width=15, height=3, bg="#000000") #aca van los botenes (inicial, reiniciar, restaurar)
        self.button_frame.pack()
        
        self.star_button = tk.Button(self.button_frame, width=15, height=3,text="Iniciar", command=self.iniciar, bg="#2ecc71", fg="#ffffff")
        self.star_button.pack(side=tk.LEFT, padx=5, pady=10)
        
        self.stop_button = tk.Button(self.button_frame, width=15, height=3,text="Pausar", command=self.detener, bg="#FE2E2E", fg="#ffffff")
        self.stop_button.pack(side=tk.LEFT, padx=5, pady=10)
        
        self.reset_button = tk.Button(self.button_frame,width=15, height=3, text="Reiniciar", command=self.reiniciar, bg="#01A9DB", fg="#ffffff")
        self.reset_button.pack(side=tk.RIGHT, padx=5, pady=10)
      
        
    #Actualizar_display
    def actualizar_display(self, tiempo):  #Se actualiza la ventana(label donde esta el cronometro)
        self.display.set(tiempo)
        

    #Inicia
    def iniciar(self):
        if not self.corriendo:
            self.corriendo = True 
            self.actualizar_cronometro()

    #Detener
    def detener(self):
        self.corriendo = False
        
    #Reinciar
    def reiniciar(self):
        self.horas = 0
        self.minutos = 0
        self.segundos = 0
        self.milisegundos = 0
        self.actualizar_display ("00:00:00.000")

    #Actualizar_cronometro
    def actualizar_cronometro(self):
        if self.corriendo:         
            self.milisegundos += 10
            if self.milisegundos >= 1000:
                self.milisegundos = 0
                self.segundos += 1
            if self.segundos ==60:
                self.segundos =0
                self.minutos +=1
            if self.minutos ==60:
                self.minutos =0
                self.horas += 1
                
            tiempo_formateado = f"{self.horas:02}:{self.minutos:02}:{self.segundos:02}.{self.milisegundos:03}"  
            self.actualizar_display(tiempo_formateado)      
            self.master.after(10, self.actualizar_cronometro)  # Cada 10 milisegundos vamos a llamar a la función actualizar cronómetro.       

if __name__ == "__main__":
    root = tk.Tk()
    cronometro = Cronometro(root)       
    root.mainloop()