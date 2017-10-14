##################################################
## Problem: super_digit.py
## Std: std61
## Name: 
## StudentId: 
##################################################
# Please do not forget to `genheader`

def super_digit(n):
	# Write your `super_digit(n)` here
	if n > 9999:
		return super_digit(n-9999)
	return super_digit(n-9) if n > 9 else n


########## DON'T EDIT CODES BELOW ##########
print(super_digit(int(input())))
