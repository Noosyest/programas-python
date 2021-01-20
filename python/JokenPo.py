from random import randint
from time import sleep

while True:
    jogador = str(input('''VAMOS JOGAR JOKEN PO!
[1] PEDRA
[2] PAPEL
[3] TESOURA
QUAL VOCÊ ESCOLHE? '''))
    if jogador == '1' or jogador == '2' or jogador == '3':
        computador = randint(1, 3)
        if jogador == '1':
            jogador = 'PEDRA'
        elif jogador == '2':
            jogador = 'PAPEL'
        elif jogador == '3':
            jogador = 'TESOURA'
        if computador == 1:
            computador = 'PEDRA'
        elif computador == 2:
            computador = 'PAPEL'
        elif computador == 3:
            computador = 'TESOURA'
        print('JOKEN...')
        sleep(1)
        print('PÔ!')
        sleep(0.5)
        print(' ')
        print('-=-=-=-=- RESULTADO -=-=-=-=-')
        print(f'VOCÊ: {jogador}')
        print(f'COMPUTADOR: {computador}')
        print(' ')
        sleep(1)
        if jogador == computador:
            print(f'''-=-=-=- EMPATE -=-=-=-
AMBOS ESCOLHERAM {jogador}''')
        elif jogador == 'PEDRA' and computador == 'TESOURA':
            print(f'''-=-=-=- PARABÉNS -=-=-=-
VOCÊ VENCEU!
O COMPUTADOR ESCOLHEU {computador} E VOCÊ ESCOLHEU {jogador}''')
        elif jogador == 'TESOURA' and computador == 'PEDRA':
            print(F'''-=-=-=- QUE PENA -=-=-=-
VOCÊ PERDEU!
O COMPUTADOR ESCOLHEU {computador} E VOCÊ ESCOLHEU {jogador}''')
        elif jogador == 'PAPEL' and computador == 'PEDRA':
            print(f'''-=-=-=- PARABÉNS -=-=-=-
VOCÊ VENCEU!
O COMPUTADOR ESCOLHEU {computador} E VOCÊ ESCOLHEU {jogador}''')
        elif jogador == 'PEDRA' and computador == 'PAPEL':
            print(F'''-=-=-=- QUE PENA -=-=-=-
VOCÊ PERDEU!
O COMPUTADOR ESCOLHEU {computador} E VOCÊ ESCOLHEU {jogador}''')
        elif jogador == 'TESOURA' and computador == 'PAPEL':
            print(f'''-=-=-=- PARABÉNS -=-=-=-
VOCÊ VENCEU!
O COMPUTADOR ESCOLHEU {computador} E VOCÊ ESCOLHEU {jogador}''')
        elif jogador == 'PAPEL' and computador == 'TESOURA':
            print(F'''-=-=-=- QUE PENA -=-=-=-
VOCÊ PERDEU!
O COMPUTADOR ESCOLHEU {computador} E VOCÊ ESCOLHEU {jogador}''')
        sair = ''
        while True:
            print(' ')
            sair = str(input('QUER JOGAR DE NOVO? [S/N]')).upper().strip()
            bool_sair = bool(sair)
            if bool_sair == True:
                sair = sair[0]
                if sair == 'N' or sair == 'S':
                    break
        if sair == 'N':
            print('BYE')
            break
        else:
            print(' ')
            print('-=-=-=- NOVA PARTIDA -=-=-=-')
    else:
        input('ESSA OPÇÃO NÃO EXISTE')