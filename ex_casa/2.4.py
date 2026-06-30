"""
Faça um programa que receba 4 notas de um aluno. 
Retorne a média dessas notas, a menor e a maior nota:

Média: x
Menor: y
Maior: z

"""
notas = []

for i in range(4):
    nota = float(input('Digite a nota: '))
    notas.append(nota)

print(f'Maior nota {max(notas)}')
print(f'Menor nota {min(notas)}')
print(f'Média das notas {sum(notas) / len(notas)}')
