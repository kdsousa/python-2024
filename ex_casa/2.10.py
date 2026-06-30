"""
Faça um programa que receba um número. Este número corresponde a uma 
posição na sequência de Fibonacci: 1, 1, 2, 3, 5,...

Exiba o número da sequência cuja posição foi informada:
	A posição x corresponde ao número y

"""

posicao = int(input("Digite a posição na sequência de Fibonacci: "))

a = 1
b = 1

if posicao == 1 or posicao == 2:
    
    resultado = 1
    
else:
    
    for _ in range(3, posicao + 1):
        
        proximo = a + b  
        a = b            
        b = proximo      
        
    resultado = b

print(f"A posição {posicao} corresponde ao número {resultado}")
