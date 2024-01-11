import requests
import os
import threading

def descargar_fragmento(url, ruta_destino, byteInicial, byteFinal, i):
    print(f"Descargando fragmento {i}: bytes={byteInicial}-{byteFinal}")
    encabezados = {'Range': f'bytes={byteInicial}-{byteFinal}'}
    r = requests.get(url, headers=encabezados, stream=True)
    temp = f'{ruta_destino}Fragmento_{i}.bin'
    with open(temp, 'wb') as file:
        for chunk in r.iter_content(chunk_size=8192):
            file.write(chunk)

def obtener_tamaño(url):
    r = requests.head(url)
    tamaño = int(r.headers.get('content-length', 0))
    if tamaño == 0:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            tamaño = int(r.headers.get('content-length', 0))
    return tamaño

if __name__ == "__main__":
    url = 'https://www.boe.es/buscar/pdf/1995/BOE-A-1995-25444-consolidado.pdf'
    ruta_destino = 'C:\\Users\\Portix\\Documents\\Javier\\FP\\Segundo\\Proyecto\\Python\\PSP\\Proyecto Optimazación\\Carpeta Destino\\'
    tamaño = obtener_tamaño(url)
    print(f'El tamaño del archivo es de {tamaño} bytes')

    if tamaño == 0:
        print("No se pudo obtener el tamaño del archivo.")
        exit()
    
    numeroFragmentos = 10
    tamañoFragmento = tamaño // numeroFragmentos
    tamañoUltimoFragmento = tamañoFragmento + (tamaño % numeroFragmentos)

    hilos = []
    for i in range(numeroFragmentos):
        byteInicial = i * tamañoFragmento
        if i != numeroFragmentos -1:
            byteFinal = byteInicial + tamañoFragmento - 1
        else:
            byteFinal = byteInicial + tamañoUltimoFragmento
        hilo = threading.Thread(target=descargar_fragmento, args=(url, ruta_destino, byteInicial, byteFinal, i))
        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()

    print("Descarga de todos los fragmentos completada.")

    formato = input('¿Formato del archivo final? ')
    archivo_final_ruta = f'{ruta_destino}Archivo_Final.{formato}'

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
