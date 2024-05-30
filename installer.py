import subprocess,sys,os,time

adminStatus = False

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
    try:
        import winshell
    except ImportError:
        install('winshell')
    labl.config(text="winshell instalado")
    root.update()
    time.sleep(1)
    try:
        import pyautogui
    except ImportError:
        install('pyautogui')
    labl.config(text="pyautogui instalado")
    root.update()
    time.sleep(1)
    try:
        import win32api
    except ImportError:
        install('pywin32')
    labl.config(text="win32 instalado")
    root.update()
    time.sleep(1)
    try:
        import cv2
        example = cv2.xfeatures2d.SIFT_create()
        #raise ImportError('opencv-contrib-python needed for xfeatures2d')
    except ImportError:
        install('opencv-python')
        install('opencv-contrib-python')
    labl.config(text="opencv y opencv-contrib-python instalados")
    root.update()
    time.sleep(1)
    try:
        import pytesseract
    except ImportError:
        install('pytesseract',)
    labl.config(text="libreria pytesseract instalada")
    root.update()
    time.sleep(1)
    try:
        import bcrypt
    except ImportError:
        install('bcrypt',)
    labl.config(text="bcrypt instalado")
    root.update()
    time.sleep(1)
    try:
        import git
    except ImportError:
        install("gitpython",)
        labl.config(text="gitpython instalado")
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
            import git
            root.geometry("250x100")
            clear()
            labl.pack()
            labl.config(text='Comenzando importación')
            root.update()
            time.sleep(2)
            repo = git.Repo.clone_from(repo_url, clone_dir, branch=branch)
            labl.config(text=f"Repositorio clonado")
            root.update()
            time.sleep(0.5)
        except Exception as e:
            print(f'Error al clonar el repositorio: {e}')
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
    root.geometry("250x100")
    root.title("EnviApp installer")

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
        global labl
        labl = tk.Label(root,text="Comprobando dependencias...")
        labl.pack(pady=20)
        root.update()  # Forzar actualización de la ventana
        root.after(500, lambda: download_packages())

    lab = tk.Label(root,text="Instalador de EnviApp")
    lab.pack()
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