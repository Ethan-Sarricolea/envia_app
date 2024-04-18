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
        
    def screnshot(self,x=0,y=0):
        # Toma una captura de pantalla del escritorio
        screenshot = pyautogui.screenshot()
        #Recorta la captura
        screenshot = screenshot.crop((x, y, x + self.ancho, y + self.alto))
        # Guarda la captura de pantalla en un archivo
        screenshot.save('screenshot.jpg')

        # También puedes mostrar la captura de pantalla en una ventana emergente
        screenshot.show()
