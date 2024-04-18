"""
Description: Interfaz grafica de usuario
- Tabla de datos
- App
Author: Ethan Yahel Sarricolea Cortés
"""

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from bin import capturer
from bin import organizier

class TablaDatos:
    def __init__(self,app) -> None:
            # Crear Treeview    
        self.app = app
        self.tabla = ttk.Treeview(self.app.win)
        self.tabla["columns"] = ("1", "2", "3","4")  # Definir las columnas
        self.tabla.column("#0", width=200, minwidth=100, stretch=NO)  # Configurar la primera columna
        self.tabla.column("1", width=200, minwidth=100, stretch=NO)
        self.tabla.column("2", width=200, minwidth=100, stretch=NO)
        self.tabla.column("3", width=200, minwidth=100, stretch=NO)
        self.tabla.column("3", width=200, minwidth=100, stretch=NO)
        self.tabla.heading("#0", text="Nombre", anchor=W)  # Encabezado de la primera columna
        self.tabla.heading("1", text="Tiempo", anchor=W)  # Encabezado de la segunda columna
        self.tabla.heading("2", text="Precio", anchor=W)  # Encabezado de la tercera columna
        self.tabla.heading("3", text="Final", anchor=W)  # Encabezado de la cuarta columna
        self.tabla.heading("4", text="Utilidad", anchor=W)
        self.scrollbar = ttk.Scrollbar(self.app.win, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=self.scrollbar.set)

    def mostrar(self):
        self.limpiar_tabla()
        self.tabla.place(x=100,y=100)
        #self.scrollbar.pack(side="right", fill="y")

    def addDiaCotizacion(self,archivo):
        self.limpiar_tabla()
        archivo = "db\\"+archivo
        file = organizier.CSVRegister.leer_csv(archivo)
        for dato in file[1]:
            self.tabla.insert("", END, text=dato[0], values=(dato[1], dato[2], dato[3],dato[4]))
        file[0].close()

    def limpiar_tabla(self):
        # Eliminar todas las filas de la tabla
        self.tabla.delete(*self.tabla.get_children())

class TablaCotizaciones:
    def __init__(self,app) -> None:
            # Crear Treeview    
        self.app = app
        self.tabla = ttk.Treeview(self.app.win)
        self.tabla["columns"] = ("1", "2")  # Definir las columnas
        self.tabla.column("#0", width=330, minwidth=100, stretch=NO)  # Configurar la primera columna
        self.tabla.column("1", width=330, minwidth=100, stretch=NO)
        self.tabla.column("2", width=330, minwidth=100, stretch=NO)
        self.tabla.heading("#0", text="Nombre", anchor=W)  # Encabezado de la primera columna
        self.tabla.heading("1", text="Tiempo", anchor=W)  # Encabezado de la segunda columna
        self.tabla.heading("2", text="Precio", anchor=W)  # Encabezado de la tercera columna
        self.scrollbar = ttk.Scrollbar(self.app.win, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=self.scrollbar.set)

    def addCotizaciones(self,datos):
        for dato in datos:
            self.tabla.insert("", END, text=dato[0], values=(dato[1], dato[2], dato[3],dato[4]))

    def mostrar(self):
        self.limpiar_tabla()
        self.tabla.place(x=100,y=100)
        
    def limpiar_tabla(self):
        # Eliminar todas las filas de la tabla
        self.tabla.delete(*self.tabla.get_children())

