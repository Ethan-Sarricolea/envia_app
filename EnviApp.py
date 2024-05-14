"""
Description: Codigo para convertir a ejecutable de la app
Author: Sarricolea Cortés Ethan Yahel
"""

import subprocess

# Ruta al archivo secundario que deseas ejecutar
archivo_secundario = "main.py"

# Comando para ejecutar el archivo secundario con Python
comando = ["python", archivo_secundario]

# Ejecutar el comando
subprocess.run(comando)
