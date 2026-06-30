"""
Faça um programa que receba um número e exiba seu fatorial.
"""

numero = int(input("Digite um número inteiro positivo: "))
numero_original = numero
fatorial = 1

if numero < 0:

    print("Não existe fatorial de número negativo.")
    
else:

    while numero > 1:

        fatorial = fatorial * numero
        numero = numero - 1 

    print(f"O fatorial de {numero_original} é {fatorial}")
