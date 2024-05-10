def consultar_produtos ():
    nome = input(f'Digite o nome que está procurando: ').upper()
    encontrados = False
    with open('Cadastro de produtos.txt', 'r') as cadastro:
        for produto in cadastro:
            if nome in produto.upper():
                print(produto)
                encontrados = True
    if not encontrados:
        print('Nenhum produto encontrado!')
    cadastro.close()
    return consultar_produtos()

