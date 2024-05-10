from Cadastro_corte import cadastra_cortes
from Tabela_valores import tabela_valores
from Deletar_cortes import deletar_cortes
from Consultar_corte import consultar_cortes
from Cadastrar_produtos import cadastrar_produtos
from Consultar_produtos import consultar_produtos
from Deletar_produtos import deletar_produtos
import re


def validacao_email(email):
    padrao_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(padrao_email, email) is not None

# verficação do email, so pode acessar se for um email
while True:
    email = str(input('Digite seu email: '))
    if validacao_email(email):
        print('Email valido!')
        break
    else:
        print('Email invalido')

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
        match servicos:
            case '1':
                tabela_valores()
            case '2':
                cadastra_cortes()
            case '3':
                deletar_cortes()
            case '4':
                consultar_cortes()
            case '5':
                cadastrar_produtos()
            case '6':
                consultar_produtos()
            case '7':
                deletar_produtos()
            case '8':
                sair()
        voltar_menu = input('Deseja retornar para o menu principal? (s/n) ').lower()

def sair():
    print(f'Obrigado por interagir comigo...!!! \nAté mais...!')
    exit()
    
def main ():
    menu()
main()


    
    
       