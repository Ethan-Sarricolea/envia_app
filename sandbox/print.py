import win32print

def imprimir_archivo(nombre_archivo, nombre_impresora):
    try:
        # Obtener una manija (handle) para la impresora
        impresora = win32print.OpenPrinter(nombre_impresora)
        
        # Iniciar una nueva tarea de impresión
        tarea = win32print.StartDocPrinter(impresora, 1, ("Test", None, "RAW"))
        
        # Iniciar una nueva página en la tarea de impresión
        win32print.StartPagePrinter(impresora)
        
        # Abrir el archivo en modo lectura
        with open(nombre_archivo, 'rb') as archivo:
            # Leer el contenido del archivo
            contenido = archivo.read()
            
            # Enviar el contenido del archivo a la impresora
            win32print.WritePrinter(impresora, contenido)
        
        # Finalizar la página de impresión
        win32print.EndPagePrinter(impresora)
        
        # Finalizar la tarea de impresión
        win32print.EndDocPrinter(impresora)
        
        print("Impresión completada exitosamente.")

    except Exception as e:
        print("Error al imprimir:", e)

# Especifica el nombre del archivo y el nombre de la impresora
nombre_archivo = r"C:\Users\personal\Desktop\App\code\envia_app\src\tikets\ticket.txt"
nombre_impresora = "POS-80"

# Llama a la función para imprimir el archivo en la impresora especificada
imprimir_archivo(nombre_archivo, nombre_impresora)

