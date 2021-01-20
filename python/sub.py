sub = 0
count = 0
while True:
	count += 1
	num = int(input(f'[{count}]Digite um valor: '))
	if num == 0:
		break
	else:
		if count == 1:
			sub = num
		else:
			sub -= num		
print(sub)
