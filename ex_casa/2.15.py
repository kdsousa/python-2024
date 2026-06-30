"""
Escreva um programa que receba uma lista de números do 
usuário e conte quantas vezes um número específico aparece na lista.
 Solicite ao usuário um número e exiba a contagem.
"""

lista_numeros = []

print("--- Montando a sua lista ---")
print("Digite os números que deseja adicionar. Quando terminar, digite 'sair'.")

while True:

    entrada = input("Digite um número (ou 'sair'): ").strip().lower()
    
    if entrada == 'sair':

        break  
        
    if entrada.replace('-', '', 1).isdigit():
        
        numero = int(entrada)
        lista_numeros.append(numero)

    else:

        print("Por favor, digite um número válido ou 'sair'.")


print(f"Sua lista final ficou assim: {lista_numeros}")

buscar_numero = int(input("Qual número você deseja contar dentro dessa lista? "))
contador = 0

for num in lista_numeros:

    if num == buscar_numero:

        contador += 1 


print(f"O número {buscar_numero} aparece {contador} vez(es) na lista.")
