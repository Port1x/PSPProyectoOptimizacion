import requests

url = 'https://www.boe.es/buscar/pdf/1995/BOE-A-1995-25444-consolidado.pdf'

# Obtener el tamaño del archivo
r = requests.head(url)
tamaño = int(r.headers.get('content-length', 0))

print(f"El tamaño del archivo es: {tamaño} bytes")

if tamaño == 0:
    print("No se pudo obtener el tamaño del archivo.")
    exit()

numeroFragmentos = 10
tamañoFragmento = tamaño // numeroFragmentos
tamañoUltimoFragmento = tamañoFragmento + (tamaño % numeroFragmentos)

ruta_destino = 'C:\\Users\\Portix\\Documents\\Javier\\FP\\Segundo\\Proyecto\\Python\\PSP\\Proyecto Optimazación\\Carpeta Destino\\'

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

print("Descarga de todos los fragmentos completada.")
