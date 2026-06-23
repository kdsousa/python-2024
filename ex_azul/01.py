"""
Faça um programa que vende uma garrafa de água:
    a - Se o cliente escolher água mineral natural, será cobrado R$1,50
    b - Se o cliente escolher água mineral com gás, será cobrado R$2,50
"""
# %%
pedido = int(input('Para água normal digit 1 \n'
                    'para água com gás digite 2\n'))

if pedido == 1:
    print('O valor da água mineral é R$1,50')
elif pedido == 2:
    print('O valor da água com gás é R$2,50')
else:
    print('não temos essa opção!')
    