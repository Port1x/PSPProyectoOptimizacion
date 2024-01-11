import requests
import time

# URL del archivo a descargar
url = 'http://ipv4.download.thinkbroadband.com/5MB.zippP'

# Solicitar el nombre del archivo al usuario
nombre = input('¿Nombre del archivo? ')

# Ruta local donde se guardará el archivo
archivoLocal = f'C:\\Users\\Portix\\Documents\\Javier\\FP\\Segundo\\Proyecto\\Python\\PSP\\Proyecto Optimazación\\Carpeta Destino\\{nombre}'

# Iniciar el cronómetro
inicio = time.time()

# Realizar la petición GET para descargar el archivo
respuesta = requests.get(url)

# Finalizar el cronómetro
fin = time.time()

# Verificar si la petición fue exitosa
if respuesta.status_code == 200:
    # Escribir el contenido de la respuesta en un archivo local
    with open(archivoLocal, 'wb') as file:
        file.write(respuesta.content)
    print(f"Archivo descargado exitosamente en {fin - inicio} segundos.")
else:
    print(f"Error al descargar el archivo: {respuesta.status_code}")
