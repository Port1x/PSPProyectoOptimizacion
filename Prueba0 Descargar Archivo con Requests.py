import requests

# URL del archivo a descargar
url = 'https://www.boe.es/buscar/pdf/1995/BOE-A-1995-25444-consolidado.pdf'

# Solicitar el nombre del archivo al usuario
nombre = input('¿Nombre del archivo? ')

# Ruta local donde se guardará el archivo
archivoLocal = f'C:\\Users\\Portix\\Documents\\Javier\\FP\\Segundo\\Proyecto\\Python\\PSP\\Proyecto Optimazación\\Carpeta Destino\\{nombre}'

# Realizar la petición GET para descargar el archivo
respuesta = requests.get(url)

# Verificar si la petición fue exitosa
if respuesta.status_code == 200:
    # Escribir el contenido de la respuesta en un archivo local
    with open(archivoLocal, 'wb') as file:
        file.write(respuesta.content)
else:
    print(f"Error al descargar el archivo: {respuesta.status_code}")
