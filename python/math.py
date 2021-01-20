soma = sub = opcao = count = 0
while not opcao == '3':
    while True:
        count += 1
        num = int(input('[{}]Digite um valor: '.format(count)))
        soma += num
        sub = num - sub
        if num == 0:
            break
    while not opcao == '3':
        opcao = str(input('''
O que você deseja fazer com os valores digitados?
    [1] Somar
    [2] Subtrair
    [3] Sair
Digite a opçao desejada: '''))
        if opcao == '1':
            print(' ')
            print('-=-=-=-=- RESULTADO -=-=-=-=-')
            print('A soma entre os valores digitados é {}'.format(soma))
        elif opcao == '2':
            print(' ')
            print('-=-=-=-=- RESULTADO -=-=-=-=-')
            print('A subtração entre os valores digitados é {}'.format(sub))
        if opcao != '3':
            while True: 
                sair = str(input('Deseja fazer mais alguma coisa com os valores digitados?[S/N]: ')).upper().strip()
                sair_bool = bool(sair)
                if sair_bool == True:
                    sair = sair[0]
                    if sair in 'NS':
                        break
            if sair == 'N':
                count = soma = sub = 0
                break