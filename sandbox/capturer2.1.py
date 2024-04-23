import cv2
import numpy as np
from PIL import ImageGrab

# 67% de zoom

import time

time.sleep(5)

def encontrar_area_similar(imagen_referencia, captura_pantalla):
    # Convertir la captura de pantalla de RGB a BGR
    captura_pantalla = cv2.cvtColor(captura_pantalla, cv2.COLOR_RGB2BGR)

    # Convertir las imágenes a escala de grises
    referencia_gris = cv2.cvtColor(imagen_referencia, cv2.COLOR_BGR2GRAY)
    captura_pantalla_gris = cv2.cvtColor(captura_pantalla, cv2.COLOR_BGR2GRAY)

    # Realizar coincidencia de plantillas
    resultado = cv2.matchTemplate(captura_pantalla_gris, referencia_gris, cv2.TM_CCOEFF_NORMED)

    # Obtener la posición de la mejor coincidencia
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

    # Obtener las dimensiones de la imagen de referencia
    ancho_referencia, alto_referencia = imagen_referencia.shape[1], imagen_referencia.shape[0]

    # Obtener las coordenadas del área más parecida a la imagen de referencia
    x, y = max_loc
    x2, y2 = x + ancho_referencia, y + alto_referencia

    # Devolver el área encontrada
    return captura_pantalla[y:y2, x:x2]

def capturar_area():
    # Cargar la imagen de referencia
    imagen_referencia = cv2.imread('src\images\GUIA.jpg')

    # Capturar la pantalla
    captura_pantalla = np.array(ImageGrab.grab())

    # Encontrar el área más similar a la imagen de referencia
    area_similar = encontrar_area_similar(imagen_referencia, captura_pantalla)

    # Guardar el área encontrada como una nueva imagen
    cv2.imwrite('area_similar.png', area_similar)

"""# Mostrar la captura de pantalla con el área similar resaltada
cv2.imshow('Captura de pantalla con área similar', area_similar)
cv2.waitKey(0)
cv2.destroyAllWindows()"""
