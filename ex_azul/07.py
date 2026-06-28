"""
Faça um programa que conte quantas vezes a letra "a" 
aparece em uma palavra 
"""
contador = 0
palavra = input('Digite uma palavra: ')

for i in palavra:

    if i == 'a':
        contador += 1

print(f'Na palavra {palavra} tem {contador} letras "a"')

## com metodo .count()
print(palavra.count("a"))
