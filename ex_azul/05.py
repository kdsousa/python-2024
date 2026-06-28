"""
Faça um programa que verifique se a pessoa pertence à família "calvo" ou "silva"
"""
nome = input('Digite o seu nome completo: ')

if 'calvo' in nome or 'silva' in nome:
    print('Você pertence a familia Calvo ou a família Silva!')
else:
    print('Você não pertence a família Calvo e nem a família silva!')
