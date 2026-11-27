import tkinter as tk  # Importar las herramientas graficas y le asigna el alias tk

ventana = tk.Tk()     # Crear una sola ventana raiz
ventana.title("Mi primera ventana")   # Texto de la barra de titulo
ventana.geometry("400x220")     # Ancho de 400 y alto de 220 pixeles
ventana.resizable(True, True)  # Permitir cambiar el ancho, no el alto

ventana.mainloop()    # Atender clics y redibujados hasta cerrar
