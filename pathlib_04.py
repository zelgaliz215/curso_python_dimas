# Crear y eliminar archivos

numeros = list(range(1,21)) # Crea una lista con los numero del 1-20
print(numeros)

for i in numeros:
    with open(f"C1/archivos_{i}.txt","w") as file: #Crear archivos
        file.write("Hola Python, este es el archivo número {i}")

# Eliminando archivos:
from pathlib import Path
rutas = list(Path("C1").glob("**/*.txt"))        

for ruta in rutas:
    pass
    #ruta.unlink()  #esta instruccion elimina / Si e un directorio usar rmdir

#Descomprimir archivos
import zipfile
directorio_zip = Path('C1')
descomrpimido = Path('C1/descomprimidos')

archivo_zip = directorio_zip.glob("*.zip") # se podria usar **/*

for ruta in archivo_zip:
    print(ruta)

######REVISAR : https://www.youtube.com/watch?v=qC6SuxvWA9k&list=PL7HAy5R0ehQVAPSvts0I5FL-ejv6hh4bC&index=5
    
