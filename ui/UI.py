"""
Description: Interfaz grafica de usuario
- Tabla de datos
- App
Author: Ethan Yahel Sarricolea Cortés
"""

from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
from bin import capturer,cotizaciones,OCR,organizier,tiketCreator,comparador
from ui import user
import time

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
        self.tabla["columns"] = ("1", "2","3","4")  # Definir las columnas
        self.tabla.column("#0", width=1, minwidth=100, stretch=NO)  # Configurar la primera columna
        self.tabla.column("1", width=200, minwidth=100, stretch=NO)
        self.tabla.column("2", width=200, minwidth=100, stretch=NO)
        self.tabla.column("3", width=200, minwidth=100, stretch=NO)
        self.tabla.column("4", width=200, minwidth=100, stretch=NO)
        self.tabla.heading("#0", text="", anchor=W)  # Encabezado de la primera columna
        self.tabla.heading("1", text="Nombre", anchor=W)
        self.tabla.heading("2", text="Tipo", anchor=W)
        self.tabla.heading("3", text="Tiempo", anchor=W)  # Encabezado de la segunda columna
        self.tabla.heading("4", text="Precio", anchor=W)  # Encabezado de la tercera columna
        self.scrollbar = ttk.Scrollbar(self.app.win, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=self.scrollbar.set)

    def addCotizaciones(self,lista):
        for fila in lista:
            self.tabla.insert("", "end", values=tuple(fila))

    def mostrar(self,lista):
        self.limpiar_tabla()
        self.addCotizaciones(lista)
        self.tabla.place(x=100,y=100,height=400)
        
    def limpiar_tabla(self):
        # Eliminar todas las filas de la tabla
        self.tabla.delete(*self.tabla.get_children())
    
    def obtener_fila_seleccionada(self):
        # Obtener el ID de la fila seleccionada
        seleccion = self.tabla.focus()
        if seleccion:
            # Obtener los valores de la fila seleccionada
            valores = self.tabla.item(seleccion, 'values')
            return valores
        else:
            messagebox.showwarning("Advertencia","Ninguna fila seleccionada.")

class TablaColaboradores:
    def __init__(self,app) -> None:
            # Crear Treeview    
        self.app = app
        self.tabla = ttk.Treeview(self.app.win)
        self.tabla["columns"] = ("1")  # Definir las columnas
        self.tabla.column("#0", width=400, minwidth=100, stretch=NO)  # Configurar la primera columna
        self.tabla.heading("#0", text="Nombre", anchor=W)  # Encabezado de la primera columna
        self.scrollbar = ttk.Scrollbar(self.app.win, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=self.scrollbar.set)

    def mostrarNombres(self,datos):
        for dato in datos:
            self.tabla.insert("", END, text=dato)

    def mostrar(self):
        self.limpiar_tabla()
        listanombres = self.app.acesores(1)
        self.mostrarNombres(listanombres) if listanombres!=None else False
        self.tabla.place(x=100,y=100)
        
    def limpiar_tabla(self):
        # Eliminar todas las filas de la tabla
        self.tabla.delete(*self.tabla.get_children())

    def update(self):
        self.limpiar_tabla()
        listanombres = self.app.acesores(1)
        self.mostrarNombres(listanombres) if listanombres!=None else False

