"""
Faça um programa que receba um número. Verifique se este 
número é primo ou não, e retorne o resultado:

	O número x é primo
ou
	O número x não é primo
"""

numero = int(input("Digite um número inteiro: "))

if numero <= 1:
    
    print(f"O número {numero} NÃO é primo.")
    
else:
    
    eh_primo = True
    
    for i in range(2, numero):
        
        if numero % i == 0:
            
            eh_primo = False 
            break         
            
    if eh_primo:
        
        print(f"O número {numero} é PRIMO!")
        
    else:
        
        print(f"O número {numero} NÃO é primo.")
        