# %%
count = 1

while count <= 10:
    print(count)
    count += 1

# %%
while True:
    
    senha = input('Entre com a senha: ')
    if senha == 'pipoco':
        break
    else:
        print('Se deu mal!')

print('Sai do laço!')

# %%
while True:
    
    senha = input('Entre com a senha: ')
    if senha == 'pipoco':
        break

    elif senha == 'laralara':
        print("quase ...")
        continue

    print('Se deu mal!')

print('Sai do laço!')

# %%
count = 1

while count <= 15:
    if count % 2 == 0:
        print(count)
    count +=1
