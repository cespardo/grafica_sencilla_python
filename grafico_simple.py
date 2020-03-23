#...
#César Pardo - 23-marzo-2020
#Código de una gráfica en Python
#...

#Se importan los módulos necesarios
#Para MacOS debes abrir un terminal, y digitar el
#comando, no es necesario ingresar como SU (super usuario)
#para el caso del módulo numpy, digita este comando:
# pip3 install numpy
#para el caso del módulo matplotlib, digita este comando:
#pip3 matplotlib numpy

#Algunas aclaraciones de los módulos añadidos:
#1- Math contiene las funciones matemáticas más populares en Python,
#funciones trigonométricas, logaritmos, etc,
#2- numpy es una extensión de Python que agrega más soporte para vectores y
#matrices.
#3- Matplotlib es una biblioteca completa para crear visualizaciones
#estáticas, animadas e interactivas en Python

import math
import numpy as np
from matplotlib import pyplot as plt

#Generamos los datos para el gráfico

x = np.array(range(20))*0.1

y = np.zeros(len(x))
for i in range(len(x)):
	y[i] = math.sin(x[i])

#Se crea el gráfico
#Truco para que no se quede colgado el gráfico
plt.ion()
plt.plot(x,y)
#Truco para mostrar la gráfica, usar plt.show(), si no la coloco no modtrará
#el gráfico, aunque si se usa plt.ion() es mejor, el gráfico
#no quedará colgado
