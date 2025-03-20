from math import sqrt, pi, exp

def normal_dist(x, mean, sd):
    dist = (1/(sqrt(2*pi)*desviacion_estandar)) * exp(-0.5*((x-media)/desviacion_estandar)**2)
    return dist

media = 10
desviacion_estandar = 2
x = 10

result = normal_dist(x, media, desviacion_estandar)
print(round(result, 4))