class App:
    def __init__(self) -> None:
        self.LARGESIZE = "1200x600"
        self.SMALLSIZE = "200x100"

        self.win = Tk()
        self.win.geometry(self.LARGESIZE)
        self.ancho,self.alto = 1200,600
        self.win.configure(bg="gray70")
        self.win.title("EnviApp")
        self.win.resizable(0,0)
        self.buttonsize = 20
        #self.win.iconbitmap("")

        self.organizador = organizier.Register()
        self.listaCotizador = cotizaciones.ListaCotizaciones()
        self.camara = capturer.Capturer(self.listaCotizador)
        #self.teseract = OCR.REOPC()
        self.impresora = tiketCreator.Printer()
        self.admin = user.ModalSesionInit()

        #Menu inicial
        self.logoEnvia = Image.open("src\images\logo.jpg")
        self.logoEnvia = self.logoEnvia.resize((500,175))
        self.logoEnvia = ImageTk.PhotoImage(self.logoEnvia)
        self.titleFrame = Frame(self.win,bg="gray30",width=self.ancho,height=150)
        self.lineFrame = Frame(self.win,bg="gold",width=self.ancho,height=30)
        self.goButtom = Button(self.win,text="Comenzar",bg="yellow",width=self.buttonsize,command=self.capture_mode)
        self.dayButtom =  Button(self.win,text="Venta diaria",bg="yellow",width=self.buttonsize,command=self.sales_list)
        self.optionsButtom = Button(self.win,text="Configuración",bg="gray30",width=self.buttonsize,command=self.configuration_mode)
        self.exitButton = Button(self.win,bg="brown2",text="Salir",width=self.buttonsize,command=self.win.destroy)
        self.title = Label(self.win,image=self.logoEnvia,bg="gold")

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
        self.venderButton = Button(self.win,text="Vender",bg="SpringGreen2",width=20,command=self.forms_mode)

        # Combobox
        self.combobox_variable = StringVar(value="seleccionar cotización")
        self.combobox = ttk.Combobox(self.win,values=[],
                                     textvariable=self.combobox_variable,state="readonly")
        
        # Pantalla de config
        self.tabla_acesores = TablaColaboradores(self)
        self.colabs = ttk.Combobox(self.win,state="radonly",values=[])
        #self.acesoresAdd = lambda: self.acesores(2)
        #self.acesoresDel = lambda: self.acesores(3)
        self.addColab = Button(self.win,width=20,text="Agregar",command=lambda: self.acesores(2))
        self.deleteColab = Button(self.win,width=20,text="Eliminar",command=lambda: self.acesores(3))
        self.updateColabs = Button(self.win,text="Actualizar",width=20,command=self.tabla_acesores.update)


        #Pantalla de formulario
        self.cancelButton = Button(self.win,text="Cancelar",width=20,bg="brown2",command=self.main_menu)
        self.completButton = Button(self.win,text="Completar",width=20,bg="SpringGreen2",command=self.venta)
        self.envioLabel = Label(self.win,text="Envio")
        self.infolabel = Label(self.win,text="Informacion")
        self.name = Entry(self.win)
        self.type = Entry(self.win)
        self.time = Entry(self.win)
        self.acesor = ttk.Combobox(self.win,values=[],state="readonly")
        self.guia = Entry(self.win)
        self.price_text = StringVar()
        self.price = Entry(self.win,textvariable=self.price_text,state="readonly")

    def acesores(self,option):
        # 1=read 2=add 3=delete
        lista = []
        name = self.colabs.get()
        if option==1:
            with open("src\colaborators.txt","r") as acesoresList:
                archivo = acesoresList.readlines()
                for line in archivo:
                    line = line.strip()
                    lista.append(line)
                if not lista:
                    messagebox.showwarning("Advertencia",
                                           "No se ha registrado ningún asesor en la lista. Para optimizar la eficiencia del proceso, se sugiere encarecidamente registrar su nombre en la sección de configuración del menú principal.")
                else:
                    return lista
        elif option==2:
            with open("src\colaborators.txt","a+") as acesoresList:
                acesoresList.write(name+"\n")
        elif option==3:
            name = name+"\n"
            with open("src\colaborators.txt","r") as archivo:
                lines = archivo.readlines()
                for nombre in lines:
                    lista.append(nombre) if nombre!=name else False
            with open("src\colaborators.txt","w") as archivo:
                for nombre in lista:
                    archivo.write(nombre)
                    
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
        self.goButtom.place(x=600,y=260,anchor=CENTER)
        self.dayButtom.place(x=600,y=310,anchor=CENTER)
        self.optionsButtom.place(x=600,y=360,anchor=CENTER)
        self.exitButton.place(x=600,y=410,anchor=CENTER)
        self.title.place(x=350,y=0)

    def list_menu(self,lista):
        self.hide_all()
        self.win.geometry(self.LARGESIZE)
        self.leaveToMenu.place(x=20,y=50)
        self.limpiarButton.place(x=100,y=510)
        self.limpiarButton.config(command=self.tablaCot.limpiar_tabla)
        self.venderButton.place(x=950,y=510)
        self.tablaCot.mostrar(lista)

    def sales_list(self):
        self.admin.run()
        self.admin.window.wait_window()
        if self.admin.readPass():
            self.hide_all()
            self.win.geometry(self.LARGESIZE)
            self.leaveToMenu.place(x=20,y=50)
            self.limpiarButton.place(x=100,y=400)
            self.limpiarButton.config(command=self.tabla.limpiar_tabla)
            self.combobox.place(x=500,y=50)
            self.combobox.configure(values=self.organizador.leer_database())
            self.combobox.bind("<<ComboboxSelected>>", self.selectDataCombobox)
            self.tabla.mostrar()
        else:
            pass

    def configuration_mode(self):
        self.hide_all()
        self.win.geometry(self.LARGESIZE)
        self.leaveToMenu.place(x=20,y=50)
        self.colabs.place(x=800,y=100)
        self.addColab.place(x=800,y=150)
        self.deleteColab.place(x=800,y=200)
        self.updateColabs.place(x=800,y=250)
        self.colabs['values'] = self.acesores(1)
        self.tabla_acesores.mostrar()

    def capture_mode(self):
        self.hide_all()
        self.win.geometry(self.SMALLSIZE)
        self.captureButton.place(x=15,y=10)
        self.leaveIcon.place(x=110,y=10)

    def show_cotizaciones(self):
        self.win.withdraw()
        time.sleep(5)
        cotizacionesMan =self.camara.manuable_scan()
        #messagebox.showinfo("",f"{self.camara.manuable_scan()}")
        time.sleep(0.1)
        self.win.deiconify()
        self.list_menu(cotizacionesMan)

    def forms_mode(self):
        datos = self.tablaCot.obtener_fila_seleccionada()
        self.tablaCot.limpiar_tabla()
        self.hide_all()
        self.cancelButton.place(x=100,y=500)
        self.completButton.place(x=500,y=500)
        self.envioLabel.place(x=200,y=100)
        self.infolabel.place(x=400,y=100)
        self.name.place(x=200,y=150)
        self.name.insert(0,"Nombre" if datos[0]=="False" or datos[0]==False else datos[0])
        self.type.place(x=200,y=200)
        self.type.insert(0,datos[1])
        self.time.place(x=200,y=250)
        self.time.insert(0,datos[2])
        self.price_text.set(f"${datos[3]}")
        self.price.place(x=200,y=300)
        self.guia.place(x=400,y=200)
        self.guia.insert(0,"No. de Guia")
        self.acesor.place(x=400,y=150)
        self.acesor['values'] = self.acesores(1)

    def venta(self):
        cotVent = self.listaCotizador.search(price=self.price.get().replace("$",""))
        self.organizador.writeJson(name=cotVent[0],
                                   tipo=cotVent[1],
                                   time=cotVent[2],
                                   price=cotVent[3],
                                   utilidad=cotVent[4],
                                   final=cotVent[5])
        self.impresora.create_ticket(venta=self.organizador.readJson(),
                                     colaborator=self.acesor.get(),guide=self.guia.get())
        # json a registro

    def run(self):
        self.main_menu()
        self.win.mainloop()
