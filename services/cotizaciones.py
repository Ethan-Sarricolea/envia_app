"""
Estrcutrura de cotizaciones y lista de cotizaciones
Author: Ethan Yahel Sarricolea Cortés
"""

class Cotizacion:
    def __init__(self,name="",tipo="",time="",precio="") -> None:
        try:
            float(precio)
            self.number = True
        except:
            self.number = False
        self.nombre = name
        self.precio = (float(precio) if self.number else "")
        self.utilidad:float
        self.final:float
        self.tiempo = time
        self.type = tipo
        self.siguiente = None

class ListaCotizaciones:
    def __init__(self) -> None:
        self.head = None

    def addCotizacion(self,name,tipo,tiempo,precio):
        # Agregar cotizacion al final
        newCot = Cotizacion(name,tipo,tiempo,precio)
        if self.head:
            actualCot = self.head
            while (actualCot.siguiente!=None):
                actualCot = actualCot.siguiente
            actualCot.siguiente = newCot
        else:
            self.head = newCot

    def generarLista(self):                             # Tabla de correcciones
        # Generar array de la lista de cotizaciones
        if self.head:
            array = []
            actualCot = self.head
            while(actualCot!=None):
                array.append((actualCot.nombre,
                              actualCot.type,
                              actualCot.tiempo,
                              actualCot.precio))
                actualCot = actualCot.siguiente
            return array
        else:
            print("No hay cotizaciones en la lista")

    def returnFinal(self):          # Tabla de registros
        if self.head:
            array = []
            actualCot = self.head
            while(actualCot!=None):
                self.finalPrices(0.45)
                array.append((actualCot.nombre,
                              actualCot.type,
                              actualCot.tiempo,
                              actualCot.precio,
                              actualCot.utilidad,
                              actualCot.final))
                actualCot = actualCot.siguiente
            return array
        else:
            print("No hay cotizaciones en la lista")

    def search(self, price):
        # Busqueda de cotización agregada en captura
        actualCot = self.head
        if actualCot:
            while actualCot is not None:
                if actualCot.final == price or actualCot.final == float(price):
                    return [actualCot.nombre, actualCot.type, actualCot.tiempo, actualCot.precio, actualCot.utilidad, actualCot.final]
                actualCot = actualCot.siguiente
            return None
        else:
            print("No hay cabeza")

    def searchNew(self,price):
        # Busqueda de cotizacion recientemente creada
        actualCot = self.head
        if actualCot:
            while actualCot is not None:
                if actualCot.precio == price or actualCot.precio == float(price):
                    return [actualCot.nombre, actualCot.type, actualCot.tiempo, actualCot.precio, actualCot.utilidad, actualCot.final]
                actualCot = actualCot.siguiente
            return None
        else:
            print("No hay cabeza")

    def clear(self):
        # Limpiar lista
        actual = self.head
        while actual:
            siguiente = actual.siguiente
            del actual
            actual = siguiente
        self.cabeza = None
    
    def finalPrices(self,porcent,old):
        # Generar los precios finales a partir de la correccion de los datos
        actualCot = self.head
        if actualCot:
            while (actualCot!=None):
                if (actualCot.nombre==old[0] and actualCot.type==old[1] and
                    actualCot.tiempo==old[2] and actualCot.precio==old[3]):
                    actualCot.utilidad = (round(actualCot.precio*porcent,2))
                    actualCot.final = (round(actualCot.precio + actualCot.utilidad,2))
                    return
                actualCot = actualCot.siguiente
        else:
            print("Error: No hay cotizaciones en la lista")
        
    def edit(self,old,new):
        # intercambiar la cotizacion anterior con la nueva
        actualCot=self.head
        if actualCot:
            while (actualCot!=None):
                if (actualCot.nombre==old[0] and actualCot.type==old[1] and
                    actualCot.tiempo==old[2] and actualCot.precio==float(old[3])):
                    actualCot.nombre=new[0]
                    actualCot.type=new[1]
                    actualCot.tiempo=new[2]
                    actualCot.precio=float(new[3])
                actualCot = actualCot.siguiente
        else:
            print("Error: No hay cotizaciones en la lista")

    def mostrador(self):
        if self.head:
            array = []
            actualCot = self.head
            while(actualCot!=None):
                array.append((actualCot.nombre,
                              actualCot.type,
                              actualCot.tiempo,
                              actualCot.final))
                actualCot = actualCot.siguiente
            return array
        else:
            print("No hay cotizaciones en la lista")

    def show(self):
        actualCot = self.head
        if actualCot:
            while (actualCot != None):
                print(actualCot.nombre,actualCot.type,actualCot.tiempo,actualCot.precio)
                actualCot = actualCot.siguiente
        else:
            print("Lista vacia")

#
"""
lista = ListaCotizaciones()
lista.generarLista()
lista.addCotizacion("Estafeta","Dia siguiente","1 Dia(S) aprox.",244.75)
lista.addCotizacion("FedEx","Standard Overnight","1 Dia(S) aprox.",211.39)
print("\n-----normal",lista.generarLista())
print(lista.edit(old=["Estafeta","Dia siguiente","1 Dia(S) aprox.",244.75],
           new=["ESTAFETA","Express","1 Dia(s) aprox.",500.00]))

print("\n----Editada",lista.generarLista())
print("\n-----Final",lista.returnFinal())
#"""