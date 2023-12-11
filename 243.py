import re

cadena = "    Esta es   una   cadena con   palabras    separadas   por espacios   en blanco.   "

cadena_estandarizada = ' '.join(re.findall(r'\S+', cadena))

print(cadena_estandarizada)
