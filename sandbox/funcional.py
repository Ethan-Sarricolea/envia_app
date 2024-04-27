import win32print
import win32ui
import win32con

def imprimir_archivo(nombre_archivo):
    # Inicializar la impresora predeterminada
    impresora = win32print.GetDefaultPrinter()

    # Crear un objeto de impresión
    hprinter = win32print.OpenPrinter(impresora)
    hdc = win32ui.CreateDC()
    hdc.CreatePrinterDC(impresora)

    # Configurar la impresión
    hdc.StartDoc(nombre_archivo)
    hdc.StartPage()

    # Definir posición inicial
    x, y = 0, 0

    # Abrir el archivo y leer e imprimir línea por línea
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            hdc.TextOut(x, y, linea)
            # Incrementar la posición vertical para la próxima línea
            y += 100  # Ajusta este valor según sea necesario

    hdc.EndPage()
    hdc.EndDoc()

    # Cerrar la impresora
    win32print.ClosePrinter(hprinter)

# Llamar a la función para imprimir un archivo de texto

imprimir_archivo(r"src\tikets\ticket.txt")
