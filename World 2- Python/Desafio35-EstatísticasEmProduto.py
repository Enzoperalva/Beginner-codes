cont_milreais=soma=menor=cont_produto=0
barato=''
while True:
    print('==============LOJINHA DO CHORUME!==============')
    nome_produto= str(input('Qual o nome do produto:'))
    valor_produto= int(input('Preço: R$'))
    cont_produto+=1
    if valor_produto > 1000:
        cont_milreais+=1
    if cont_produto ==1:
        menor=valor_produto
        barato=nome_produto
    else:
        if valor_produto<menor:
            menor=valor_produto
            barato=nome_produto
    soma+=valor_produto
    continuar= str(input('Deseja continuar [S/N]')).upper().strip()[0]
    while continuar!= 'S' and continuar != 'N':
        print('\033[31mRESPOSTA INVÁLIDA!\033[m')
        continuar = str(input('Deseja continuar [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
print('\033[36m=======CAIXA:=======\033[m')
print(f'O total gasto na compra foi: R$\033[32m{soma}\033[m')
print(f'Produtos que custam mais de R$1000: \033[32m{cont_milreais}\033[m')
print(f'Produto mais barato:{nome_produto} que custa; R${menor}')