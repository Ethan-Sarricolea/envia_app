import requests
from bs4 import BeautifulSoup

# URL de inicio de sesión
login_url = 'https://www.example.com/login'

# Datos de inicio de sesión
payload = {
    'username': 'tu_usuario',
    'password': 'tu_contraseña'
}

# Crear una sesión para mantener la autenticación
session = requests.Session()

# Enviar una solicitud POST para iniciar sesión
login_response = session.post(login_url, data=payload)

# Verificar si el inicio de sesión fue exitoso
if login_response.status_code == 200:
    # Ahora puedes hacer solicitudes a páginas protegidas
    protected_page_url = 'https://www.example.com/protected-page'
    protected_page_response = session.get(protected_page_url)
    
    # Verificar si la solicitud a la página protegida fue exitosa
    if protected_page_response.status_code == 200:
        # Parsear el HTML utilizando BeautifulSoup
        soup = BeautifulSoup(protected_page_response.content, 'html.parser')
        
        # Ahora puedes extraer información del contenido HTML
        # por ejemplo, encontrar elementos específicos, etc.
    else:
        print("Error al acceder a la página protegida:", protected_page_response.status_code)
else:
    print("Error al iniciar sesión:", login_response.status_code)
