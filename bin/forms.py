"""
pasar datos a siscard de json
Author: Ethan Yahel Sarricolea Cortés
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Inicializa el navegador
driver = webdriver.Chrome()  # Necesitarás descargar el controlador de Chrome: https://sites.google.com/a/chromium.org/chromedriver/
driver.get("http://ejemplo.com")  # Reemplaza "http://ejemplo.com" con la URL de la página web que deseas controlar

# Encuentra el campo de entrada y escribe algo
campo_input = driver.find_element_by_id("id_del_campo_input")  # Reemplaza "id_del_campo_input" con el ID del campo de entrada en el formulario web
campo_input.send_keys("Datos que deseas ingresar")

# También puedes simular el envío del formulario
campo_input.send_keys(Keys.RETURN)  # Esto enviará el formulario. Puedes usar otras teclas de acuerdo con tus necesidades.

# Cierra el navegador
driver.close()
