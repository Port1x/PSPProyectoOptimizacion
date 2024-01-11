import requests
from threading import Thread

url = 'https://www.boe.es/buscar/pdf/1995/BOE-A-1995-25444-consolidado.pdf'


r = requests.get(url)


tamaño = r.headers.get('content-length', None)


if tamaño is not None:
    print(f"El tamaño del archivo es: {tamaño} bytes")
else:
    print("No se pudo obtener el tamaño del archivo.")





