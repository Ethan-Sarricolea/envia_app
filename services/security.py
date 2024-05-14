"""
Description: generacion, comparacion y verificacion de contraseña de administrador
Author: Ethan yahel Sarricolea Cortés
"""

import os
import bcrypt

class Password:
    def __init__(self) -> None:
        # Obtener la contraseña del administrador
        self.__admin_password = os.getenv('ENVIAPP_ENV_VAR')
        if self.__admin_password is None:
            raise ValueError("La variable / contraseña no está configurada")
        self.__contraseña_admin_hash = self.generar_hash_contraseña(self.__admin_password)

    def generar_hash_contraseña(self,contraseña):
        # Función para generar un hash de contraseña seguro
        salt = bcrypt.gensalt()
        hash_contraseña = bcrypt.hashpw(contraseña.encode('utf-8'), salt)
        return hash_contraseña

    def verificar_contraseña(self,contraseña_ingresada, hash_contraseña):
        # Comparar la contraseña ingresada con el hash almacenado
        return bcrypt.checkpw(contraseña_ingresada.encode('utf-8'), hash_contraseña)

    def iniciar_sesion_admin(self,password_ingresada):
        # Inicio de sesion de administrador
        return (True if self.verificar_contraseña(password_ingresada, self.__contraseña_admin_hash) else False)