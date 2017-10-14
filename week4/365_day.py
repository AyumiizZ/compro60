direction = input()
x = int(input())
y = int(input())

x_i = 0
y_i = 0
count = 0

for i in direction:
	if i == 'U':
		y_i+=1
	if i =='D':
		y_i-=1
	if i =='R':
		x_i+=1
	if i=='L':
		x_i-=1
	count+=1
	if x_i == x and y_i == y:
		print('Y')
		print(count)
		exit()
print('N')
