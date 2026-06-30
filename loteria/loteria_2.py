
numero_sorte = 7


for tentariva in range(3):

    while True:
        try:
            numero = int(input('Entre com um número entre 1 e 15: '))
            break

        except ValueError:
            continue

    if numero == numero_sorte:
        print('Você acertou o número!!')
        break

    elif numero > numero_sorte: 
        print('Você errou!! Tente um número menor!')

    else:
        print('Você errou!! Tente um número maior!')
