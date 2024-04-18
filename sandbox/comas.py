import re

texto2 = ",,,$64.99,,,$77.99,,,$94.40,,,$128.62,,,$134.66,,,$137.97,,,$138.55,,,$149.54,,,$150.23,,,$151.24"

# Usamos una expresión regular para encontrar las comas seguidas por letras, números o espacios
nuevo_texto = re.sub(r',{3}(.+?),{3}', r',\1,', texto2)

print(nuevo_texto)
