"""
Description: RECONOCIMIENTO OPTICO DE CARACTERES
Author: Ethan Yahel Sarricolea Cortés

Nota: La ruta se debe cambiar por la de tesseract en el usuario

"""

import cv2
import pytesseract
import re


class REOPC:
    def __init__(self) -> None:
        # Especificar la ruta al ejecutable de Tesseract
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        self.priceList = ["c","C","r","e","a","r","n","v","i","o","w",
                          "x",">","m","\n","t","s","p","M","G","?"]
        self.daysList = ["@","}",")"]
        self.dias5 = ["S"]
        self.dias5mas = ["Sr"]
        self.dias1 = ["A","L","a","d"]
        self.dias2 = []
        self.dias3 = []

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
        newtext = newtext.replace(" ",",")
        for letter in self.priceList:
            newtext = newtext.replace(letter,"")
        newtext = re.sub(r',{3}(.+?),{3}', r',\1,', newtext)
        newtext = newtext.replace("$","")
        final = newtext[1:].split(",")
        i=0
        for data in final:
            if data=="" or data==None:
                final.pop(i)
            i+=1
        final = list(filter(None,final))
        return final
    
    def correcion_tiempo(self,lista):
        # corrige las palabras mal detectadas a las palabras que deberian ser
        for i in range(len(lista)):
            dato = lista[i]
            if dato[0] in self.dias5:
                lista[i] = "5 dia(s) aprox."
            if dato[:2] in self.dias5mas:
                lista[i] = "5+ dia(s) aprox."
            elif dato[0] in self.dias1:
                lista[i] = "1 dia(s) aprox."
        return lista

    def recibe_tiempo(self,imagen):
        # convierte la imagen, elimina caracteres extra y salto de linea y elimina datos vacios
        newtext = self.convert(imagen)
        print(newtext)
        for letter in self.daysList:
            newtext = newtext.replace(letter,"")
        newtext = newtext.split("\n")
        i=0
        for dato in newtext:
            if dato==" " or dato=="":
                newtext.pop(i)
            i+=1
        print(newtext)
        return self.correcion_tiempo(newtext)

    def recibe_tipo(self,imagen):
        # Falta correccion por alguna razon no lee el texto
        newtext = self.convert(imagen)
        newtext = newtext.replace("\n",",")
        newtext = re.sub(r",{2}([a-zA-Z0-9\s]+),{2}",r",\1,",newtext)
        newtext = newtext.split(",")
        newtext.pop(0)
        newtext = list(filter(None,newtext))
        return newtext

     
""" def trad_manuable(self):
        esta se llamara despues de sacar las capturas y traducira todo
    #lala = REOPC()
    algo = lala.recibe_tipo(r"src\screenshots\prueba.jpg")
    print(algo)
#"""