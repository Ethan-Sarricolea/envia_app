import requests
from bs4 import BeautifulSoup

# URL de la página web
url = 'URL_DE_LA_PAGINA'

# Datos de inicio de sesión (si es necesario)
payload = {
    'usuario': 'TU_USUARIO',
    'contraseña': 'TU_CONTRASEÑA'
}

# Hacer una solicitud POST para iniciar sesión (si es necesario)
# Esto dependerá de cómo esté diseñada la página web y si requiere inicio de sesión
sesion = requests.Session()
sesion.post('URL_DE_INICIO_DE_SESION', data=payload)

# Hacer una solicitud GET para obtener la página principal
response = sesion.get(url)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Obtener el HTML de la página
    html = response.text

    # Crear un objeto BeautifulSoup para analizar el HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar los elementos específicos que te interesan (por ejemplo, divs con una clase específica)
    elementos_interesantes = soup.find_all('div', class_='clase_del_div')

    # Iterar sobre los elementos interesantes y obtener el texto
    for elemento in elementos_interesantes:
        texto = elemento.get_text()
        print(texto)
else:
    print('Error al obtener la página:', response.status_code)
