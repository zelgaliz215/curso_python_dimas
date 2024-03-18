import calendar
import goslate
from os import system
system("cls")
from pathlib import Path #importola clase Path de la libreria pathlib

ruta_actual =Path.cwd()  #  Path.cwd() = obtiene ruta actual
print(ruta_actual)

ruta = Path('Nueva_carpeta')  #Instancia de Path con la ruta de una nueva carpeta
ruta.mkdir(exist_ok=True)  #Creo una nueva carpeta con el objeto Path -->exits_ok=True, crea solo si no existe, omite error

ruta2 = Path("Nueva_Carpeta2")
ruta2.mkdir(exist_ok=True)

#Creo estructura de carpéta
ruta3 = Path("Nueva_carpeta_3/Subcarpeta") # subcarpeta dentro de la carpeta
ruta3.mkdir(parents = True, exist_ok=True) #Crea todas las carpetas hasta la subcarpeta

ruta4 = Path("Nueva_carpeta_4/Subcarpeta/Subcarpeta_2")
ruta4.mkdir( parents = True , exist_ok = True)

#EJERCICIO CARPETAS CON LOS MESES Y DIAS 1-30

gs = goslate.Goslate()

meses = list(calendar.month_name)[1:]
print(meses)

""" traduccion= []
for mes in meses:
    traduccion.append = gs.translate(meses,'es')
    print(traduccion) """

#Creacion de listas con un for normal
dias=[]
for i in range(1,31):
    dias.append(i) 
print (dias) 
#Compresion de listas

dias2 = [i for i in range(1,31)]
print (dias2)

for mes in meses :
    print(mes)

for dia in dias2 :
    print( dia )

for mes in meses :
    for dia in dias : 
        print(f"Mes: {mes}, Día: {dia}")
        ruta = Path(f"2023/{mes}/{dia}")
        print(ruta)
        ruta.mkdir(parents=True,exist_ok=True)