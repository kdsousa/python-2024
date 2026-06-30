"""
Refaça o exercício 2.4 utilizando for e listas para receber as 
notas dos alunos
"""

notas = []

for i in range(4):
    nota = float(input('Digite a nota: '))
    notas.append(nota)

print(f'Maior nota {max(notas)}')
print(f'Menor nota {min(notas)}')
print(f'Média das notas {sum(notas) / len(notas)}')
