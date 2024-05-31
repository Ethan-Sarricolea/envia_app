"""
Description: Interfaz grafica de usuario
Author: Ethan Yahel Sarricolea Cortés
"""

from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
from services import capturer,cotizaciones,organizier
from services import tiketCreator,otherproduct,contador
from ui import user,editor
import time

# Tabla de venta diaria
class TablaDatos:
    def __init__(self,app) -> None:
        # Crear Treeview    
        self.app = app
        self.tabla = ttk.Treeview(self.app.win)
        self.tabla["columns"] = ("1", "2", "3","4","5")  # Definir las columnas
        self.tabla.column("#0", width=150, minwidth=100, stretch=NO)  # Columnas
        self.tabla.column("1", width=180, minwidth=100, stretch=NO)
        self.tabla.column("2", width=200, minwidth=100, stretch=NO)
        self.tabla.column("3", width=150, minwidth=100, stretch=NO)
        self.tabla.column("4", width=150, minwidth=100, stretch=NO)
        self.tabla.column("5", width=150, minwidth=100, stretch=NO)
        self.tabla.heading("#0", text="Nombre", anchor=W)  # Encabezados
        self.tabla.heading("1", text="Tipo", anchor=W)
        self.tabla.heading("2", text="Tiempo", anchor=W)
        self.tabla.heading("3", text="Precio", anchor=W)
        self.tabla.heading("4", text="Utilidad", anchor=W)
        self.tabla.heading("5", text="Final", anchor=W)
        self.scrollbar = ttk.Scrollbar(self.app.win, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=self.scrollbar.set)

    def mostrar(self):
        # Mostrar tabla en ventana principal
        self.limpiar_tabla()
        self.tabla.place(x=100,y=100,relheight=400/600)

    def addDiaCotizacion(self,archivo):
        # Agregar cotizaciones a tabla y calcular totales
        price = 0
        util = 0
        coste = 0
        self.limpiar_tabla()
        archivo = "db\\"+archivo
        file = organizier.Register.leer_csv(archivo)
        for dato in file[1]:
            self.tabla.insert("", END, text=dato[0], values=(dato[1], dato[2], dato[3],dato[4],dato[5]))
            price+=float(dato[5])
            util+=float(dato[4])
            coste+=float(dato[3])
        file[0].close()
        self.app.totalLabel.config(text=f"Costo={'{:.2f}'.format(coste)} / Ganancia={'{:.2f}'.format(util)} / Total={'{:.2f}'.format(price)}")

    def limpiar_tabla(self):
        # Eliminar todas las filas de la tabla
        self.tabla.delete(*self.tabla.get_children())
        self.app.totalLabel.config(text="Costo= / Ganancia= / Total=")

# Tabla de cotizaciones
class TablaCotizaciones:
    def __init__(self,app) -> None:
            # Crear Treeview    
        self.app = app
        self.tabla = ttk.Treeview(self.app.win)
        self.tabla["columns"] = ("1", "2","3","4")  # Definir las columnas
        self.tabla.column("#0", width=1, minwidth=100, stretch=NO)  # Columnas
        self.tabla.column("1", width=255, minwidth=100, stretch=NO)
        self.tabla.column("2", width=245, minwidth=100, stretch=NO)
        self.tabla.column("3", width=245, minwidth=100, stretch=NO)
        self.tabla.column("4", width=245, minwidth=100, stretch=NO)
        self.tabla.heading("#0", text="", anchor=W)  # Encabezados
        self.tabla.heading("1", text="Nombre", anchor=W)
        self.tabla.heading("2", text="Tipo", anchor=W)
        self.tabla.heading("3", text="Tiempo", anchor=W)
        self.tabla.heading("4", text="Precio", anchor=W)
        self.scrollbar = ttk.Scrollbar(self.app.win, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=self.scrollbar.set)

    def addCotizaciones(self,lista):
        # Insertar lista de cotizaciones
        for fila in lista:
            self.tabla.insert("", "end", values=tuple(fila))

    def addIndivcot(self,lista):
        # Insertar la cotizacion individual
        self.tabla.insert("", END, values=(lista[0], lista[1], lista[2], lista[5]))
        self.tabla.place_forget()
        self.tabla.place(x=100,y=100,relheight=400/600)

    def mostrar(self,lista):
        # Mostrar tabla en ventana principal
        self.limpiar_tabla()
        self.addCotizaciones(lista)
        self.tabla.place(x=100,y=100,relheight=400/600)
        
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
            return False
        
    def updateData(self,id,values):
        self.tabla.item(id,values=values)

