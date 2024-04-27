import subprocess

def abrir_en_bloc_de_notas(archivo):
    subprocess.Popen(["notepad.exe", archivo])

# Llamar a la función para abrir el archivo en Bloc de notas
abrir_en_bloc_de_notas(r"src\tikets\ticket.txt")
