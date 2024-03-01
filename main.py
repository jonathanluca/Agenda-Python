def menu():
    voltar_menu = 's'
    while voltar_menu == 's':    
        opcao = input('''
            ============================
            AGENDA
            MENU:
            [1]CADASTRAR
            [2]LISTAR CONTATO
            [3]DELETAR CONTATO
            [4]BUSCAR CONTATO
            [5]SAIR
            ============================
            ESCOLHA UMA OPÇÃO ACIMA: 
            ''')
        
        if opcao=='1':
            cadastrar_contato()
        elif opcao=='2':
            listar_contato()
        elif opcao=='3':
            deletar_conato()
        elif opcao=='4':
            buscar_contato()
        else:
            sair()
        voltar_menu = input('Deseja retornar para o menu principal? (s/n) ').lower()
        

def cadastrar_contato():
    id_contato = input('Escolha o ID do seu conato: ')
    nome = input('Escolha o nome do seu contato: ')
    tel = input('Escreva so telefone do contato: ')
    Email = input('Escreva o E-mail do contato: ')
    try:
        agenda = open('Agenda.txt', 'a')
        dados = f'{id_contato}; {nome}; {tel}; {Email}\n'
        agenda.write(dados)
        agenda.close()
        print(f'Contato gravdo com sucesso!')
    except:
        print('Error na gravação')

def listar_contato():
    agenda = open('agenda.txt', 'r')
    for contato in agenda:
        print(contato)
    agenda.close()

def deletar_conato():
    nome_deletado = input('Digite o nome que deseja deletar: ').lower()
    agenda = open('agenda.txt', 'r')
    aux =  []
    aux2 = []
    for i in agenda:
        print(i)
        aux.append(i)
    for i in range(0, len(aux)):
        if  nome_deletado not in aux[i].lower():
            aux2.append(aux[i])
    agenda = open('agenda.txt', 'w')
    for i in aux2:
        agenda.write(i)
    print(f'Contato deletado com sucesso!')
    listar_contato()
    
    
def buscar_contato():
    nome = input(f'Digite o nome que está procurando: ').upper()
    agenda = open('agenda.txt', 'r')
    for contato in agenda:
        if nome in contato.split(';')[1].upper():
            print(contato)
    agenda.close()
    
def sair():
    print(f'Até mais...!')
    exit()

def main():
    menu()
main()