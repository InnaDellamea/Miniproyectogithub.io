import tkinter as tk
from tkinter import Scrollbar, Text

# Función para cerrar la ventana
def cerrar_ventana():
    ventana.destroy()

# Crear la ventana principal
ventana = tk.Tk()
ventana.geometry("670x700")
ventana.title("Acerca de")

# Crear un Frame para el texto con scroll
frame_texto = tk.Frame(ventana)
frame_texto.place(relx=0.5, rely=0.5, anchor='center')  # Posiciona el Frame en el centro

# Crear un Text con Scrollbar
scrollbar = Scrollbar(frame_texto)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

texto = Text(frame_texto, height=25, width=70, wrap=tk.WORD, yscrollcommand=scrollbar.set)
texto.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=texto.yview)

# Agregar un texto de ejemplo
texto.insert(tk.END, """Somos COWORKING, una empresa joven y dinámica dedicada al desarrollo web, compuesta por un talentoso equipo de estudiantes del Informatorio, quienes representan las nuevas promesas en la industria de la programación.

Nuestro Equipo
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

Gracias por confiar en COWORKING.
Estamos emocionados de llevar sus proyectos al siguiente nivel con nuestra pasión y habilidades en desarrollo web. ¡Juntos, construiremos el futuro digital!""")
texto.config(font=("arial", 11), state=tk.DISABLED)

# Boton Volver (cierra la ventana)
btn_cerrar = tk.Button(ventana, text="Volver", command=cerrar_ventana)
btn_cerrar.place(relx=0.8, rely=0.9, anchor='center')  # Posiciona el botón en la parte inferior derecha

ventana.mainloop()
