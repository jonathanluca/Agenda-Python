def menu():
    voltar_menu = 's'
    while voltar_menu == 's':
        servicos = input('''
            ======================================================
            \t\tMENU BARBEARIA
            [1] CADASTRAR CORTES
            [2] DELETAR CORTES
            [3] CONSULTAR CORTES
            [4] CADASTRAR PRODUTOS
            [5] CONSULTAR PRODUTOS
            [6] DELETAR PRODUTOS
            [7] SAIR                         
            ======================================================
            ''')
        if servicos == '1':
            cadastra_cortes ()
        elif servicos == '2':
            deletar_cortes ()
        elif servicos == '3':
            consultar_cortes ()
        elif servicos == '4':
            cadastrar_produtos ()
        elif servicos == '5':
            consultar_produtos ()
        elif servicos == '6':
            deletar_produtos ()
        else:
            sair ()
        voltar_menu = input('Deseja retornar para o menu principal? (s/n) ').lower()
        
def cadastra_cortes ():
    print('Informe o nome do produto de que deseja cadastrar!\n')
    nome_cliente = input('Nome do produto: ')
    horario = input('Informe o horário que deseja: ')
    try:
        agenda = open('Cadastro corte.txt', 'a')
        dados = f'{nome_cliente}; {horario}\n'
        agenda.write(dados)
        agenda.close()
        print(f'Agendamento realizado com sucesso!')
    except:
        print('Error no agendamento')

def deletar_cortes ():
    deletar_cortes = input('Digite o nome que deseja deletar: ').lower()
    agenda = open('Cadastro corte.txt', 'r')
    aux =  []
    aux2 = []
    for i in agenda:
        print(i)
        aux.append(i)
    for i in range(0, len(aux)):
        if  deletar_cortes not in aux[i].lower():
            aux2.append(aux[i])
    agenda = open('Cadastro corte.txt', 'w')
    for i in aux2:
        agenda.write(i)
    print(f'Agendamento deletado com sucesso!')
    
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
    return cadastra_cortes
    
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
    return cadastrar_produtos


def deletar_produtos ():
    produto_deletado = input('Digite o nome que deseja deletar: ').lower()
    agenda = open('Cadastro de produtos.txt', 'r')
    aux =  []
    aux2 = []
    for i in agenda:
        print(i)
        aux.append(i)
    for i in range(0, len(aux)):
        if  produto_deletado not in aux[i].lower():
            aux2.append(aux[i])
    agenda = open('Cadastro de produtos.txt', 'w')
    for i in aux2:
        agenda.write(i)
    print(f'Contato deletado com sucesso!')
    
def sair():
    print(f'Obrigado por interagir comigo...!!! \nAté mais...!')
    exit()
    
def main ():
    menu()
main()



# listar o valores dos serviços
    
    
    
    
    
       