import requests
import os

url = 'https://www.boe.es/buscar/pdf/1995/BOE-A-1995-25444-consolidado.pdf'

r = requests.get(url)

tamaño = r.headers.get('content-length', None)

if tamaño is not None:
    print(f"El tamaño del archivo es: {tamaño} bytes")
else:
    print("No se pudo obtener el tamaño del archivo.")

numeroFragmentos = 10
tamañoFragmento = int(tamaño) / numeroFragmentos

fragmentos = []
sumatorioFragmentos = tamañoFragmento

for i in range(numeroFragmentos):
    fragmentos.append(sumatorioFragmentos)
    sumatorioFragmentos += tamañoFragmento

ruta_destino = 'C:\\Users\\Portix\\Documents\\Javier\\FP\\Segundo\\Proyecto\\Python\\PSP\\Proyecto Optimazación\\Carpeta Destino\\'

for i in range(numeroFragmentos):
    byteInicial = int(fragmentos[i] - tamañoFragmento)
    byteFinal = int(fragmentos[i]) 

    print(f"Descargando fragmento {i}: bytes={byteInicial}-{byteFinal}")

    encabezados = {'Range': f'bytes={byteInicial}-{byteFinal}'}
    r = requests.get(url, headers=encabezados, stream=True)

    temp = f'{ruta_destino}Fragmento {i}.bin'

    with open(temp, 'wb') as file:
        for chunk in r.iter_content(chunk_size=8192):
            file.write(chunk)

print("Descarga de todos los fragmentos completada.")
