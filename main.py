"""
Autor: Sarricolea Cortés Ethan Yahel
Description: inicializador de aplicación
"""

from ui import UI

try:
    app = UI.App()
    app.run()
    
except Exception as e:
    print(f"Error type: {e}")
    
    #messagebox.showerror("Ha ocurrido un error",f"Error type: {e}")