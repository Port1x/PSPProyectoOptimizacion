import requests

url = 'https://www.boe.es/buscar/pdf/1995/BOE-A-1995-25444-consolidado.pdf'

r = requests.get(url)

tamaño = r.headers.get('content-length', None)

if tamaño is not None:
    print(f"El tamaño del archivo es: {tamaño} bytes")
else:
    print("No se pudo obtener el tamaño del archivo.")

numeroFragmentos = 10
    
tamañoFragmento = int(tamaño) / numeroFragmentos

sumatorioFragmentos = tamañoFragmento

fragmentos = []

for i in range(numeroFragmentos):
    fragmentos.append(sumatorioFragmentos)
    sumatorioFragmentos = sumatorioFragmentos + tamañoFragmento

print(fragmentos)

fragmento = input('¿Framento a descargar?')

byteInicial = fragmentos[int(fragmento)] - tamañoFragmento

byteFinal = fragmentos[int(fragmento)]

print(byteInicial)
print(byteFinal)

encabezados = {'Range': f'bytes={byteInicial}-{byteFinal}'}

r = requests.get(url, headers=encabezados, stream=True)

temp = f'C:\\Users\\Portix\\Documents\\Javier\\FP\\Segundo\\Proyecto\\Python\\PSP\\Proyecto Optimazación\\Carpeta Destino\\Fragmento {fragmento}.bin'

with open(temp, 'wb') as file:
    file.write(r.content)
