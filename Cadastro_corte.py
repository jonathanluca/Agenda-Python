
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