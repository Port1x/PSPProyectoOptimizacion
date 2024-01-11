import os

formato = input('¿Formato del archivo? ')
archivoFinal = f'C:\\Users\\Portix\\Documents\\Javier\\FP\\Segundo\\Proyecto\\Python\\PSP\\Proyecto Optimazación\\Carpeta Destino\\Archivo Final.{formato}'
fragmento = input('¿Fragmento a descargar? ')

temp = f'C:\\Users\\Portix\\Documents\\Javier\\FP\\Segundo\\Proyecto\\Python\\PSP\\Proyecto Optimazación\\Carpeta Destino\\Fragmento {fragmento}.bin'

with open(temp, 'rb') as archivo_temp:
    contenido = archivo_temp.read()
        
with open(archivoFinal, 'wb') as archivo_final:
    archivo_final.write(contenido)

os.remove(temp)
