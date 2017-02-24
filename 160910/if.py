#if states

age = 20
if age>=18 :
	print('your age is ',age)
	print('and you are adult')
else:
	print('nonono')

birth = input('birth: ')
birth = int(birth)
if birth<2000:
	print('naive')

else:
	print('old')