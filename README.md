# Prototipo

EnviApp

## Notas personales

identificar el funcionamiento de texto de tesseract

# Objetivo a corto plazo

evitar que aparezca el archivo json en venta diaria
reseteo de lista de cotizaziones !!!!!!!
Limpieza de entrys

## Objetivos

# nuevos
Crear un capturador / recortador de pantalla y usarlo para detectar el texto

Objetivo:
    Ajustar proceso de que hacer en caso de no detectar un logo
    una ves que se tome los datos de cotizacion que estos se organizcen con la lista de cotizaciones.py
    de cotizaciones pasan a la tabla de del UI
    una ves seleccionado y presionado vender en el UI, se obtienen los datos de la tabla y se introducen al json
    Ya en el json y en la pestaña de forms se confirman los datos o se corrigen
    al confirmar la venta se pasan los datos del json al csv y al creador de tikets
    el creador de tikets imprime el tiket
    añadir seguridad a los registros


## Seguridad 
Usar la libreria bcrypt para las contraseñas

#### Nota
Pensar en como cancelar una venta y como afecta a los datos.

### librerias

Instalación de pytesseract: https://github.com/UB-Mannheim/tesseract/wiki

## advertencia

error: [ WARN:0@0.675] global shadow_sift.hpp:15 cv::xfeatures2d::SIFT_create DEPRECAs://github.com/PRECATED: cv.xfeatures2d.SIFT_create() is deprecated due SIFT tranfer to ain r
the main repository. https://github.com/opencv/opencv/issues/16736 

Resumen: Es posible que en otras versiones de openCV deje de funcionar la funcion xfeatures2d por lo que es necesario tomarlo en cuenta para las proximas versiones de la aplicacion