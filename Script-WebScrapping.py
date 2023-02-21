import sys
import csv
import requests
import os
from bs4 import BeautifulSoup

#Comprobamos que se ha pasado un argumento
if len(sys.argv) != 2:
    print('Error. Debe pasar como argumento una URL de un canal de Youtube')
    sys.exit(1)

#Cogemos el HTML de la URL del canal de Youtube, y aceptamos las cookies.
#De lo contrario si no aceptamos las cookies, no nos devuelve el HTML completo.
url = sys.argv[1]
r = requests.get(url, cookies={'CONSENT': 'YES+1'})
file = open("pagina.txt", "w", encoding="utf-8")
file.write(f"{r.text}")
contenido = open("pagina.txt", "r", encoding="utf-8")

#Con el HTML, cogemos primero las URLs de los vídeos
soup = BeautifulSoup(contenido.read(), 'html.parser')
videos = []
for link in soup.find_all('a'):
    if link.get('href').startswith('/watch?v='):
        videos.append('https://www.youtube.com' + link.get('href'))
print(videos)

#Cambio para probar los commits en git
#Cambio para probar los commits en git
#Cambio para probar los commits en git
#Cambio para probar los commits en git
#Cambio para probar los commits en git
#Cambio para probar los commits en git
#Cambio para probar los commits en git