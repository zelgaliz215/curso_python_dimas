#ref = https://www.ibidemgroup.com/edu/traduccion-automatica-python/#Bibliotecas_Python

# %pip install goslate 
# ref =  https://www.ibidemgroup.com/edu/traduccion-automatica-python/#Bibliotecas_Python


#Prueba

from googletrans import Translator

# Lista en inglés que queremos traducir
lista_ingles = ["apple", "banana", "orange"]

# Creamos una instancia de Translator
translator = Translator()

# Creamos una lista vacía para almacenar la traducción
lista_traducida = []

# Recorremos la lista en inglés y traducimos cada palabra
for palabra in lista_ingles:
    # Traducimos la palabra al español
    traduccion = translator.translate(palabra, src='en', dest='es')
    # Añadimos la traducción a la lista traducida
    lista_traducida.append(traduccion.text)

# Imprimimos la lista traducida
print("Lista en español:", lista_traducida)