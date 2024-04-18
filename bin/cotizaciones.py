"""
Estrcutrura de cotizaciones y lista de cotizaciones
Author: Ethan Yahel Sarricolea Cortés
"""

class Cotizacion:
    def __init__(self,name="",precio="",time="") -> None:
        self.nombre = name
        self.precio = float(precio)
        self.tiempo = time
        self.porcentaje = 0.15      # porcentaje de utilidad
        self.utilidad = self.precio+self.precio*self.porcentaje
        self.siguiente = None

class ListaCotizaciones:
    def __init__(self) -> None:
        self.head = None

    def addCotizacion(self,name,price,time):        # Agregar al final
        newCot = Cotizacion(name,price,time)
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
                              actualCot.precio,
                              actualCot.tiempo,
                              actualCot.utilidad))
                actualCot = actualCot.siguiente
            return array
        else:
            print("No hay cotizaciones en la lista")

"""
lista = ListaCotizaciones()
lista.generarLista()
lista.addCotizacion("Estafeta",150,"+5 dias")
lista.addCotizacion("FedEx",200,"2 dias")
print(lista.generarLista()) """