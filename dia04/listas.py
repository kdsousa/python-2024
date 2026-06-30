# %%

minha_lista = []

print(minha_lista)

# %%

minha_lista = ['Teo', 'Calvo', 31, 1.82]
print(minha_lista)

# %%

# primeiro elemente
minha_lista[0]

# %%

# segundo elemento
minha_lista[1]

# %%

#ultimo elemento da lista
minha_lista[-1]

# %%

# fatiamento ou slincing
minha_lista[:2]

# %%

minha_lista[-2:]

# %%

nova_lista = minha_lista[:]
print(nova_lista)

# %%

minha_lista[::-1] # inversão

# %%

notas = []
nota = 7.75

notas.append(nota)

print(notas)

notas.append(10)

print(notas)

notas.extend([5.75, 6.24])

print(notas)

# %%

nome = 'Fulano'
nome_alto = nome.upper()

print(nome)
print(nome_alto)

notas = notas + [10, 9.25]

print(notas)

# %%

notas.remove(10)

print(notas)

# %%

nomes = ['maria', 'naty', 'luiza']

for i in nomes:
    print(i.title())

# %%

dados = ['Fulano', 'santos', 31, ['Naty', 'Josefina', 'Elaine'], ['Maria']]

dados[3][1]

# %%

dados[4][0][0]

# %%
