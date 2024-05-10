def consultar_cortes ():
    nome = input(f'Digite o nome que está procurando: ').upper()
    encontrados = False
    with open('Cadastro corte.txt', 'r') as agenda:
        for produto in agenda:
            if nome in produto.upper():
                print(produto)
                encontrados = True
    if not encontrados:
        print('Nenhum cliente encontrado!')
    agenda.close()
    return consultar_cortes()