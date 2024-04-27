"""
Description: RECONOCIMIENTO OPTICO DE CARACTERES
Author: Ethan Yahel Sarricolea Cortés

Nota: La ruta se debe cambiar por la de tesseract en el usuario

"""

import cv2
import pytesseract
import re
from bin import comparador
#import comparador

class REOPC:
    def __init__(self) -> None:
        self.comparator = comparador.IMGcomaparator()
        # Especificar la ruta al ejecutable de Tesseract
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        self.priceList = ["c","C","r","e","a","r","n","v","i","o","w",
                          "x",">","m","\n","t","s","p","M","G","?","u"]
        self.daysList = ["@","}",")"]
        self.dias5 = ["S","5"]
        self.dias5mas = ["Sr","5+"]
        self.dias1 = ["A","L","a","d","1"]
        self.dias2 = ["2"]
        self.dias3 = ["3"]
        self.dias4 = ["4"]

    def convert(self,img):
        # Cargar imagen img = cv2.imread("screenshot.jpg")
        img = cv2.imread(img)
        # Convierte la imagen a escala de grises
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Aplicar umbral para convertir a imagen binaria
        threshold_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        # Pasa la imagen por pytesseract
        text = pytesseract.image_to_string(threshold_img)
        # Imprimir el texto extraído
        return(text)
    
    def recibe_precio(self,imagen):
        # convierte la imagen, remplaza los espacios y caracteres extra, elimina comas extra y retorna una lista
        newtext = self.convert(imagen)
        newtext = newtext.replace(" ","")
        for letter in self.priceList:
            newtext = newtext.replace(letter,"")
        newtext = re.sub(r',{3}(.+?),{3}', r',\1,', newtext)
        newtext = newtext.replace("$","")
        #final = newtext[1:].split(",")
        #final = filter(None,final)
        return newtext #final
    
    def correcion_tiempo(self,texto):
        # corrige las palabras mal detectadas a las palabras que deberian ser
        if texto[0] in self.dias5:
            texto = "5 Dia(s) aprox."
            if texto[:2] in self.dias5mas:
                texto = "5+ Dia(s) aprox."
        elif texto[0] in self.dias4:
            texto = "4 Dia(s) aprox."
        elif texto[0] in self.dias3:
            texto = "3 Dia(s) aprox."
        elif texto[0] in self.dias2:
            texto = "2 Dia(s) aprox."
        elif texto[0] in self.dias1:
           texto = "1 Dia aprox."
        return texto

    def recibe_tiempo(self,imagen):
        # convierte la imagen, elimina caracteres extra y salto de linea y elimina datos vacios
        newtext = self.convert(imagen)
        newtext = newtext.replace("\n","")
        """print(newtext)
        for letter in self.daysList:
            newtext = newtext.replace(letter,"")
        """
        return self.correcion_tiempo(newtext) #newtext

    def recibe_tipo(self,imagen):
        # Falta correccion / por alguna razon no lee el texto
        newtext = self.convert(imagen)
        newtext = newtext.replace("\n","")
        """
        newtext = re.sub(r",{2}([a-zA-Z0-9\s]+),{2}",r",\1,",newtext)
        #newtext.pop(0)
        #newtext = filter(None,newtext)"""
        return newtext
    
    def recibe(self,imagen="",opcion=0):
        if opcion==0:
            #Logo
            logo = self.comparator.comparacion(imagen)
            return logo
        elif opcion==1:
            return self.recibe_tipo(imagen)
        elif opcion==2:
            return self.recibe_tiempo(imagen)
        elif opcion==3:
            pass
        elif opcion==4:
            return self.recibe_precio(imagen)

"""lala = REOPC()
helloWorld = [lala.recibe(r'src\screenshots\screenshot0.jpg',0),#LOGo
              lala.recibe(r"src\screenshots\screenshot1.jpg",1),#Tipo
              lala.recibe(r"src\screenshots\screenshot2.jpg",2),# tiempo
              lala.recibe(r'src\screenshots\screenshot4.jpg',4)]# precio
print(helloWorld)"""

# Error con shape del comparador (averigualo)