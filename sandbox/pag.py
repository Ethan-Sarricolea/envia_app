import requests
from bs4 import BeautifulSoup

def get_text_from_url(url):
    # Obtener el HTML de la página web
    response = requests.get(url)
    
    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Crear un objeto BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extraer el texto visible en la página
        visible_text = soup.get_text()
        
        # Retornar el texto extraído
        return visible_text
    else:
        # Si la solicitud no fue exitosa, imprimir un mensaje de error
        print("Error al obtener la página:", response.status_code)
        return None

# URL de la página web que deseas copiar
url = 'https://dle.rae.es/monolito'

# Obtener el texto de la página web
web_text = get_text_from_url(url)

# Imprimir el texto obtenido
print(web_text)
