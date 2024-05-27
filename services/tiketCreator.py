"""
Description: Creacion de tiket en formato txt / proximamente a pdf tambien
Author: Ethan Yahel Sarricolea Cortés
"""

#from reportlab.lib.pagesizes import letter
#from reportlab.pdfgen import canvas
#from PyPDF2 import PdfReader, PdfWriter
from services import clock
import subprocess

class Printer:
    def __init__(self) -> None:
        self.reloj = clock.Clock()
        self.data = ""
        self.date_time = ""
        self.info = ""

    def create_ticket(self,venta,colaborator,guide):
        filename = r"src\tikets\ticket.pdf"
        self.data = self.reloj.data().replace("-","/")
        self.date_time = f"{self.data}, {self.reloj.hour()}"
        # Formato de tiket
        self.info = f"""
--------------------------------

            ENVIA
            
--------------------------------

Punto de venta: ENVIA LAS PALMAS
Fecha y hora: {self.date_time}
Lugar: ENVIA, EL PALMAR AV. LAS PALMAS 101 LOC 32 COATZACOALCOS, VERACRUZ



Compañia: {venta["name"]}
Tipo de envio: {venta["tipo"]}
Tiempo de espera: {venta["time"]}
Precio: ${venta["final"]}



Asesor: {colaborator}
Número de guia: {guide}


--------------------------------

    ¡Gracias por tu compra!

--------------------------------
""" 
        txtpath = filename.replace(".pdf",".txt")
        txt = open(txtpath,"w+")
        txt.write(self.info)
        txt.close()
        subprocess.Popen(["notepad.exe", txtpath])