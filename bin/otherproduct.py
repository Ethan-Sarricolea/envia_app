"""
Description: Ventana de agregar otro producto a la lista de cotizaciones
Author: Ethan Yahel Sarricolea Cortés
"""

from tkinter import Label,Toplevel,Entry,ttk,StringVar,Frame,Button,messagebox

class Adder:
    def continuar(self):
        # Confitmar datos de cotizacion individual añadida
        self.adition = True
        try:
            float(self.__price.get())
            self.lista = [self.__name.get(),
                    self.__type.get(),
                    self.__time.get(),
                    self.__price.get()]
            for element in self.lista:
                status = True
                if not element:
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
        
    def run(self):
        # Iniciar ventana toplavel
        self.adition = False
        self.win = Toplevel()
        self.win.geometry("300x200")
        #widgets
        self.row = Frame(self.win)
        self.addLabel = Label(self.win,text="Añadir un producto")
        self.nametext = StringVar(self.win,value="Compañia")
        self.__name = ttk.Combobox(self.row,values=["DHL","ESTAFETA","FEDEX","J&T","PQUETEXPRESS","REDPACK","UPS"],
                                   textvariable=self.nametext,state="readonly")
        self.__type = Entry(self.row)
        self.__time = Entry(self.row)
        self.__price = Entry(self.row)
        self.cancelButton = Button(self.win,text="Cancelar",bg="red",command=self.win.destroy)
        self.continuebutton = Button(self.win,text="Continuar",bg="green",command=self.continuar)

        # reset
        self.addLabel.pack()
        self.row.pack(pady=10)
        self.__name.pack(pady=5)
        self.__type.pack(pady=5)
        self.__type.insert(0,"Tipo de envio")
        self.__time.pack(pady=5)
        self.__time.insert(0,"Tiempo de envio")
        self.__price.pack(pady=5)
        self.__price.insert(0,"Precio de envio")
        self.cancelButton.pack(side="left",padx=20)
        self.continuebutton.pack(side="right",padx=20)

"""
lala = Adder()
lala.run()"""