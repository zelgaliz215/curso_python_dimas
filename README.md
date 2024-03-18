# Curso libreria pathlib
**Referencia: Canal de Código Espinoza**
[Curso de Python 2023: ¿Cómo manipular archivos y directorios con el módulo PathLib de Python?](https://www.youtube.com/playlist?list=PL7HAy5R0ehQVAPSvts0I5FL-ejv6hh4bC)
## Revisar
https://www.youtube.com/watch?v=XH8TzcqUWiM

**Video completo**
[Libreria pathlib](https://www.youtube.com/watch?v=-rpLCYbPU7g&list=PL7HAy5R0ehQVAPSvts0I5FL-ejv6hh4bC&index=9&pp=iAQB)

**Invocacion y comandos basicos**

```Python
from pathlib import Path 

path_pathlib = Path.cwd() #Ruta actual
print(type(path_pathlib)) #Tipo objeto
path = Path("prueba/archivo.text") #Instancia de la ruta
print(type(path_pathlib.parts)) # Todas las partes de la ruta
print (path_pathlib.parts[0]) 
print(path_pathlib.name) # Nombre de la carpeta actual
print(path.stem) #Solo el nombre
print(path.suffix)  #Solo la extencion

```

**Crear carpetas:**
```Python
from pathlib import Path
# Instancio  con el nombre de la nueva carpeta
ruta = Path('Nueva_Carpeta')
ruta.mkdir(exist_ok = True) #Creo la nueva carpeta
#Importo la libreria calendario 
import calendar
# Creo lista con los meses
meses = list(calendar.month_name)[1:]
#creo los 30 dias 
dias = [i for i in range(1,31)]

for mes in meses
    for dia in dias :
        print(f"Mes: {mes}, Día: {dia}")
        ruta = Path(f"2023/{mes}/{dia}")
        print(ruta)
        ruta.mkdir(parents=True,exist_ok=True)

```
## Manejo de carpetas

```Python
#ruta = Path("Prueba_Renombrada")
#ruta.rename("Prueba_Renombrada")  #Rename : Renombrada
#ruta.rename("C1")

#ruta2 = Path("C1/archivo.txt")
#print(ruta2)
#ruta2.rename('C1/renombrado.txt')

#Listar subdirectorios

carpeta = Path("2023")

for r in carpeta.iterdir(): # r de ruta, iterdir itera en todos las carpertas
    print(r)

carpeta2 = Path("2023").glob("**/*") #Entrega todas las rutas y archivos dentro 

for r in carpeta2:
    print (r)

#Imprimir las carpetas que tengan archivos
carpeta3 = Path("2023").glob("**/*")

for r in carpeta3:
    if r.is_file():
        print(r)

carpeta4 = Path("2023").glob("**/*.txt")

for r in carpeta4:
    if r in carpeta4:
        print (r)
```

```Python
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
    ruta.unlink()  #esta instruccion elimina / Si e un directorio usar rmdir

