##################################################
## Problem: secure_password.py
## Std: std61
## Name: 
## StudentId: 
##################################################
inp = input()
sym = '!@#$%^&*()-_+=\'\";:/?><\\|/{}[]~`%'
num = '0123456789'
scheck = False; ncheck = False
for i in inp:
	if i in sym:
		scheck = True
	if i in num:
		ncheck = True
	if len(inp) >= 8 and ncheck and scheck and inp.upper() != inp and inp.lower() != inp:
		print('secure password')
		exit()
if inp.count(' ') == 3:
	temp = [len(i) for i in inp.split(' ')]
	for i in temp:
		if i < 4:
			print('bad password')
			exit()
	print('good password')
	exit()
print('bad password')
