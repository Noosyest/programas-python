soma = count = 0
while True:
    count = count + 1
    num = str(input('[Digite 0 para sair]Digite um valor: '))
    if num.isnumeric():
        num = int(num)
        soma = soma + num
        if num == 0:
            break
    else:
        print('''
-=-=-=- AVISO -=-=-=-  ''')
        input('''Você deve digitar penas números
''')

print('''
-=-=-=- RESULTADO -=-=-=-''')
print(f'A soma dos valores digitados é {soma}')