# Tabla de colaboradores
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
        # Llenar tabla co0n datos
        self.limpiar_tabla()
        for dato in datos:
            self.tabla.insert("", END, text=dato)

    def mostrar(self):
        # Mostrar tabla en ventana principal
        self.limpiar_tabla()
        listanombres = self.app.acesores(1)
        self.mostrarNombres(listanombres) if listanombres!=None else False
        self.tabla.place(x=100,y=100)
        
    def limpiar_tabla(self):
        # Eliminar todas las filas de la tabla
        self.tabla.delete(*self.tabla.get_children())

    def update(self):
        # Actualizar datos de la tabla
        self.limpiar_tabla()
        listanombres = self.app.acesores(1)
        self.mostrarNombres(listanombres) if listanombres!=None else False

class App:
    def __init__(self) -> None:
        #Const
        self.LARGESIZE = "1200x600"
        self.SMALLSIZE = "200x150"

        #window
        self.win = Tk()
        self.win.geometry(self.LARGESIZE)
        self.ancho,self.alto = 1200,600
        self.win.configure(bg="gray70")
        self.win.title("EnviApp")
        self.win.resizable(0,0)
        self.buttonsize = 20

        #Package
        self.utilidades = contador.Counter()
        self.edicion = editor.Corrector()
        self.organizador = organizier.Register()
        self.camara = capturer.Capturer()
        self.adderProd = otherproduct.Adder()
        self.impresora = tiketCreator.Printer()
        self.admin = user.ModalSesionInit()

        #Menu inicial
        self.logoEnvia = Image.open(r"src\images\logo.png")
        self.logoEnvia = self.logoEnvia.resize((400,150))
        self.logoEnvia = ImageTk.PhotoImage(self.logoEnvia)
        self.titleFrame = Frame(self.win,bg="gray30",width=self.ancho,height=150)
        self.title = Label(self.win,image=self.logoEnvia,foreground="gold",background="gray30")#,bg="gold"
        self.lineFrame = Frame(self.win,bg="gold",width=self.ancho,height=30)
        self.goButtom = Button(self.win,text="Comenzar",bg="yellow",width=self.buttonsize,command=self.capture_mode)
        self.dayButtom =  Button(self.win,text="Venta diaria",bg="yellow",width=self.buttonsize,command=self.sales_list)
        self.optionsButtom = Button(self.win,text="Configuración",bg="gray30",width=self.buttonsize,command=self.configuration_mode)
        self.exitButton = Button(self.win,bg="brown2",text="Salir",width=self.buttonsize,command=self.win.destroy)
        # Modo captura
        self.sissors = Image.open(r"src\images\icono_tijeras.png")
        self.sissors = self.sissors.resize((60,70))
        self.sissorsTk = ImageTk.PhotoImage(self.sissors)
        self.exitIcon = Image.open(r"src\images\Salir_icono.png")
        self.exitIcon = self.exitIcon.resize((70,70))
        self.exitIcon = ImageTk.PhotoImage(self.exitIcon)
        self.captureButton = Button(self.win,image=self.sissorsTk,command=self.show_cotizaciones)
        self.leaveIcon = Button(self.win,image=self.exitIcon,command=self.main_menu)
        self.kilosLabel = StringVar(self.win,value="Kilogramos")
        self.kilos = ttk.Combobox(self.win,values=[1,2,3,4,5,7,10,15,20,25,30,40,50,60],
                                  textvariable=self.kilosLabel,state="readonly")

        #Muestra de cotizaciones
        self.tablaCot = TablaCotizaciones(self)
        self.tabla = TablaDatos(self)
        self.totalLabel = Label(self.win,text="Costo= / Ganancia= / Total=")
        self.leaveToMenu = Button(self.win,bg="IndianRed2",text="Volver",width=20,command=self.main_menu)
        self.limpiarButton = Button(self.win,text="Limpiar",bg="deep sky blue",width=20)
        self.venderButton = Button(self.win,text="Vender",bg="SpringGreen2",width=20,
                                   command=self.forms_mode)
        self.agregarCot = Button(self.win,text="Añadir cotizacion",width=self.buttonsize,bg="yellow",command=self.productAddition)
  
        # Zona de correccion
        self.editButton = Button(self.win,text="Editar",width=self.buttonsize,bg="orange",command=self.productEdition)
        self.continuarButton = Button(self.win,text="Continua",width=self.buttonsize,bg="green",command=self.cotizProducts)    # Continuar a cotizaciones
        
        # Combobox
        self.combobox_variable = StringVar(value="seleccionar cotización")
        self.combobox = ttk.Combobox(self.win,values=[],
                                     textvariable=self.combobox_variable,state="readonly")
      
        # Pantalla de config
        self.tabla_acesores = TablaColaboradores(self)
        self.colabs = ttk.Combobox(self.win,state="radonly",values=[])
        self.addColab = Button(self.win,width=20,text="Agregar",command=lambda: self.acesores(2))       # add
        self.deleteColab = Button(self.win,width=20,text="Eliminar",command=lambda: self.acesores(3))       # del

        #Pantalla de formulario
        self.cancelButton = Button(self.win,text="Cancelar",width=20,bg="brown2",command=self.cancelVent)
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

    def show_corrections(self,lista):
        self.hide_all()
        self.win.geometry(self.LARGESIZE)
        self.editButton.place(x=100,y=510)
        self.continuarButton.place(x=950,y=510)
        self.leaveToMenu.place(x=20,y=50)
        self.tabla_acesores.limpiar_tabla()
        self.tablaCot.mostrar(lista) 

    def cotizProducts(self):
        peso = self.kilos.get()
        self.listaCotizador.delete_process()
        lista = self.listaCotizador.generarLista()
        for cotiz in lista:
            # print(cotiz)
            porcent = self.utilidades.getPorcent(company=cotiz[0],tiempo=cotiz[2],peso=int(peso))
            try:
                self.listaCotizador.finalPrices(porcent=porcent,old=cotiz)
            except TypeError:
                messagebox.showerror("Error de calculo","No se ha podido cotizar el precio,\n verifica que los datos hayan sido colocados correctamente") #Llamen a dios
        newdata = self.listaCotizador.mostrador()
        self.list_menu(newdata)
        # boton de vender

    def cancelVent(self):
        # Mensaje de ancelar venta
        status = messagebox.askyesnocancel("Cancelar venta","Estas a punto de cancelar la venta, presiona SI para continuar")
        if status:
            self.listaCotizador.clear()
            self.tablaCot.limpiar_tabla()
            self.main_menu()

    def acesores(self,option):
        # 1=read 2=add 3=delete / manipulacion de registros de acesores
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
                                           "No se ha registrado ningún asesor en la lista.")
                else:
                    return lista
        elif option==2:
            with open("src\colaborators.txt","a+") as acesoresList:
                acesoresList.write(name+"\n")
            self.colabs['values'] = self.acesores(1)
            self.tabla_acesores.update()
        elif option==3:
            name = name+"\n"
            with open("src\colaborators.txt","r") as archivo:
                lines = archivo.readlines()
                for nombre in lines:
                    lista.append(nombre) if nombre!=name else False
            with open("src\colaborators.txt","w") as archivo:
                for nombre in lista:
                    archivo.write(nombre)
            self.colabs['values'] = self.acesores(1)
            self.tabla_acesores.update()
                    
    def selectDataCombobox(self,event):
        # Mostrar datos de cotizaciones del dia
        self.tabla.addDiaCotizacion(self.combobox.get())

    def hide_all(self):
        # Limpieza de ventana principal
        for widget in self.win.winfo_children():
            widget.place_forget()

    def main_menu(self):
        # Mostrar el menu princial
        self.hide_all()
        self.tablaCot.limpiar_tabla()
        self.win.geometry(self.LARGESIZE)
        self.titleFrame.place(x=0,y=0)
        self.lineFrame.place(x=0,y=150)
        self.goButtom.place(x=600,y=260,anchor=CENTER)
        self.dayButtom.place(x=600,y=310,anchor=CENTER)
        self.optionsButtom.place(x=600,y=360,anchor=CENTER)
        self.exitButton.place(x=600,y=410,anchor=CENTER)
        self.title.place(x=400,y=0)

    def productEdition(self):
        # Guardar los datos originales del producto para editar la lista de cots
        data = self.tablaCot.obtener_fila_seleccionada()
        if data:
            self.edicion.run(tipo=data[1],price=data[3])
            self.edicion.win.wait_window()
            status = self.edicion.returnToWindow()
            if not status:
                pass
            else:
                selected_item = self.tablaCot.tabla.selection()[0]  # Obtener el ID de la fila seleccionada
                self.tablaCot.updateData(selected_item,status)
                self.listaCotizador.edit(data,status)
                # self.listaCotizador.delete(["J&T","Terrestre","5 Dia(s) aprox.",78.43])
                # self.listaCotizador.show()


    def productAddition(self):
        # Mostrar ventana Toplevel de agregar producto
        self.adderProd.run()
        self.adderProd.win.wait_window()
        status = self.adderProd.returnToWindow()
        if not status:
            pass
        else:
            peso = int(self.kilos.get())
            # print(peso)
            self.listaCotizador.addCotizacion(name=status[0],tipo=status[1],tiempo=status[2],precio=status[3])
            old = self.listaCotizador.preSearch(price=status[3])
            # print(old)
            porcent = self.utilidades.getPorcent(peso=peso, company=status[0],tiempo=status[2])
            # print(porcent)
            self.listaCotizador.finalPrices(porcent=porcent,old=old)
            newdate = self.listaCotizador.searchNew(status[3])
            self.tablaCot.addIndivcot(newdate)
            self.adds_count+=1
            if self.adds_count == 2:
                self.agregarCot.place_forget()
                self.adds_count=0

    def list_menu(self,lista):
        # Mostrar Tabla de cotizaciones de manuable
        #
        self.hide_all()
        self.adds_count=0
        self.tablaCot.limpiar_tabla()
        self.win.geometry(self.LARGESIZE)
        self.leaveToMenu.place(x=20,y=50)
        #self.limpiarButton.place(x=100,y=510)
        #self.limpiarButton.config(command=self.tablaCot.limpiar_tabla)
        self.venderButton.place(x=950,y=510)
        self.agregarCot.place(x=500,y=510)
        self.tablaCot.mostrar(lista)

    def sales_list(self):
        # Mostrar registros de ventas
        self.admin.run()
        self.admin.window.wait_window()
        if self.admin.readPass():
            self.hide_all()
            self.win.geometry(self.LARGESIZE)
            self.leaveToMenu.place(x=20,y=50)
            self.limpiarButton.place(x=100,y=510)
            #self.limpiarButton.config(command=self.tabla.limpiar_tabla)
            self.totalLabel.place(x=630,y=515)
            self.combobox.place(x=500,y=50)
            self.combobox.configure(values=(self.organizador.leer_database()))
            self.combobox.bind("<<ComboboxSelected>>", self.selectDataCombobox)
            self.tabla.mostrar()
        else:
            pass

    def configuration_mode(self):
        # Mostrar tabla de adicion de colaboradores
        self.hide_all()
        self.win.geometry(self.LARGESIZE)
        self.leaveToMenu.place(x=20,y=50)
        self.colabs.place(x=800,y=100)
        self.addColab.place(x=800,y=150)
        self.deleteColab.place(x=800,y=200)
        self.colabs['values'] = self.acesores(1)        # Read
        self.tabla_acesores.mostrar()

    def capture_mode(self):
        # Configurar ventana a modo de captura de pantalla
        self.hide_all()
        self.win.geometry(self.SMALLSIZE)
        self.kilos.place(x=25,y=100)
        self.captureButton.place(x=15,y=10)
        self.leaveIcon.place(x=110,y=10)

    def show_cotizaciones(self):
        if self.kilos.get()!="Kilogramos":
            # Capturar la pantalla y obtener cotizaciones de manuable
            self.win.withdraw()
            time.sleep(0.1)
            self.tablaCot.limpiar_tabla()
            self.listaCotizador = cotizaciones.ListaCotizaciones()
            data = self.camara.manuable_scan(self.listaCotizador)# Remplazable con Nota de readme
            time.sleep(0.1)
            self.win.deiconify()
            # self.listaCotizador.show()
            self.show_corrections(data)
        else:
            messagebox.showwarning("Error de datos","El peso no ha sido seleccionado")

    def forms_mode(self):
        # configurar ventana a modo formulario de correccion
        datos = self.tablaCot.obtener_fila_seleccionada()
        if datos!=False:
            self.tablaCot.limpiar_tabla()
            self.hide_all()
            self.cancelButton.place(x=100,y=500)
            self.completButton.place(x=500,y=500)
            self.envioLabel.place(x=200,y=100)
            self.infolabel.place(x=400,y=100)
            self.name.place(x=200,y=150)
            self.name.delete(0, END)
            self.name.insert(0,"Nombre" if datos[0]=="False" or datos[0]==False else datos[0])
            self.type.place(x=200,y=200)
            self.type.delete(0, END)
            self.type.insert(0,datos[1])
            self.time.place(x=200,y=250)
            self.time.delete(0, END)
            self.time.insert(0,datos[2])
            self.price_text.set(f"${datos[3]}")
            self.price.place(x=200,y=300)
            self.guia.place(x=400,y=200)
            self.guia.delete(0, END)
            self.guia.insert(0,"No. de Guia")
            self.acesor.place(x=400,y=150)
            self.acesor['values'] = self.acesores(1)        # read

    def venta(self):
        # Procesar cotizacion y crear tiket
        cotVent = self.listaCotizador.search(price=self.price.get().replace("$",""))
        self.organizador.writeJson(name=(cotVent[0] if cotVent[0]==self.name.get() else self.name.get()),
                                   tipo=(cotVent[1] if cotVent[1]==self.type.get() else self.type.get()),
                                   time=(cotVent[2] if cotVent[2]==self.time.get() else self.time.get()),
                                   price=cotVent[3],
                                   utilidad=cotVent[4],
                                   final=cotVent[5])
        messagebox.showinfo("Proceso completado","La venta ha sido registrada exitosamente, continua para imprimir el tiket.")
        self.impresora.create_ticket(venta=self.organizador.readJson(),
                                     colaborator=self.acesor.get(),guide=self.guia.get())
        # Registrar la venta en db
        jsonVent = self.organizador.readJson()
        self.organizador.create_csv(f"{jsonVent['name']},{jsonVent['tipo']},{jsonVent['time']},{jsonVent['price']},{jsonVent['utilidad']},{jsonVent['final']}")
        self.tablaCot.limpiar_tabla()
        self.main_menu()

    def run(self):
        # Inicializar aplicacion
        self.main_menu()
        self.win.mainloop()