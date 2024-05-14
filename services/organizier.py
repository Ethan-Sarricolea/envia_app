"""
description: Organizador de registros JSON Y CSV
Author: Ethan Yahel Sarricolea Cortés
"""

import csv
import os
import json
from bin import clock

class Register:
    def __init__(self) -> None:
        self.fecha = clock.Clock()
        self.data_json = {
            "name":"",
            "tipo":"",
            "time":"",
            "price":0,
            "utilidad":0,
            "final":0}
        self.lectura = None

    def leer_csv(archivo):
        #leer contenido de archivo csv
        archivoHoy = open(archivo,mode="r",newline='')
        lector_csv = csv.reader(archivoHoy)
        data = [archivoHoy,lector_csv]
        return data
        
    def leer_database(self):
        # Leer y enlistar archvios csv en db
        ruta = "db"
        datos = os.listdir(ruta)
        del datos[-1]
        return datos

    def ubicar_archivo(self,name):
        # Encontrar un archivo
        return (True if os.path.exists(name) else False)

    def create_csv(self,contenido):
        # Agregar dato o crear y agregar dato a archivo csv
        self.nombre_archivo = "db/"+(self.fecha.data())+".csv"
        status = self.ubicar_archivo(self.nombre_archivo)
        if status:
            with open(str(self.nombre_archivo), 'a+') as archivo:
                contenido = "\n"+contenido
                archivo.write(contenido)    # contenido se remplazara por la info
        else:
            with open(str(self.nombre_archivo), 'w+') as archivo:
                archivo.write(contenido)

    def writeJson(self,name,tipo,time,price,utilidad,final):
        # Colocar cotizacion en archivo de configuracion
        self.data_json["name"] = name
        self.data_json["tipo"] = tipo
        self.data_json["time"] = time
        self.data_json["price"]= price
        self.data_json["utilidad"]=utilidad
        self.data_json["final"]=final
        with open("db\lastRegis.json","w") as jsonFile:
            json.dump(self.data_json,jsonFile)

    def readJson(self):
        # Leer archivo de configuracion
        with open("db\lastRegis.json","r") as jsonFile:
            data = json.load(jsonFile)
        return data

    def jsonToList(self,data):
        # Obtener un arreglo de la informacion de JSON
        lista = f"{data['name']},{data['tipo']},{data['time']},{data['price']},{data['utilidad']},{data['final']}"
        return lista

    def add_venta(self):
        # Agregar una venta al archivo CSV 
        self.create_csv(self.fecha.data(),self.jsonToList(self.readJson()))

    def cancel_venta(self):
        # Eliminar datos del json
        self.data_json["name"] = ""
        self.data_json["tipo"] = ""
        self.data_json["time"] = ""
        self.data_json["price"]= ""
        self.data_json["utilidad"]=""
        self.data_json["final"]=""
        with open("db\lastRegis.json","w") as jsonFile:
            json.dump(self.data_json,jsonFile)
        # Abrir el archivo CSV en modo de lectura y escritura
        with open(f'{self.nombre_archivo}.csv', 'r+', newline='') as archivo:
            # Leer el contenido del archivo CSV
            lector_csv = csv.reader(archivo)
            filas = list(lector_csv)
            # Eliminar la última fila
            filas.pop()
            # Volver al inicio del archivo
            archivo.seek(0)
            # Escribir el contenido actualizado en el archivo CSV
            escritor_csv = csv.writer(archivo)
            for fila in filas:
                escritor_csv.writerow(fila)
            # Truncar el archivo para eliminar cualquier contenido restante
            archivo.truncate()

#
"""
jsoner = Register()
#jsoner.writeJson("Estafeta","terrestre","1 dias aprox.",500,50,550)
jsoner.add_venta()
from bin import clock
fecha = clock.Clock()
date = fecha.data()
creador = CSVRegister()
creador.crear_csv(date,"Nombre,tiempo,precio,final")
lolo = creador.leer_database()
print(lolo)

#"""