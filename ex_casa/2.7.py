"""
Escreva um programa que crie um dicionário com nomes de
 frutas como chaves e seus respectivos preços como valores. 
 Solicite ao usuário o nome de uma fruta e exiba o preço correspondente.

    Maçã: R$1,50
    Banana: R$2,75
    Uva: R$1,90

    Goiaba: R$2,15
    Abacaxi: R$3,20
    Jaca: R$5,80
"""
frutas = {
    'Maçã': 1.50,
    'Banana': 2.75,
    'Uva': 1.90,
    'Goiaba': 2.15,
    'Abacaxi': 3.20,
    'Jaca': 5.80
}

fruta = input("Digite o nome da fruta para saber o preço: ").strip().title()
preco = frutas.get(fruta)

if preco is not None:
    print(f"O preço da fruta {fruta} é: R${preco:.2f}")
else:
    print(f"Desculpe, a fruta '{fruta}' não foi encontrada no sistema.")
    