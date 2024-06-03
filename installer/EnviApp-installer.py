import subprocess,sys,os,time,webbrowser,git
from pathlib import Path

adminStatus = False

librerias = ["winshell","pyautogui","pywin32","opencv-python","opencv-contrib-python","pytesseract","gitpython","bcrypt"]

def actualizacion():
    ruta_archivo = Path(__file__).resolve()
    print(ruta_archivo)
    ruta_archivo = ruta_archivo.parent
    clear()
    labl.pack(pady=20)
    try:
        # Abre el repositorio
        repo = git.Repo(ruta_archivo)
        
        # Verifica si el repositorio está limpio (sin cambios no cometidos)
        if repo.is_dirty(untracked_files=True):
            labl.config(text="El repositorio tiene cambios no cometidos")
            root.update()
            time.sleep(0.5)
            return
        
        # Obtén la rama actual
        rama_actual = repo.active_branch.name

        # Recupera la información más reciente del repositorio remoto
        labl.config(text="Buscando actualizaciones...")
        root.update()
        time.sleep(0.5)
        origin = repo.remotes.origin
        origin.fetch()

        # Verifica si hay diferencias entre la rama local y la remota
        diferencias = repo.git.diff(f'{rama_actual}..origin/{rama_actual}')
        if diferencias:
            labl.config(text="Actualizacion detectada.")
            root.update()
            time.sleep(0.5)
            labl.config(text="Actualizando...")
            root.update()
            time.sleep(0.5)
            origin.pull()
            labl.config(text="El repositorio ha sido actualizado")
            root.update()
            time.sleep(0.5)
        else:
            labl.config(text="El repositorio esta en su ultima version")
            root.update()
            time.sleep(0.5)
    except Exception as e:
        labl.config(text="Ha ocurrido un error")
        root.update()
        time.sleep(0.5)
        print(f"Ocurrió un error: {e}")

def crear_acceso_directo(ruta_objetivo):
    import winshell
    from win32com.client import Dispatch
    # Obtener el escritorio del usuario actual
    escritorio = winshell.desktop()
    # Definir la ruta completa del acceso directo
    ruta_objetivo += "\\EnviApp.exe"
    ruta_acceso_directo = os.path.join(escritorio, "EnviApp.lnk")
    # Crear el acceso directo
    shell = Dispatch('WScript.Shell')
    acceso_directo = shell.CreateShortCut(ruta_acceso_directo)
    acceso_directo.TargetPath = ruta_objetivo
    acceso_directo.save()

def install(package):
    labl.config(text=f"Installing {package}")
    root.update()
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    time.sleep(0.5)

def is_package_installed(package_name):
    try:
        result = subprocess.run(
            [sys.executable, '-m', 'pip', 'show', package_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.returncode == 0
    except Exception as e:
        print(f"Error al verificar el paquete: {e}")
        return False

def detectPass():
    if os.getenv("ENVIAPP_ENV_VAR"):
        labl.config(text="Contraseña de administrador encontrada")
        status = True
    else:
        labl.config(text="Introduzca la contraseña de administrador")
        status = False
    root.update()
    time.sleep(0.5)
    return status

def download_packages():
    labl.config(text="Comprobando paquetes")
    root.update()
    for lib in librerias:
        status = True if is_package_installed(lib) else False
        if status:
            labl.config(text=f"{lib} installed")
            root.update()
            time.sleep(0.5)
            continue
        else:
            install(lib)
            labl.config(text=f"{lib} installing")
            root.update()
            time.sleep(1)
    root.update()
    time.sleep(0.5)
    labl.config(text="All required packages are installed.")
    root.update()
    time.sleep(1.5)
    root.after(500, lambda: repo())

def clone_repo():
    branch='deploy'
    clone_dir= entry.get()
    repo_url = "https://github.com/Ethan-Sarricolea/envia_app.git"
    if os.path.isdir(clone_dir):
        try:
            clone_dir= (entry.get()+"\\Envia_app")
            root.geometry("250x100")
            clear()
            labl.pack()
            labl.config(text='Comenzando importación')
            root.update()
            time.sleep(2)
            repos = git.Repo.clone_from(repo_url, clone_dir, branch=branch)
            labl.config(text=f"Repositorio clonado")
            root.update()
            time.sleep(0.5)
        except Exception as e:
            print(f'Error al clonar el repositorio: {e}')
            repo()
            return
        time.sleep(3)
        admin()
        crear_acceso_directo(clone_dir)  
    else:
        labl.config(text=f'La ruta de directorio no es valida')
        root.update()
    
def window():
    import tkinter as tk
    from tkinter import filedialog
    global root
    root = tk.Tk()
    root.geometry("250x150")
    root.title("EnviApp installer")
    root.resizable(0,0)

    global clear
    def clear():
        for widget in root.winfo_children():
            widget.pack_forget()
    
    global admin
    def admin():
        clear()
        labl.pack(pady=20)
        labl.config(text="Verificando contraseña de administrador...")
        root.update()
        time.sleep(0.5)
        if detectPass():
            labl.config(text="Instalacion exitosa")
        else:
            labl.config(text="Instalacion exitosa. No hay contraseña de administrador")
    
    global repo
    def repo():
        root.geometry("300x200")
        labl.config(text="Selecciona la carpeta de descarga para la app")
        global entry
        entry = tk.Entry(root)
        entry.pack()
        entry.insert(0,"C:\Program Files")
        tk.Button(root,text="Seleccionar ubicación",command=path).pack()
        tk.Button(root,text="Descargar",bg="green",
               command=clone_repo).pack(side="right")
        tk.Button(root,text="Cancelar",bg="red",
               command=root.destroy).pack(side="left")

    def path():
        filepath = filedialog.askdirectory()
        entry.delete(0,tk.END)
        entry.insert(0,filepath)

    def run():
        clear()
        labl.pack(pady=20)
        root.update()  # Forzar actualización de la ventana
        root.after(500, lambda: download_packages())

    def pythonlink():
        webbrowser.open("https://www.microsoft.com/store/productId/9NRWMJP3717K?ocid=pdpshare")

    global labl
    labl = tk.Label(root,text="Comprobando dependencias...")

    lab = tk.Label(root,text="Instalador de EnviApp",font=("TkDefaultFont", 14))
    lab.pack()
    tk.Button(root,text="Descargar python",
              bg="blue",
              command=pythonlink).pack(pady=10)
    tk.Button(root,text="Buscar actualizaciones",bg="gold",command=actualizacion).pack()
    leave = tk.Button(root,text="Salir",
           bg="red",
           command=root.destroy)
    leave.pack(side="left",padx=20,ipadx=15)
    cont = tk.Button(root,text="Comenzar",
           bg="green",
           command=run)
    cont.pack(side="right",padx=20,ipadx=5)
    root.mainloop()
window()