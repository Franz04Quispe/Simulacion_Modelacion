from math import sqrt, pi, exp
import numpy as np
import matplotlib.pyplot as plt

def distribucion_normal(x, media, desviacion_estandar):
    dist = (1/(sqrt(2*pi)*desviacion_estandar)) * exp(-0.5*((x-media)/desviacion_estandar)**2)
    return dist

media = 10
desviacion_estandar = 2
x = 10

print(round(distribucion_normal(x, media, desviacion_estandar), 4))

x_values = np.linspace(media - 4*desviacion_estandar, media + 4*desviacion_estandar, 1000)
y_values = [distribucion_normal(x, media, desviacion_estandar) for x in x_values]

# Graficar la distribución normal
plt.plot(x_values, y_values, label='Distribución Normal')
plt.title('Distribución Normal')
plt.xlabel('x')
plt.ylabel('Densidad de Probabilidad')
plt.legend()
plt.grid(True)
plt.show()