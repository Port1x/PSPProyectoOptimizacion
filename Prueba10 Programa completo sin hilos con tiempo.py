import requests
import os
import time

# URL del archivo a descargar
url = 'http://ipv4.download.thinkbroadband.com/100MB.zip'
try:
    r = requests.head(url)
    tamaño = int(r.headers.get('content-length', 0))

    if tamaño == 0:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()  # Verifica si la solicitud fue exitosa
            tamaño = int(r.headers.get('content-length', 0))

except requests.RequestException as e:
    print(f"Error al realizar la solicitud: {e}")
    tamaño = 0

if tamaño == 0:
    print("No se pudo obtener el tamaño del archivo.")
    exit()
else:
    print(f"El tamaño del archivo es: {tamaño}")

# Permitir al usuario especificar el número de fragmentos
numeroFragmentos = int(input("Ingrese el número de fragmentos para descargar: "))
tamañoFragmento = tamaño // numeroFragmentos
tamañoUltimoFragmento = tamañoFragmento + (tamaño % numeroFragmentos)
ruta_destino = 'C:\\Users\\Portix\\Documents\\Javier\\FP\\Segundo\\Proyecto\\Python\\PSP\\Proyecto Optimazación\\Carpeta Destino\\'

# Iniciar el cronómetro
inicio = time.time()

# Descargar cada fragmento
for i in range(numeroFragmentos):
    byteInicial = i * tamañoFragmento
    if i == numeroFragmentos - 1:  # Ajuste para el último fragmento
        byteFinal = byteInicial + tamañoUltimoFragmento 
    else:
        byteFinal = byteInicial + tamañoFragmento - 1

    print(f"Descargando fragmento {i}: bytes={byteInicial}-{byteFinal}")
    
    encabezados = {'Range': f'bytes={byteInicial}-{byteFinal}'}
    r = requests.get(url, headers=encabezados, stream=True)

    temp = f'{ruta_destino}Fragmento_{i}.bin'
    with open(temp, 'wb') as file:
        for chunk in r.iter_content(chunk_size=8192):
            file.write(chunk)

# Finalizar el cronómetro
fin = time.time()
print(f"Descarga de todos los fragmentos completada en {fin - inicio} segundos.")

# Unir los fragmentos descargados
formato = input('¿Formato del archivo? ')
archivo_final_ruta = f'{ruta_destino}Archivo Final.{formato}'

with open(archivo_final_ruta, 'wb') as archivo_final:
    for i in range(numeroFragmentos):
        temp_ruta = f'{ruta_destino}Fragmento_{i}.bin'
        
        if os.path.exists(temp_ruta):
            with open(temp_ruta, 'rb') as archivo_temp:
                contenido = archivo_temp.read()
            
            archivo_final.write(contenido)
            os.remove(temp_ruta)
        else:
            print(f"No se encontró el Fragmento_{i}.bin")

print("Todos los fragmentos han sido procesados y unidos.")
