def acesores(option,name=""):
        # 1=read 2=add 3=delete
        lista = []
        if option==1:
            with open("src\colaborators.txt","r") as acesoresList:
                archivo = acesoresList.readlines()
                for line in archivo:
                    line = line.strip()
                    lista.append(line)
                if not lista:
                    print("xd")
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