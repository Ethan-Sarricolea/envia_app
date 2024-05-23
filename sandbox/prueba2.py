import tkinter as tk
from tkinter import ttk

# Función para mostrar los datos actuales de la fila seleccionada
def show_selected_row():
    selected_item = tree.selection()[0]  # Obtener la fila seleccionada
    values = tree.item(selected_item, 'values')  # Obtener los valores actuales de la fila seleccionada
    
    # Mostrar los valores actuales en las entradas
    entry1.delete(0, tk.END)
    entry1.insert(0, values[0])
    entry2.delete(0, tk.END)
    entry2.insert(0, values[1])

# Función para actualizar la fila seleccionada
def update_row():
    selected_item = tree.selection()[0]  # Obtener la fila seleccionada
    new_value1 = entry1.get()
    new_value2 = entry2.get()
    
    # Actualizar los valores en la fuente de datos
    data[selected_item] = (new_value1, new_value2)
    
    # Actualizar la fila en el Treeview
    tree.item(selected_item, values=(new_value1, new_value2))

# Configuración de la ventana principal
root = tk.Tk()
root.title("Treeview Example")

# Crear el Treeview
columns = ("Column 1", "Column 2")
tree = ttk.Treeview(root, columns=columns, show='headings')
tree.heading("Column 1", text="Column 1")
tree.heading("Column 2", text="Column 2")

# Datos iniciales
data = {
    "item1": ("Value 1.1", "Value 1.2"),
    "item2": ("Value 2.1", "Value 2.2")
}

# Insertar los datos en el Treeview
for key, values in data.items():
    tree.insert("", "end", iid=key, values=values)

tree.pack()

# Entradas para modificar datos
entry1 = tk.Entry(root)
entry1.pack()
entry2 = tk.Entry(root)
entry2.pack()

# Botón para mostrar los datos de la fila seleccionada
select_button = tk.Button(root, text="Seleccionar Fila", command=show_selected_row)
select_button.pack()

# Botón para actualizar la fila seleccionada
update_button = tk.Button(root, text="Actualizar Fila", command=update_row)
update_button.pack()

root.mainloop()
