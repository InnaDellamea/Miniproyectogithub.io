import tkinter as tk
from tkinter import simpledialog, messagebox

class Recetario:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Mis Recetas")
        self.ventana.geometry("600x600+400+50")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg="#82807f")

        self.recetas = {}
        self.botones = []

        self.frame = tk.Frame(self.ventana, bg="#a25cd3")
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.frame, bg="#a25cd3")
        self.scrollbar = tk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar_marco = tk.Frame(self.canvas, bg="#a25cd3")

        self.scrollbar_marco.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollbar_marco, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.title_label = tk.Label(self.scrollbar_marco, text="MIS RECETAS", padx=200, pady=30, font=("Arial", 24), bg="#a25cd3")
        self.title_label.grid(row=0, column=0, columnspan=3, pady=10)

        self.añadir_boton = tk.Button(self.scrollbar_marco, text="Agragar recetas", width=14, height=4, command=self.añadir_receta, font=("Arial",10), bg="#a0a0a0")
        self.añadir_boton.grid(row=1, column=0, pady=10)

    def añadir_receta(self):
        nombre_receta = simpledialog.askstring("Nueva Receta", "Nombre de la receta:")
        if nombre_receta:
            self.recetas[nombre_receta] = ""
            self.actualizar_recetas()

    def actualizar_recetas(self):
        for widget in self.scrollbar_marco.winfo_children():
            if isinstance(widget, tk.Button) and widget != self.añadir_boton:
                widget.destroy()

        row, column = 1, 0
        for recipe in self.recetas:
            button = tk.Button(self.scrollbar_marco, text=recipe, width=16, height=5, command=lambda r=recipe: self.editar_receta(r), bg="#a0a0a0")
            button.grid(row=row, column=column, padx=5, pady=5)
            column += 1
            if column == 3:
                column = 0
                row += 1

        self.añadir_boton.grid(row=row, column=column, padx=5, pady=10)

    def editar_receta(self, nombre_receta):
        editar_ventana = tk.Toplevel(ventana)
        editar_ventana.title(nombre_receta)
        editar_ventana.geometry("600x600")
        editar_ventana.resizable(False, False)
        editar_ventana.configure(bg="#adaaa8")

        bloc_notas = tk.Text(editar_ventana, bg="#a25cd3", font=("Arial"))
        bloc_notas.insert(tk.END, self.recetas[nombre_receta])
        bloc_notas.pack(expand=True, fill=tk.BOTH)

        boton_guardar = tk.Button(editar_ventana, text="Guardar", command=lambda: self.guardar_receta(nombre_receta, bloc_notas.get("1.0", tk.END)))
        boton_guardar.pack(side=tk.LEFT, padx=10, pady=10)

        boton_borrar = tk.Button(editar_ventana, text="Eliminar", command=lambda: self.eliminar_receta(nombre_receta, editar_ventana))
        boton_borrar.pack(side=tk.RIGHT, padx=10, pady=10)

    def guardar_receta(self, nombre_receta, contenido):
        self.recetas[nombre_receta] = contenido
        messagebox.showinfo("Guardar", f"Receta '{nombre_receta}' guardada.")

    def eliminar_receta(self, nombre_receta, ventana):
        del self.recetas[nombre_receta]
        ventana.destroy()
        self.actualizar_recetas()

if __name__ == "__main__":
    ventana = tk.Tk()
    app = Recetario(ventana)
    ventana.mainloop()
