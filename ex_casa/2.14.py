"""
Considere a seguinte lista:
[123, 435, 987, 1984, 2, 19, 423, -178, 320]

Faça um programa que retorne a posição do menor e do maior valor encontrado:

O maior valor está na posição x
O menor valor está na posição y

"""

numeros = [123, 435, 987, 1984, 2, 19, 423, -178, 320]

maior_valor = numeros[0]
posicao_maior = 0
menor_valor = numeros[0]
posicao_menor = 0

for indice, numero in enumerate(numeros):
    
    if numero > maior_valor:

        maior_valor = numero
        posicao_maior = indice
        
    if numero < menor_valor:

        menor_valor = numero
        posicao_menor = indice

print(f"O maior valor está na posição {posicao_maior}")
print(f"O menor valor está na posição {posicao_menor}")
