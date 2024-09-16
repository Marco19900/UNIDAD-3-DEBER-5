# creacion de una aplicacion GUI basica
import tkinter as tk  # Importa Tkinter para la interfaz gráfica
from tkinter import messagebox  # Importa messagebox para mostrar mensajes

# Función para agregar texto a la lista
def agregar():
    # Obtiene el texto del campo de entrada
    item = entry.get()
    # Si el campo no está vacío, lo agrega a la lista
    if item:
        lista.insert(tk.END, item)
        # Limpia el campo de entrada después de agregar
        entry.delete(0, tk.END)

# Función para limpiar todos los elementos de la lista
def limpiar():
    lista.delete(0, tk.END)

# Función para manejar el evento de presionar "Enter"
def on_enter(event):
    agregar()  # Llama a la función agregar cuando se presiona "Enter"

# Función para manejar el clic en un elemento de la lista
def on_lista_click(event):
    seleccion = lista.curselection()  # Obtiene el índice del elemento seleccionado
    if seleccion:
        item = lista.get(seleccion[0])  # Obtiene el texto del elemento seleccionado
        messagebox.showinfo("Elemento Seleccionado", f"Seleccionaste: {item}")  # Muestra el texto en un mensaje

# Configuración de la ventana principal
ventana = tk.Tk()  # Crea la ventana principal
ventana.title("Aplicación GUI Básica")  # Título de la ventana

# Etiqueta para indicar al usuario qué hacer
etiqueta = tk.Label(ventana, text="Ingrese información:")
etiqueta.pack(pady=10)  # Agrega la etiqueta con un espacio alrededor

# Campo de texto para ingresar datos
entry = tk.Entry(ventana, width=50)
entry.pack(pady=5)  # Agrega el campo de texto con un espacio alrededor

# Botón para agregar datos
btn_agregar = tk.Button(ventana, text="Agregar", command=agregar)
btn_agregar.pack(side=tk.LEFT, padx=10)  # Agrega el botón con un espacio a la izquierda

# Botón para limpiar la lista
btn_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
btn_limpiar.pack(side=tk.LEFT, padx=10)  # Agrega el botón con un espacio a la izquierda

# Lista para mostrar los datos agregados
lista = tk.Listbox(ventana, width=50, height=10)
lista.pack(pady=10)  # Agrega la lista con un espacio alrededor

# Asocia el evento de presionar "Enter" con la función on_enter
entry.bind("<Return>", on_enter)

# Asocia el clic en la lista con la función on_lista_click
lista.bind("<ButtonRelease-1>", on_lista_click)

# Ejecuta la aplicación
ventana.mainloop()