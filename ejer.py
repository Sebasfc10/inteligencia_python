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

"""
Un banco da a sus ahorradores un interes de 1.5% sobre el monto
ahorrado. Teniendo como dato de entrada el saldo inicial del
ahorrador determine el saldo final.
"""
saldo = float(input('ingrese su saldo: '))
interes = saldo * 1.5/100
suma = saldo + interes
print(f'su ganancia por intereses es: {suma}')


"""
Una empresa le hace los siguientes descuentos sobre el sueldo base
a sus trabajadores: 1% por ley de politica pública, 4% por seguro
social, 0.5% por seguro forzoso y 5% por caja de ahorro. Realice un algoritmo que determine el monto de cada descuento y el monto total
a pagar al trabajador.
"""

sueldo = float(input('Ingrese su sueldo: '))
LPP = sueldo * 1/100
SS = sueldo * 4/100
SF = sueldo * 0.5/100
CH = sueldo * 5/100
suma = sueldo + LPP + SS + SF + CH
print(f'Es el total a pagar al trabajador: {suma}')

"""
El periódico el Informador cobra por un aviso clasificado un monto
que depende del número de palabras, tamaño en cetímetros y
número de colores. Cada palabra tiene un costo de $20.000, cada
centímetro tiene un costo de $15.000 y cada color tiene un costo de
$25.000. Realice un algoritmo que determine el monto a pagar por un
aviso clasificado.
"""

palabra = float(input('ingrese el numero de palabras: '))
palabras = palabra * 20000
cm = float(input('ingrese cuantos centimetros tiene el anuncion: '))
cms = cm * 15000
color = float(input('ingrese cuantos colores tiene: '))
colores = color * 25000

suma = palabras + cms + colores
print(f'este es el costo real que tendria tu anuncio clasificado : {suma}')

"""
Una empresa paga a sus empleados un bono por antigüedad que
consiste en $100.000 por el primer año laboral y $120.000 por cada
año siguiente. Realice un algoritmo que determine el monto del bono
a pagar a un trabajador que tiene varios años en la empresa
"""

año = float(input('Ingresa tus años en la empresa: '))
sueldo = float(input('ingrese su sueldo: '))
if año == 1:
    suma = sueldo + 100000
    print(f'es su primer año laboral y su bono sera de 100k + salario,queda en : {suma}')
else:
    suma = sueldo + 120000
    print(f'ya lleva varios años, su bono es de 120k + sueldo y queda en: {suma}')
    


"""
Una Universidad le paga a sus profesores $20.000 la hora y le hace
un descuento del 5% por concepto de caja de ahorro. Determine el
monto del descuento y el monto total a pagar al profesor.
"""

horas = float(input('ingrese su horas de trabajo: '))
sueldo = horas * 20000
CH = sueldo * 5/100
descuento = sueldo - CH
print(f'Su sueldo es {sueldo} pero se le descuenta  {CH} de caja de ahorro, su sueldo final es {descuento}')
