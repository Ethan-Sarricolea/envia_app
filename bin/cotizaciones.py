"""
Estrcutrura de cotizaciones y lista de cotizaciones
Author: Ethan Yahel Sarricolea Cortés
"""

UTILIDAD = 0.15

class Cotizacion:
    def __init__(self,name="",tipo="",time="",precio="") -> None:
        try:
            float(precio)
            self.number = True
        except:
            self.number = False
        self.nombre = name
        self.precio = (float(precio) if self.number else "")
        self.tiempo = time
        self.type = tipo
        self.utilidad = (round(self.precio*UTILIDAD,2) if self.number else "")
        self.final = (round(self.precio+self.utilidad,2) if self.number else "")
        self.siguiente = None

class ListaCotizaciones:
    def __init__(self) -> None:
        self.head = None

    def addCotizacion(self,name,tipo,tiempo,precio):        # Agregar al final
        newCot = Cotizacion(name,tipo,tiempo,precio)
        if self.head:
            actualCot = self.head
            while (actualCot.siguiente!=None):
                actualCot = actualCot.siguiente
            actualCot.siguiente = newCot
        else:
            self.head = newCot

    def generarLista(self):
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

    def search(self, price):
        actualCot = self.head
        if actualCot:
            while actualCot is not None:
                #print("Precio final de la cotización actual:", actualCot.final)
                if actualCot.final == price or actualCot.final == float(price):
                    return [actualCot.nombre, actualCot.type, actualCot.tiempo, actualCot.precio, actualCot.utilidad, actualCot.final]
                actualCot = actualCot.siguiente
            #print("No se encontró ninguna cotización con el precio dado.")
            return None
        else:
            print("No hay cabeza")

    def clear(self):
        actual = self.head
        while actual:
            siguiente = actual.siguiente
            del actual
            actual = siguiente
        self.cabeza = None
           
#
"""
lista = ListaCotizaciones()
lista.generarLista()
lista.addCotizacion("Estafeta","Dia siguiente","1 Dia(S) aprox.",244.75)
print(lista.generarLista())
lista.addCotizacion("FedEx","Standard Overnight","1 Dia(S) aprox.",211.39)
print(lista.generarLista())
lista.search(244.75)
lista.search("244.75")
#"""