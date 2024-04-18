"""
description: Organizador de registros JSON Y CSV
Author: Ethan Yahel Sarricolea Cortés
"""

import csv
from bin import clock
import os

class CSVRegister:
    def __init__(self) -> None:
        pass

    def leer_csv(archivo):
        #with open(archivo,mode="r",newline='') as archivoHoy:
            archivoHoy = open(archivo,mode="r",newline='')
            lector_csv = csv.reader(archivoHoy)
            data = [archivoHoy,lector_csv]
            return data
        
    def leer_database(self):
        ruta = "db"
        return os.listdir(ruta)

    def ubicar_archivo(self,name):
        return (True if os.path.exists(name) else False)

    def crear_csv(self,date,contenido):
        nombre_archivo = "db/"+date +".csv"
        status = self.ubicar_archivo(nombre_archivo)
        if status:
            with open(str(nombre_archivo), 'a+') as archivo:
                contenido = "\n"+contenido
                archivo.write(contenido)    # contenido se remplazara por la info
        else:
            with open(str(nombre_archivo), 'w+') as archivo:
                archivo.write(contenido)

class JSONRegister:
    def __init__(self) -> None:
        pass

"""
fecha = clock.Clock()
date = fecha.data()
creador = CSVRegister()
creador.crear_csv(date,"Nombre,tiempo,precio,final")
lolo = creador.leer_database()
print(lolo)
#"""

