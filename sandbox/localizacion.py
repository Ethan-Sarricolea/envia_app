from geopy.geocoders import Nominatim
from geopy.distance import distance

def calcular_distancia_cp(cp1, cp2):
    geolocator = Nominatim(user_agent="mi_aplicacion")  # Reemplaza "mi_aplicacion" por tu nombre de usuario o nombre de la aplicación

    location1 = geolocator.geocode(cp1)
    location2 = geolocator.geocode(cp2)

    if location1 and location2:
        coords1 = (location1.latitude, location1.longitude)
        coords2 = (location2.latitude, location2.longitude)

        dist = distance(coords1, coords2).kilometers
        return dist
    else:
        return None

# Ejemplo de uso
codigo_postal_1 = "96520"  # Tu código postal
codigo_postal_2 = "64000"  # Otro código postal

distancia = calcular_distancia_cp(codigo_postal_1, codigo_postal_2)
if distancia is not None:
    print(f"La distancia entre {codigo_postal_1} y {codigo_postal_2} es de {distancia:.2f} kilómetros.")
else:
    print("No se pudo encontrar información para uno o ambos códigos postales.")
