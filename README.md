# Prototipo

## Notas personales

identificar el funcionamiento de texto de tesseract

## Objetivos

### Listo
- archivo que saque imagenes
- Identificar si se debe dividir la imagen en partes
- agregar a csv
- precios en ocr
- tiempo en ocr (a medias)

### pendiente

AHORA SOLO FUNCIONA EL PRECIO

- tipos de envio en ocr
- compañias en ocr (Considera usar otro metodo de comparación para asegurar que se detecten todas las compañias)
    idea: guardar los logos de compañias y detectar cuando aparecen en la ss
- Conseguir capturas de 3, 2 y 4 dias de manuable

- Obtener el texto de la pagina (Las imagenes)
- Pasar el texto a json
- Mostrar datos del json en pantalla
- pasar informacion de json a tiket
- Agregar creacion e impresion de tiket (informacion de manuable / cotizacion)

### Observaciones de OCR

columna 1 errores (compañias) Nota: recortar los logos por imagen?? / descargar los logos de las compañias en escala de grises.

Columna 2 MUY BIEn (Tipo de envio) Nota: minimos errores ortograficos.

columna 3 mas o menos (dias) Nota: Las S significan 5, las A,L,I significan 1.

columna 4 mas o menos (Es irrelevante)

columna 5 MUY BIEN (precios) Nota: aparecen otras letras, este algoritmo debe detectar los $ y tomar hasta 2 caracteres despues del punto.

# Problemas por resolver y mas notas

En la captura no aparecen todas las cotizaciones

agregar la opcion de hacer otra captura y que en esta se vean las demas paqueterias

preguntar que paqueterias si se usan

si las paqueterias con limitadas se puede hacer que solo se identificquen estas

hacer una lista de objetos (cotizaciones) y que si los datos de la cotizacion son exactamente los mismos se omita agregarla, asi se podran hacer mas capturas en caso de faktar cotizaciones importantes

la lista de objetos se agregara al json y esta al terminarse la compra identificara la seleccionada y se pasara al csv de registro

el csv de registro llevara la fecha y hora en que fue creado

# Nota pdf

agregar opcion de configuracion donde se cree una lista de colaboradores, asi al crear el tiket el colaborador solo seleccionara su nombre en lugar de escribirlo


MEjorar el sistema de impresion