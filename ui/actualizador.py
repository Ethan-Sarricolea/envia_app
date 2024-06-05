"""
Version no funcional para actualizar repositorio
"""

from tkinter import messagebox
from pathlib import Path
import git,time,threading
import tkinter as tk

class Updater:
    def run(self) -> None:
        self.win = tk.Toplevel()
        self.win.title("Updater")
        self.win.geometry("250x100")
        self.win.resizable(0,0)
        self.labl = tk.Label(self.win,text="Preparando actualizaciones")
        self.labl.pack(pady=20)
        self.win.after(3000,self.run_detection)
        # self.win.mainloop()

    def run_detection(self):
        hilo = threading.Thread(target=self.actualizacion)
        hilo.start()

    def actualizacion(self):
        ruta_archivo = Path(__file__).resolve()
        ruta_archivo = ruta_archivo.parent
        ruta_archivo = ruta_archivo.parent
        # print(ruta_archivo)
        try:
            # Abre el repositorio
            repo = git.Repo(ruta_archivo)
            
            # Verifica si el repositorio está limpio (sin cambios no cometidos)
            if repo.is_dirty(untracked_files=True):
                 # Cada que se añada un registro habra cambios (tomar en cuenta)
                self.labl.config(text="El repositorio tiene cambios no cometidos")
                self.win.update()
                time.sleep(0.5)
                return
            
            # Obtén la rama actual
            rama_actual = repo.active_branch.name

            # Recupera la información más reciente del repositorio remoto
            self.labl.config(text="Buscando actualizaciones...")
            self.win.update()
            time.sleep(0.5)
            origin = repo.remotes.origin
            origin.fetch()

            # Verifica si hay diferencias entre la rama local y la remota
            diferencias = repo.git.diff(f'{rama_actual}..origin/{rama_actual}')
            if diferencias:
                self.labl.config(text="Actualizacion detectada.")
                self.win.update()
                time.sleep(0.5)
                self.labl.config(text="Actualizando...")
                self.win.update()
                time.sleep(0.5)
                origin.pull()
                self.labl.config(text="El repositorio ha sido actualizado")
                self.win.update()
                time.sleep(0.5)
            else:
                self.labl.config(text="El repositorio esta en su ultima version")
                self.win.update()
                time.sleep(3)
                self.win.destroy()
        except Exception as e:
            self.labl.config(text="Ha ocurrido un error")
            messagebox.showerror("Error:",e)
            self.win.update()
            time.sleep(0.5)
            messagebox.showerror("Error:",e)