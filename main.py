import requests
from tkinter import *

def menu():
    voltar_menu = 's'
    while voltar_menu == 's':
        servicos = input('''
            ======================================================
            \t\tMENU BARBEARIA
            [1] TABELA DE VALORES
            [2] CADASTRAR CORTES
            [3] DELETAR CORTES
            [4] CONSULTAR CORTES
            [5] CADASTRAR PRODUTOS
            [6] CONSULTAR PRODUTOS
            [7] DELETAR PRODUTOS
            [8] SAIR                         
            ======================================================
            ''')
        
        if servicos == '1':
            tabela_valores()
        elif servicos == '2':
            cadastra_cortes()
        elif servicos == '3':
            deletar_cortes()
        elif servicos == '4':
            consultar_cortes()
        elif servicos == '5':
            cadastrar_produtos()
        elif servicos == '6':
            consultar_produtos()
        elif servicos == '7':
            deletar_produtos()
        else:
            sair()
        voltar_menu = input('Deseja retornar para o menu principal? (s/n) ').lower()

def tabela_valores():
    cabelo = 30.00
    barba = 15
    pezinho = 10
    luzes = 40
    print(f'Cabelo {cabelo}$\n', f'Barba {barba}$\n', f'Pezinho {pezinho}$\n', f'Luzes {luzes}$\n')
        
def cadastra_cortes ():
    print('Informações do cliente!\n')
    nome_cliente = input('Nome do cliente: ')
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

janela = Tk()
janela.title('Barbearia')

tabela_de_valores = Label(janela, text='Consulte a tabela de varlores abaixo')
tabela_de_valores.grid(column=0, row=0)
botao_valores = Button(janela, text='Tabela de valores', command=tabela_valores)
botao_valores.grid(column=0, row=1)
texto_valores = Label(janela, text='')
texto_valores.grid(column=0, row=2)

cadastro_cortes = Label(janela, text='Realize seu cadastro')
cadastro_cortes.grid(column=0, row=2)
botao_corte = Button(janela, text='Cadastro cliente', command=cadastra_cortes)
botao_corte.grid(column=0, row=3)
texto_cortes = Label(janela, text='')
texto_cortes.grid(column=0, row=4)

excluir_cortes = Label(janela, text='Deseja excluir um corte?')
excluir_cortes.grid(column=0, row=4)
botao_excluir = Button(janela, text='Excluir corte', command=deletar_cortes)
botao_excluir.grid(column=0, row=5)
texto_excluir = Label(janela, text='')
texto_excluir.grid(column=0, row=6)

consulta_de_cortes = Label(janela, text='Consulte seu corte realizado')
consulta_de_cortes.grid(column=0, row=6)
botao_consultar = Button(janela, text='Consultar corte', command=consultar_cortes)
botao_consultar.grid(column=0, row=7)
texto_consultar = Label(janela, text='')
texto_consultar.grid(column=0, row=8)

cadastro_de_cortes = Label(janela, text='Cadastro de produtos')
cadastro_de_cortes.grid(column=0, row=8)
botao_cadastro_produtos = Button(janela, text='Cadastre um produto', command=cadastrar_produtos)
botao_cadastro_produtos.grid(column=0, row=9)
texto_cadastrar_produtos = Label(janela, text='')
texto_cadastrar_produtos.grid(column=0, row=10)

consulta_de_produtos = Label(janela, text='Consulta de produtos')
consulta_de_produtos.grid(column=0, row=10)
botao_consulta_produtos = Button(janela, text='Consulte um produto', command=consultar_produtos)
botao_consulta_produtos.grid(column=0, row=11)
texto_consulta_produtos = Label(janela, text='')
texto_consulta_produtos.grid(column=0, row=12)

excluir_produtos = Label(janela, text='Deletar produtos')
excluir_produtos.grid(column=0, row=12)
botao_excluir_produtos = Button(janela, text='Delete um produto', command=deletar_produtos)
botao_excluir_produtos.grid(column=0, row=13)
texto_excluir_produtos = Label(janela, text='')
texto_excluir_produtos.grid(column=0, row=14)

janela.mainloop()

    
# realização das telas
    
    
    
       