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

    # Establecer el modo de mapa y las unidades
    hdc.SetMapMode(win32con.MM_TWIPS)  # Establecer las unidades a TWIPS (1 TWIP = 1/20 de punto)
    margen_izquierdo = 56.693  # 1 milímetro en TWIPS (25.4 TWIPS = 1 milímetro)
    margen_superior = 56.693
    hdc.SetViewportOrg((int(margen_izquierdo), int(margen_superior)))  # Establecer el origen del viewport

    # Establecer el tamaño de la fuente
    #hdc.SetTextColor(win32con.BLACK)
    hdc.SetTextAlign(win32con.TA_BASELINE | win32con.TA_LEFT | win32con.TA_NOUPDATECP)
    font = win32ui.CreateFont({
        "name": "Arial",
        "height": -100,  # Tamaño de la fuente en puntos (negativo para especificar el tamaño en puntos)
        "weight": 400,
    })
    hdc.SelectObject(font)

    # Definir posición inicial
    x, y = 0, 0

    # Definir desplazamiento vertical entre líneas
    desplazamiento_vertical = 150

    # Abrir el archivo y leer e imprimir línea por línea
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            hdc.TextOut(x, y, linea)
            # Incrementar la posición vertical para la próxima línea
            y += desplazamiento_vertical  # Ajustar este valor según sea necesario

    hdc.EndPage()
    hdc.EndDoc()

    # Cerrar la impresora
    win32print.ClosePrinter(hprinter)

imprimir_archivo(r"src\tikets\ticket.txt")
