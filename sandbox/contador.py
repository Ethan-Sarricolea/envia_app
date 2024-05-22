"""
Description:
author: Ethan Yahel Sarricolea Cortés

fedex terrestre = 5 dias
Dhl tiene margen fijo de marca
fedex dia siguiente
ups
estafeta (pendiente asi que sera 0 por el momento)
"""

class Counter:
    def __init__(self) -> None:
        self.kilos = [1,2,3,4,5,7,10,15,20,25,30,40,50,60]
        self.margen = [[1],[2],[45,65,65,65,0],
                         [45,65,65,65,0],[45,65,65,65,0],[65,65,65,45,0],
                         [65,95,95,45,0],[65,95,110,45,0],[65,85,95,45,0],
                         [25],[65,75,95,45,0],[65,65,95,45,0],
                         [65,55,80,45,0],[65,45,95,45,0]]
        self.companys = ["DHL","FEDEX","UPS","ESTAFETA"] #J&T, redpack ? "PaqueteExpress","REDPACK",
        self.timeType = ["5 Dia(s) aprox.","1 Dia(s) aprox."]

    def utilidad(self,peso,company,tiempo):
        if peso in self.kilos:
            porcentaje = self.margen[self.kilos.index(peso)]
            if company in self.companys:
                i = self.companys.index(company)
                if i==0:
                    return porcentaje[i]
                elif i==1:
                    if tiempo in self.timeType:
                        t = self.timeType.index(tiempo)+1
                        return porcentaje[t]
                elif i==2:
                    return porcentaje[i+1]
                elif i==3:
                    return porcentaje[i+1]

"""lalala = Counter()
print(lalala.utilidad(50,"ESTAFETA","1 Dia(s) aprox."))"""
# retorna 