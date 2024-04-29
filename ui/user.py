"""
Ventana de inicio de sesion de administrador
"""

from tkinter import Toplevel,Entry,Label,Button
from bin import security

class ModalSesionInit:
    def view_status(self):
        self.entry.config(show="") if self._visibility_val else self.entry.config(show="*")
        self._visibility_val = False if self._visibility_val else True

    def config_label(self):
        self.errorlabel.configure(text="")

    def passwordVerifi(self):
        if self.locker.iniciar_sesion_admin(self.entry.get()):
            self._status = True
            self.window.destroy()
        else:
            self.errorlabel.configure(text="Acceso denegado")
            self.errorlabel.after(3000,self.config_label)

    def readPass(self):
        self.status = self._status
        self._status = False
        return self.status

    def run(self):
        self.window = Toplevel()
        self.window.title("")
        self.window.geometry("250x100")
        self.locker = security.Password()
        self._visibility_val = True
        self._status=False

        #Componentes
        self.label = Label(self.window,text="Contraseña de administrador")
        self.entry = Entry(self.window,show="*")
        self.visibility = Button(self.window,text="V",command=self.view_status)
        self.errorlabel = Label(self.window,text="",fg="red")
        self.ok = Button(self.window,text="Continuar",bg="Green",command=self.passwordVerifi)
        self.cancel = Button(self.window,text="Volver",bg="Red",command=self.window.destroy)

        self.label.pack()
        self.errorlabel.pack()
        self.entry.pack()
        self.visibility.pack(side="right",anchor="n",padx=5,pady=5)
        self.cancel.pack(side="left")
        self.ok.pack(side="right",padx=5,pady=5)
