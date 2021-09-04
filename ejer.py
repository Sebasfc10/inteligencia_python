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