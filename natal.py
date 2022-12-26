from time import sleep
x = '^'
y = ' '
n = 0
while(n<10):
	if n == 0:

		print('FELIZ NATAL!!!\n 	 *')
		
	else:
		sleep(.5)
		print((y*(10-n)) + ((n+(n-1))*x))
	n+=1

print('HoHoHo!') 
