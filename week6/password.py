import random
def check_input(msg,Min,Max):
	inp = int(input(msg))
	if inp < Min or inp > Max:
		print('Wrong Input')
		exit()
	return inp
symbol = '!@_%&'
passwd = []
pass_len = check_input('The required password lenght is: ',6,20)
up_len = check_input('The required password upper case is: ',0,pass_len)
sym_len = check_input('The required password symbols is: ',0,pass_len-up_len)
num_len = check_input('The required password numbers is: ',0,pass_len-up_len-sym_len)
low_len = pass_len - up_len - sym_len - num_len
if low_len < 1:
	print('Sorry, the numbers you entered don\'t match up! Please try again ...')
	exit()
while pass_len > 0:
	if up_len > 0:
		passwd.insert(random.randint(0,len(passwd)),chr(random.randint(ord('A'),ord('Z'))))
		up_len -= 1; pass_len -= 1
	if sym_len > 0:
		passwd.insert(random.randint(0,len(passwd)),symbol[random.randint(0,4)])
		sym_len -= 1; pass_len -= 1
	if num_len > 0:
		passwd.insert(random.randint(0,len(passwd)),str(random.randint(0,9)))
		num_len -= 1; pass_len -= 1
	if low_len > 0:
		passwd.insert(random.randint(0,len(passwd)),chr(random.randint(ord('a'),ord('z'))))
		low_len -= 1; pass_len -= 1
print(''.join(passwd))
