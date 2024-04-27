"""
Creacion de tiket en formato pdf
Author = ethan Yahel Sarricolea Cortés
"""

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter
from bin import clock

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

Punto de venta: ENVIA
Fecha y hora: {self.date_time}
Lugar: ENVIA, EL PALMAR AV. LAS PALMAS 101 LOC X COATZACOALCOS, VERACRUZ



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

        #""" TIKET EN PDF
        c = canvas.Canvas(filename, pagesize=letter)
        c.drawImage("src\images\logo.jpg", 100, 500, width=400, height=200)  # Ajusta las coordenadas y el tamaño según sea necesario
        c.setFont("Helvetica", 12)
        textobject = c.beginText(100, 500)
        textobject.textLines(self.info)
        c.drawText(textobject)

        c.showPage()
        c.save()
        #"""

    def resize_pdf(self,input_filename, output_filename, width, height):
        input_pdf = PdfReader(input_filename)
        output_pdf = PdfWriter()

        for page in input_pdf.pages:
            page.mediabox.lower_Left = (0, 0)
            page.mediabox.upper_Right = (width, height)
            output_pdf.add_page(page)

        with open(output_filename, 'wb') as f:
            output_pdf.write(f)

#
""" Generar el ticket en PDF
impresora = Printer()
impresora.create_ticket(,kg=1,colaborator="paquito",guide=12345)

# Ajustar el tamaño del PDF al tamaño de los tickets físicos (por ejemplo, 2" x 5.5")
impresora.resize_pdf(r"src\tikets\ticket.pdf", r"src\tikets\ticket.pdf", (2 * 72), (5.5 * 72))  # 1 pulgada = 72 puntos
#"""