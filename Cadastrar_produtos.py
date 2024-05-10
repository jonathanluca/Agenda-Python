def cadastrar_produtos ():
    print('Informe o nome do produto de que deseja cadastrar!\n')
    nome_produto = input('Nome do produto: ')
    valor_produto = input('Informe o valor do produto: ')
    quantidade_produto = input('Digite a quantidade: ')
    try:
        cadastro = open('Cadastro de produtos.txt', 'a')
        dados = f'{nome_produto}; {valor_produto}; {quantidade_produto}\n'
        cadastro.write(dados)
        cadastro.close()
        print(f'Produto cadastrado com sucesso!')
    except:
        print('Error no cadastramento')