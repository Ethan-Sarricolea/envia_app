import tkinter as tk
from tkinter import ttk

def mostrar_tabla(data):
    # Crear ventana
    ventana = tk.Tk()
    ventana.title("Tabla de datos")

    # Crear Treeview
    tree = ttk.Treeview(ventana)
    tree["columns"] = ("#1", "#2", "#3")  # Define las columnas de la tabla
    tree.heading("#1", text="Columna 1")
    tree.heading("#2", text="Columna 2")
    tree.heading("#3", text="Columna 3")

    # Agregar datos a la tabla
    for fila in data:
        tree.insert("", "end", values=tuple(fila))

    # Mostrar Treeview
    tree.pack(expand=True, fill="both")

    ventana.mainloop()

# Datos de ejemplo (lista bidimensional)
datos = [
    ["Dato 1", "Dato 2", "Dato 3"],
    ["Dato 4", "Dato 5", "Dato 6"],
    ["Dato 7", "Dato 8", "Dato 9"]
]

# Mostrar la tabla con los datos
mostrar_tabla(datos)
