"""
Este es un archivo de Python que se ejecutará en el entorno virtual.

from datetime import date

today = date.today()
date = today.strftime("%d - %m - %Y")
print('La Fecha de Hoy es:', date)

print("Entorno virtual...")
"""
import matplotlib.pyplot as plt
import numpy as np
print("Entorno virtual...")
# Datos para el gráfico
categorias = ['A', 'B', 'C', 'D', 'E']
valores = [5, 7, 3, 8, 6]

# Crear el gráfico de barras
plt.bar(categorias, valores, color='red')

# Añadir título y etiquetas
plt.title('Ejemplo de Gráfico de Barras...')
plt.xlabel('Categorías')
plt.ylabel('Valores')

# Mostrar el gráfico
plt.show()

"""
Uso de f-strings
En Python 3.6 y versiones más recientes, podemos usar un tipo de cadena de caracteres llamada "f-string" que nos ayuda a crear nuestras cadenas de caracteres más fácilmente.

Para crear una f-string, solo agregamos una f antes de las comillas de apertura. Luego, dentro de la cadena de caracteres, rodeamos las variables o expresiones con llaves {}. 
Esto reemplaza su valor en la cadena cuando ejecutamos el programa.
"""
nombre = "Franz"
lenguaje_favorito = "Python"

print(f"Hola, soy {nombre}. Estoy aprendiendo {lenguaje_favorito}.")
