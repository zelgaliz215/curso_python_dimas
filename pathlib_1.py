from pathlib import Path
import os

# Ref = https://www.digitalocean.com/community/tutorials/how-to-use-the-pathlib-module-to-manipulate-filesystem-paths-in-python-3-es
# Ref = https://docs.python.org/es/3/library/pathlib.html
#   Obtener el directorio actual con ambas librerias
#   Os
path_os = os.getcwd()
print(path_os)
print(type(path_os))
#   pathlib
path_pathlib = Path.cwd()
print(path_pathlib)
print(type(path_pathlib))

#   Nombre de la carpeta actual:
print(path_pathlib.name) # Nombre de la carpeta actual

path = Path("prueba/archivo.text")  #Instancia de clase Path con ruta dada
print (path)

# Partes de las rutas (carpetas)
print (path_pathlib.parts[0])   #HDD
print(type(path_pathlib.parts)) # Todas las partes de la ruta
print(path.stem)   #Solo el nombre
print(path.suffix)  #Solo la extencion

print("--------------------------------------------------------------------------------")