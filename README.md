# EnviApp Beta

## Actualizacion
                    
- Se corrigen las cotizaciones erroneas y al finalizar se muestran solo las de venta```
- Las cotizaciones se calculan de acorde al peso y tipo de envio

**Notas**: 
# Esto es mientras no se este en la otra computadora
            self.listaCotizador.addCotizacion("","","",153.12)
            self.listaCotizador.addCotizacion("J&T","Terrestre","5 Dia(s) aprox.","78.43")
            self.listaCotizador.addCotizacion("REDPACK","Ecoespress","5 Dia(s) aprox.","95.47")
            self.listaCotizador.addCotizacion("UPS","UPS Standard","1 Dia(s) aprox.","125.32")
            self.listaCotizador.addCotizacion("FEDEX","Express Saver","5 Dia(s) aprox.","132.98")
            self.listaCotizador.addCotizacion("REDPACK","Express","1 Dia(s) aprox.","151.42")
            self.listaCotizador.addCotizacion("PAQUETEEXPRESS","Estandar","5 Dia(s) aprox.","172.56")
            self.listaCotizador.addCotizacion("DHL","Economy Select Domestic","5 Dia(s) aprox.","178.10")
            self.listaCotizador.addCotizacion("FEDEX","Standard Overnight","1 Dia(s) aprox.","213.15")
            self.listaCotizador.addCotizacion("UPS","UPS World Wide Saver","5 Dia(s) aprox.","247.66")
            data = self.listaCotizador.generarLista()

## Consideraciones:

Error de ejecucion: [ WARN:0@0.675] global shadow_sift.hpp:15 cv::xfeatures2d::SIFT_create DEPRECAs://github.com/PRECATED: cv.xfeatures2d.SIFT_create() is deprecated due SIFT tranfer to ain r
the main repository. https://github.com/opencv/opencv/issues/16736 

```Es posible que en otras versiones de openCV deje de funcionar la funcion xfeatures2d por lo que es necesario tomarlo en cuenta para las proximas versiones de la aplicacion```

# Instalación

1. Se clona el repositorio.

    `git clone https://github.com/Ethan-Sarricolea/envia_app.git`

2. Se desplaza a la carpeta clonada 

    `cd envia_app`

3. Se crea el ejecutable de la app.

    `pyinstaller --onefile --windowed --icon=src\images\icono.ico EnviApp.py`

# Dependencias:

* Python instalado (3.11.9 utilizado en la creacion)
* pyautogui
* win32api
* time
* datetime
* cv2
* pytesseract
    ```Instalación de pytesseract: https://github.com/UB-Mannheim/tesseract/wiki```
* re
* csv
* os
* json
* tkinter
* bcrypt
* subprocess