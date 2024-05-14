"""
Capturador de imagen

Capturar la pantalla
Se debe dividir la captura en partes diferentes y en base a su numero
sera la informacion que se manda al OCR

Esta funcion se llamara desde el UI y retornara los path de las imagenes
Ui llamara al OCR con los path recibidos para el analisis y esos

"""

import pyautogui
import win32api
import time
from bin import OCR

class Capturer:
    def __init__(self) -> None:
        self.ocr = OCR.REOPC()
        self.ancho = win32api.GetSystemMetrics(0)
        self.alto = win32api.GetSystemMetrics(1)
        self.xin = 340
        self.yin = 147
        self.columnCoord = [150,430,370,230,400]
        self.ylimit = 1000
        self.xlimit = 1770
        self.rowSize = 86
        
    def screnshot_desk(self,x1,y1,x2,y2,numero):
        # Toma y recorta la captura
        screenshot = pyautogui.screenshot()
        screenshot = screenshot.crop((x1,y1,x2,y2))
        # Guarda 
        screenshot.save(f'src\screenshots\screenshot{numero}.jpg')
        # También puedes mostrar la captura de pantalla en una ventana emergente
        #screenshot.show()

    def manuable_scan(self,cotizador):
        # Captura una fraccion de la pantalla y llama la identificacion OCR
        self.cotiz = cotizador
        x = self.xin
        self.actualCot = []
        #Cambia el 200 por self.ylimit
        for row in range(self.yin,self.ylimit,self.rowSize):
            x = self.xin
            cot = True
            for i in range(0,5,1):
                if x==1290:
                    x += self.columnCoord[i]
                    self.actualCot.append("")
                    continue
                else:
                    self.screnshot_desk(x1=x,y1=row,x2=x+self.columnCoord[i],y2=row+self.rowSize,numero=i)
                    x += self.columnCoord[i]
                    #Llamada a OCR con el numero de opcion
                    dato = self.ocr.recibe(imagen=f'src\screenshots\screenshot{i}.jpg',opcion=i)
                    # Si la primera ves que se hace la identificacion retorna falso se pasa a la sig fila
                    self.actualCot.append(dato)
                time.sleep(0.1)
            if self.actualCot[0]==False and self.actualCot[1]=="" and self.actualCot[2]=="" or self.actualCot[4]=="":
                pass
            else:
                self.cotiz.addCotizacion(name=self.actualCot[0],tipo=self.actualCot[1],
                                        tiempo=self.actualCot[2],precio=self.actualCot[4])
            self.actualCot.clear()
        return self.cotiz.generarLista()

#
"""
import OCR
time.sleep(3)
camara = Capturer()
camara.manuable_scan()
#camara.screnshot(number="X",y=camara.row*5,x=camara.column)
#"""