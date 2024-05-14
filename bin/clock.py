"""
Description: Reloj para obtener la fecha del dia
Author: Ethan Yahel Sarricolea Cortés
"""

import datetime

class Clock:
    def __init__(self) -> None:
        self.date = datetime.datetime.now()

    def data(self):
        self.date = datetime.datetime.now()
        self.fecha = self.date.strftime("%d-%m-%Y")
        
        return self.fecha
    
    def hour(self):
        self.date = datetime.datetime.now()
        self.hora = self.date.strftime("%H:%M:%S")
        return self.hora
    
"""
import time
reloj = Clock()
print(reloj.hour())
time.sleep(5)
print(reloj.hour())
"""
