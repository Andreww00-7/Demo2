import tkinter as tk
from tkinter import ttk, messagebox 

ventana = tk.Tk()   # Instanciar la ventana principal 
ventana.title("saludo Interactivo")
ventana.geometry("360x180")

def saludar ():   # Funcion invocada cuando se hace clic 
    nombre = entrada.get().strip()  # Leer y quitar espacios extremos 
    if not nombre:   # Comprobar que exista un nombre 
        messagebox.showwarning("Dato Requerido", "Ingrese su nombre") # Mostrar mensaje de advertencia
        return # Detener el procesamiento si esta vacio
        messagebox.showinfo("Saludo", f"¡Hola, {nombre}!") # Mostrar mensaje de saludo 

ttk.Label(ventana, text="Nombre:").pack(pady=(16, 4)) # Etiqueta para el campo de entrada 
entrada = ttk.Entry(ventana) # campo de una linea 
entrada.pack(padx=20, fill="x") # Empaquetar con relleno horizontal y margen lateral
ttk.Button(ventana, text="Saludar", command=saludar).pack(pady=12) # Boton que invoca la funcion salufar al hacer 
ventana.mainloop() # Ejecutar interfaz 


    