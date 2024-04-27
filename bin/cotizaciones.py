"""
Estrcutrura de cotizaciones y lista de cotizaciones
Author: Ethan Yahel Sarricolea Cortés
"""

UTILIDAD = 0.15

class Cotizacion:
    def __init__(self,name,tipo,time,precio) -> None:
        self.nombre = name
        self.precio = float(precio)
        self.tiempo = time
        self.type = tipo
        self.utilidad = round(self.precio*UTILIDAD,2)
        self.final = round(self.precio+self.utilidad,2)
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
                """,
                              actualCot.utilidad,
                              actualCot.precio"""
                actualCot = actualCot.siguiente
            return array
        else:
            print("No hay cotizaciones en la lista")

#
"""
lista = ListaCotizaciones()
lista.generarLista()
lista.addCotizacion("Estafeta","Dia siguiente","1 Dia(S) aprox.",244.75)
print(lista.generarLista())
lista.addCotizacion("FedEx","Standard Overnight","1 Dia(S) aprox.",211.39)
print(lista.generarLista())
#"""