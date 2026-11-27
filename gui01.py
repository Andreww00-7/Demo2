import tkinter as tk           # Importa la libreria tkindedr y le asigna el alias tk
from tkinter import messagebox, ttk # Importa messagebox y ttk desde tkinder para cuadros de dialogo y widgets tematicos 

# Crear la ventana principal
ventana = tk.Tk() # Crea la ventana principal de la aplicacion
ventana.title("Mi primera aplicacion")
ventana.geometry("350x200") # Define el tamaño y posicion inicial de la ventana


def saludar(): 
    messagebox.showinfo("Saludo", "¡Bienvenido a python!") # Define tamaño y posicion inicial de la ventana

# Crea una etiqueta que muestra un texto.
etiqueta = ttk.Label(
    ventana,
    text="Aprendiendo Tkinter"
)
etiqueta.pack(pady=20)

# Crea un boton interactivo.
boton = ttk.Button(
    ventana,
    text="Saludar",
    command=saludar  # Relaciona el boton con la funcion saludar.
)
boton.pack(pady=10)

# Mantener la Ventana abierta 
ventana.mainloop()  # Inicia el ciclo de eventos para que la aplicacion responda a las interacciones del usuario.
