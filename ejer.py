# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 14:55:38 2021

@author: jeha2
"""

y = (((5+2+5)**2) * 5+8/2 - 30) / 2 * 5 - 3
z = 5
n = ((((8+2-4)**2)*5+8+7/2 -30*5) / 2*5-3)**5 + 15 *3 - 9/3
m = ((z)**2)*3+n
y = (((((z+2-n)**2)*m+8/2-30)/2*5-3)**5+15*3-9/3)**2-5/4
print(y)

#ejercicios con solucion a la problematica resuelta en python
"""
1 - Haga un algoritmo que calcule la masa de la siguiente fórmula:
Masa = (presión * volúmen) / (0.37 * (temperatura + 460))
"""
presion = float(input('ingrese la presion: '))
volumen = float(input('ingrese la volumen: '))
temperatura = float(input('ingrese la temperatura: '))
masa = (presion * volumen)/(0.37 * (temperatura + 460))
print(f'esta es la masa calculada: {masa}')

"""
2 - Calcular el número de pulsaciones que una persona debe tener por
cada 10 segundos de ejercicio, si la fórmula es:
Num. Pulsaciones = (200 – edad) /10.
"""
edad = float(input('ingrese aqui sue edad: '))
numP = (200 - edad)/10
print(f'tu numero de pulsaciones por 10 segundo son: {numP}')

"""
Tres personas deciden invertir su dinero para fundar una empresa.
Cada una de ellas invierte una cantidad distinta. Obtener el porcentaje
que cada quien invierte con respecto a la cantidad total invertida.
"""

p1 = float(input('que cantidad deseas invertir, socio 1: '))
p2 = float(input('que cantidad deseas invertir, socio 2: '))
p3 = float(input('que cantidad deseas invertir, socio 3: '))

porcentajE = (p1 + p2 + p3)/3
print(f'este es el porcentaje de cada uno al momento de invertir: {porcentajE}')