class App:
    def __init__(self) -> None:
        self.LARGESIZE = "1200x600"
        self.SMALLSIZE = "200x100"

        self.organizador = organizier.CSVRegister()

        self.win = Tk()
        self.win.geometry(self.LARGESIZE)
        self.ancho,self.alto = 1200,600
        self.win.configure(bg="gray70")
        self.win.title("Aplicación")
        self.win.resizable(0,0)
        self.buttonsize = 20
        #self.win.iconbitmap("")

        #Menu inicial
        self.title = Label(self.win,text="Aplicación",font=("Arial",20))
        self.titleFrame = Frame(self.win,bg="gray30",width=self.ancho,height=150)
        self.lineFrame = Frame(self.win,bg="gold",width=self.ancho,height=30)
        self.goButtom = Button(self.win,text="Comenzar",bg="yellow",width=self.buttonsize,command=self.capture_mode)
        self.dayButtom =  Button(self.win,text="Venta diaria",bg="yellow",width=self.buttonsize,command=self.sales_list)
        self.optionsButtom = Button(self.win,text="Configuración",bg="gray30",width=self.buttonsize,command=None)
        self.exitButton = Button(self.win,bg="brown2",text="Salir",width=self.buttonsize,command=self.win.destroy)

        # Modo captura
        self.sissors = Image.open("src\images\icono_tijeras.png")
        self.sissors = self.sissors.resize((60,70))
        self.sissorsTk = ImageTk.PhotoImage(self.sissors)
        self.exitIcon = Image.open("src\images\Salir_icono.png")
        self.exitIcon = self.exitIcon.resize((70,70))
        self.exitIcon = ImageTk.PhotoImage(self.exitIcon)
        self.captureButton = Button(self.win,image=self.sissorsTk,command=self.show_cotizaciones)
        self.leaveIcon = Button(self.win,image=self.exitIcon,command=self.main_menu)

        #Muestra de cotizaciones
        self.tablaCot = TablaCotizaciones(self)
        self.tabla = TablaDatos(self)
        self.leaveToMenu = Button(self.win,bg="IndianRed2",text="Volver",width=20,command=self.main_menu)
        self.limpiarButton = Button(self.win,text="Limpiar",bg="deep sky blue",width=20)
        self.venderButton = Button(self.win,text="Vender",bg="SpringGreen2",width=20,command=None)

        # Combobox
        self.combobox_variable = StringVar(value="seleccionar cotización")
        self.combobox = ttk.Combobox(self.win,values=[],
                                     textvariable=self.combobox_variable,state="readonly")

    def selectDataCombobox(self,event):
        self.tabla.addDiaCotizacion(self.combobox.get())

    def ventaConfirm(self,event):
        print("venta") # de aqui se registra el dato en el csv y en el json y del json se crea tiket

    def hide_all(self):
        for widget in self.win.winfo_children():
            widget.place_forget()

    def main_menu(self):
        self.hide_all()
        self.win.geometry(self.LARGESIZE)
        self.titleFrame.place(x=0,y=0)
        self.lineFrame.place(x=0,y=150)
        self.title.place(x=500,y=10)
        self.goButtom.place(x=530,y=260)
        self.dayButtom.place(x=530,y=310)
        self.optionsButtom.place(x=530,y=360)
        self.exitButton.place(x=530,y=410)


    def list_menu(self):
        self.hide_all()
        self.win.geometry(self.LARGESIZE)
        self.leaveToMenu.place(x=20,y=50)
        self.limpiarButton.place(x=100,y=400)
        self.limpiarButton.config(command=self.tablaCot.limpiar_tabla)
        self.venderButton.place(x=950,y=400)
        self.combobox.place(x=500,y=50)
        self.combobox.configure(values=[])
        self.combobox.bind("<<ComboboxSelected>>", self.ventaConfirm)
        self.tablaCot.mostrar()

    def sales_list(self):
        self.hide_all()
        self.win.geometry(self.LARGESIZE)
        self.leaveToMenu.place(x=20,y=50)
        self.limpiarButton.place(x=100,y=400)
        self.limpiarButton.config(command=self.tabla.limpiar_tabla)
        self.combobox.place(x=500,y=50)
        self.combobox.configure(values=self.organizador.leer_database())
        self.combobox.bind("<<ComboboxSelected>>", self.selectDataCombobox)
        self.tabla.mostrar()


    def capture_mode(self):
        self.hide_all()
        self.win.geometry(self.SMALLSIZE)
        self.captureButton.place(x=15,y=10)
        self.leaveIcon.place(x=110,y=10)

    def show_cotizaciones(self):
        #capturer.Capturer.screnshot()
        self.list_menu()

    def run(self):
        self.main_menu()
        self.win.mainloop()