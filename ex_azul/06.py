"""
Faça um programa que verifique se o item que a pessoa escolheu para comprar 
na loja está na lista: laranja, miojo carvão, picanha
"""
lista = ['laranja', 'cerveja', 'miojo', 'carvão', 'picanha']
item = input('Digite o item que deseja comprar: ')

if item in lista:
    print(f'O item {item}, está na lista!')
    
else:
    print(f'O item {item}, não esta na lista!')
