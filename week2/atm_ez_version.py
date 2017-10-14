value = [1000,500,100,50,20,10,1]
bank = [0,0,0,0,0,0,0]
label = ["bank","coin"]
money = int(input("Input Money: "))
for i in range(7):
	bank[i] = money//value[i]
	money%=value[i]
for i in range(7):
	if bank[i] > 1:
		print ("{} : {} {}s".format(value[i],bank[i],label[i//5]))
	elif bank[i] == 1: 
		print ("{} : {} {}".format(value[i],bank[i],label[i//5]))
