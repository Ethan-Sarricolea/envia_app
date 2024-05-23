"""
Description: Ventana toplevel de correccion de productos
Author: 
"""

from tkinter import Toplevel, Button, ttk, StringVar, Entry, Label, messagebox
from services import security

class Corrector:
    def __init__(self) -> None:
        self.companys = ["DHL","FEDEX","UPS","ESTAFETA"] #J&T, redpack ? "PaqueteExpress","REDPACK",
        self.timeType = ["5+ Dia(s) aprox.",
                         "5 Dia(s) aprox.",
                         "4 Dia(s) aprox.",
                         "3 Dia(s) aprox.",
                         "2 Dia(s) aprox.",
                         "1 Dia(s) aprox."]
        
    # def view_status(self):
    #     # Cambiar visibilidad de texto
    #     self.entry.config(show="") if self._visibility_val else self.entry.config(show="*")
    #     self._visibility_val = False if self._visibility_val else True

    def config_label(self):
        # Quitar texto de error
        self.errorlabel.configure(text="")

    def passwordVerifi(self):
        # verificar contraseña
        if self.win.winfo_exists():
            if self.locker.iniciar_sesion_admin(self.entry.get()):
                self.price.config(state="normal")
                self.login.destroy()
            else:
                self.errorlabel.configure(text="Acceso denegado")
                self.errorlabel.after(3000,self.config_label)
        else:
            self.login.destroy()

    def closeAll(self):
        self.win.destroy()
        self.login.destroy()

    def password(self):
        self.login = Toplevel()
        self.login.title("")
        self.login.geometry("250x100")
        self.login.resizable(0,0)
        self.locker = security.Password()

        #Componentes
        self.label = Label(self.login,text="Contraseña de administrador")
        self.entry = Entry(self.login,show="*")
        # self.visibility = Button(self.login,text="V",command=self.view_status)
        self.errorlabel = Label(self.login,text="",fg="red")
        self.ok = Button(self.login,text="Continuar",bg="Green",command=self.passwordVerifi)#
        self.cancel = Button(self.login,text="Volver",bg="Red",command=self.login.destroy)

        self.label.pack()
        self.errorlabel.pack()
        self.entry.pack()
        # self.visibility.pack(side="right",anchor="n",padx=5,pady=5)
        self.cancel.pack(side="left")
        self.ok.pack(side="right",padx=5,pady=5)

    def continuar(self):
        # Confirmar datos de cotizacion individual añadida
        self.adition = True
        try:
            float(self.price.get())
            self.lista = [self.companyEntry.get(),
                    self.__type,
                    self.timesEntry.get(),
                    self.price.get()]
            for element in self.lista:
                status = True
                if not element:
                    if element==self.__type:
                        pass
                    else:
                        messagebox.showerror("Error","Asegurate de agregar todos los elementos de la cotizacion")
                        status = not status
            if status:
                self.win.destroy()
        except:
            messagebox.showerror("Error","asegurate de colocar correctamente el precio.")

    def returnToWindow(self):
        # Retornar status de uso de ventana
        if self.adition:
            return self.lista
        else:
            return False

    def run(self,price,tipo):
        self.win = Toplevel()
        self.win.title("Editar cotizacion")
        self.win.resizable(0,0)
        # self.win.geometry("")

        self.__type = tipo

        # windgets
        self.title = Label(self.win,text="Correcciones")
        self.cancelButton = Button(self.win,text="Cancelar",
                                   command=self.closeAll,
                                   bg="red")
        self.continueButton = Button(self.win,text="Confirmar",
                                     command=self.continuar,
                                     bg="green")
        self.companysText = StringVar(self.win,value="Compañia")
        self.companyEntry = ttk.Combobox(self.win,
                                         textvariable=self.companysText,
                                         values=self.companys,
                                         state="readonly")
        self.timesText = StringVar(self.win,value="Tiempo de envio")
        self.timesEntry = ttk.Combobox(self.win,
                                       values=self.timeType,
                                       textvariable=self.timesText,
                                       state="readonly")
        self.pricetext = StringVar(self.win,value="")
        self.price = Entry(self.win,state="disabled",textvariable=self.pricetext)
        self.changePrice = Button(self.win,text="Cambiar precio",command=self.password)

        # show widgets
        self.title.pack(pady=20)
        self.companyEntry.pack(pady=10,padx=60)
        self.timesEntry.pack(pady=10,padx=20)
        self.pricetext.set(price)
        self.price.pack(pady=10)
        self.changePrice.pack(pady=10)
        self.cancelButton.pack(side="left",pady=10,padx=20)
        self.continueButton.pack(side="right",pady=10,padx=20)
        
"""algo = Corrector()
algo.run()"""