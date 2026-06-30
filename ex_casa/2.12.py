"""
Escreva um programa que exiba os números de 1 a 100. 
Caso o número seja divisível por 3, exiba “Fizz” no seu lugar, 
e para múltiplos de 5 exiba “Buzz”. Caso seja divisível por ambos, 
exiba “FizzBuzz”.
"""

for numero in range(1, 101):
    
    if numero % 3 == 0 and numero % 5 == 0:

        print("FizzBuzz")
        
    elif numero % 3 == 0:

        print("Fizz")
        
    elif numero % 5 == 0:

        print("Buzz")
        
    else:

        print(numero)
