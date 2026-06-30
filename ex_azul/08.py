"""
Faça um programa que receba 4 alturas, armazene 
em uma lista e depois mostre a soma dessas alturas
"""

alturas = []

for i in range(4):
    altura = float(input('Digite a altura: '))
    alturas.append(altura)

print(sum(alturas))
