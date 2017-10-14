##################################################
## Problem: house_of_cards.py
## Std: std61
## Name: 
## StudentId: 
##################################################
def house_of_cards(n):
	return 3*n + house_of_cards(n-1) if n > 1 else 3
print(house_of_cards(int(input())))
