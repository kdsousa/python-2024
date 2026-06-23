# Altere o programa anterior para considerar a quantidade de água

pedido = int(input('Para água normal digite 1 \n'
                    'Para água com gás digite 2\n'))

qtd = int(input('Quantas guarrafaz deseja? '))

if pedido == 1:
    print('O valor da água mineral é R$1,50 por garrafa')
    print(f'Seu pedido ficou {qtd} garrafa(s) de água mineral, totalizando R${qtd * 1.50}')
elif pedido == 2:
    print('O valor da água com gás é R$2,50 por garrafa')
    print(f'Seu pedido ficou {qtd} garrafa(s) de água com gás, totalizando R${qtd * 2.50}')
else:
    print('não temos essa opção!')
    