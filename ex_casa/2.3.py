"""
Escreva um programa que solicite ao usuário um 
nome e uma idade, e crie um dicionário com essas 
informações. Em seguida, exiba o dicionário.
"""
dados = {}

nome = input('Digite o nome: ')
idade = int(input('Digite a idade: '))

dados['nome'] = nome
dados['idade'] = idade

print(dados)
