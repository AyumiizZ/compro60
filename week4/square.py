def print_square(a,b):
	row = 1;column = 1
	while row <= a:
		column = 1
		while column <= b:
			if row % 3 == 1 or column == 1 or column == 4:
				print("*",end = '')
			else:
				print(" ",end = '')
			column += 1
		print ()
		row += 1
mode = ""
while not (mode == 'v' or mode == 'h'):
	mode = input("Select mode (v or h) : ")
n = -1
while n<1 or n>15:
	try:
		n = int(input("Input n (1-15) : "))
	except ValueError:
		n = int(input("Input n (1-15) : "))
if mode == 'v':
	print_square(3*n+1,4)
if mode == 'h':
	print_square(4,3*n+1)
