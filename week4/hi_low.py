import random
n_dice = int(input())
if n_dice < 1 or n_dice > 10:
	exit()
money = int(input())
if money < 100 or money > 10000:
	exit()
dice_value = random.randint(1*n_dice,6*n_dice)
bet = 0
while money > 0:
	bet += 10
	money -= bet
	guess = int(input())
	if guess == dice_value:
		print("{:.2f}\n{}\n{}".format((bet**2)*10/money,bet//10,money))
		exit()
print ("not enough money to bet")
	
