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

class Capturer:
    def __init__(self) -> None:
        self.ancho = win32api.GetSystemMetrics(0)
        self.alto = win32api.GetSystemMetrics(1)
        self.row,self.column = self.alto/12,self.ancho/6
        self.coords = [1,2,3,5]
        
    def screnshot(self,number,x=0,y=0):
        # Toma una captura de pantalla del escritorio
        screenshot = pyautogui.screenshot()
        #Recorta la captura
        screenshot = screenshot.crop((x, y, x+self.column, self.alto-(self.row*0.48)))
        # Guarda la captura de pantalla en un archivo
        screenshot.save(f'src\screenshots\screenshot{number}.jpg')
        # También puedes mostrar la captura de pantalla en una ventana emergente
        #screenshot.show()

    def manuable_scan(self):
        for i in self.coords:
            self.screnshot(number=i,y=self.row*5.1,x=self.column*i)

#
"""
import time
time.sleep(3)
camara = Capturer()
camara.manuable_scan()
#camara.screnshot(number="X",y=camara.row*5,x=camara.column)
#"""