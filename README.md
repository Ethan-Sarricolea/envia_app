# EnviApp Beta

## Actualizacion
                    
- Se corrigen las cotizaciones erroneas y al finalizar se muestran solo las de venta```
- Las cotizaciones se calculan de acorde al peso y tipo de envio

## Consideraciones:

Error de ejecucion: [ WARN:0@0.675] global shadow_sift.hpp:15 cv::xfeatures2d::SIFT_create DEPRECAs://github.com/PRECATED: cv.xfeatures2d.SIFT_create() is deprecated due SIFT tranfer to ain r
the main repository. https://github.com/opencv/opencv/issues/16736 

```Es posible que en otras versiones de openCV deje de funcionar la funcion xfeatures2d por lo que es necesario tomarlo en cuenta para las proximas versiones de la aplicacion```

# Instalación

0. Instalar python desde microsoft: 

    `https://www.microsoft.com/store/productId/9NRWMJP3717K?ocid=pdpshare`

1. Ejecutar el instalador:

    `installer.py`

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

###### Palabra clave: ENVIAPP_ENV_VAR