# Prototipo

EnviApp

V: Beta

# Nueva tarea
Agregar contador en 1 por cotizacion cada que se realiza una captura
cuando se presiona el boton de agregar el contador pasa a 0
cuando el contador esta en 0 el boton desaparece

task:
analiza la funcion nde agregar cotizacion

process: 
nueva ventana para agregar un producto
colocar info y presionar boton  de continuar
al ñpresionar continuar el toplevel obtiene y retorna la informacion a la pagina principal
la pagina principal llama a agregar uin producto a la lista con esa informacion

## Seguridad 
Usar la libreria bcrypt para las contraseñas

#### Nota
Pensar en como cancelar una venta y como afecta a los datos.

Agregar total de venta diaria   (LISTO)

### librerias

Instalación de pytesseract: https://github.com/UB-Mannheim/tesseract/wiki

## advertencia

error: [ WARN:0@0.675] global shadow_sift.hpp:15 cv::xfeatures2d::SIFT_create DEPRECAs://github.com/PRECATED: cv.xfeatures2d.SIFT_create() is deprecated due SIFT tranfer to ain r
the main repository. https://github.com/opencv/opencv/issues/16736 

Resumen: Es posible que en otras versiones de openCV deje de funcionar la funcion xfeatures2d por lo que es necesario tomarlo en cuenta para las proximas versiones de la aplicacion