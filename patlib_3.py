from pathlib import Path
#Renombrar libreria

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