import os
import bcrypt

class Password:
    def __init__(self) -> None:
        # Obtener la contraseña del administrador de la variable de entorno
        self.__admin_password = os.getenv('ENVIAPP_ENV_VAR')
        if self.__admin_password is None:
            raise ValueError("La variable de entorno ENVIAPP_ENV_VAR no está configurada")
        self.__contraseña_admin_hash = self.generar_hash_contraseña(self.__admin_password)

    # Función para generar un hash de contraseña seguro
    def generar_hash_contraseña(self,contraseña):
        salt = bcrypt.gensalt()
        hash_contraseña = bcrypt.hashpw(contraseña.encode('utf-8'), salt)
        return hash_contraseña

    # Función para verificar la contraseña ingresada con el hash almacenado
    def verificar_contraseña(self,contraseña_ingresada, hash_contraseña):
        return bcrypt.checkpw(contraseña_ingresada.encode('utf-8'), hash_contraseña)

    # Lógica para iniciar sesión como administrador
    def iniciar_sesion_admin(self,password_ingresada):
        if self.verificar_contraseña(password_ingresada, self.__contraseña_admin_hash):
            return True
            # Aquí puedes agregar la lógica para acceder a las funciones de administrador
        else:
            return False
# Llamar a la función para iniciar sesión como administrador iniciar_sesion_admin()
