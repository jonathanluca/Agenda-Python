def menu():
    voltar_menu = 's'
    while voltar_menu == 's':    
        serviços = input('''
            ============================
            \t\tAGENDA\n
            MENU:
            [1]CADASTRAR
            [2]LISTAR PRODUTOS
            [3]DELETAR PRODUTOS
            [4]BUSCAR PRODUTOS
            [5]SAIR
            ============================
            ESCOLHA UMA OPÇÃO ACIMA: 
            ''')
        
        if serviços=='1':
            cadastrar_produtos()
        elif serviços=='2':
            listar_produtos()
        elif serviços=='3':
            deletar_produtos()
        elif serviços=='4':
            buscar_produtos()
        else:
            sair()
        voltar_menu = input('Deseja retornar para o menu principal? (s/n) ').lower()
        

def cadastrar_produtos():
    print('Informe o nome do produto de que deseja cadastrar!\n')
    nome = input('Nome do produto: ')
    valor = input('Informe o valor do produto: ')
    quantidade = input('Informe a quantidade: ')
    try:
        agenda = open('Agenda.txt', 'a')
        dados = f'{nome}; {valor}; {quantidade}\n'
        agenda.write(dados)
        agenda.close()
        print(f'Contato gravdo com sucesso!')
    except:
        print('Error na gravação')

def listar_produtos():
    agenda = open('agenda.txt', 'r')
    for produtos in agenda:
        print(produtos)
    agenda.close()

def deletar_produtos():
    produto_deletado = input('Digite o nome que deseja deletar: ').lower()
    agenda = open('agenda.txt', 'r')
    aux =  []
    aux2 = []
    for i in agenda:
        print(i)
        aux.append(i)
    for i in range(0, len(aux)):
        if  produto_deletado not in aux[i].lower():
            aux2.append(aux[i])
    agenda = open('agenda.txt', 'w')
    for i in aux2:
        agenda.write(i)
    print(f'Contato deletado com sucesso!')
    listar_produtos()
    
    
def buscar_produtos():
    nome = input(f'Digite o nome que está procurando: ').upper()
    encontrados = False
    with open('agenda.txt', 'r') as agenda:
        for produto in agenda:
            if nome in produto.upper():        
                print(produto)
                encontrados = True
    if not encontrados:
        print('Nenhum produto encontrado!')
    agenda.close()
    
def sair():
    print(f'Obrigado por interagir comigo...!!! \nAté mais...!')
    exit()

def main():
    menu()
main()