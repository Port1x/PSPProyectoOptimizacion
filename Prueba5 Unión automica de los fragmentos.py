import os

formato = input('¿Formato del archivo? ')
archivo_final_ruta = f'C:\\Users\\Portix\\Documents\\Javier\\FP\\Segundo\\Proyecto\\Python\\PSP\\Proyecto Optimazación\\Carpeta Destino\\Archivo Final.{formato}'

# Asumiendo que sabes cuántos fragmentos hay, o podrías calcularlo
numero_fragmentos = 10  # Reemplaza esto con el número real de fragmentos

with open(archivo_final_ruta, 'wb') as archivo_final:
    for i in range(numero_fragmentos):
        temp_ruta = f'C:\\Users\\Portix\\Documents\\Javier\\FP\\Segundo\\Proyecto\\Python\\PSP\\Proyecto Optimazación\\Carpeta Destino\\Fragmento {i}.bin'
        
        if os.path.exists(temp_ruta):
            with open(temp_ruta, 'rb') as archivo_temp:
                contenido = archivo_temp.read()
            
            archivo_final.write(contenido)
            os.remove(temp_ruta)
        else:
            print(f"No se encontró el Fragmento_{i}.bin")

print("Todos los fragmentos han sido procesados.")
