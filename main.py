"""
Autor: Sarricolea Cortés Ethan Yahel
Description: iniciador de aplicación
"""

from ui import UI

try:
    app = UI.App()
    app.run()
    
except Exception as e:
    print(f"Error type: {e}")