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