##################################################
## Problem: parameters_count.py
## Std: std61
## Name: 
## StudentId: 
##################################################
# Please do not forget to `genheader`

# You can edit the parameters in parenthesis ().
def parameters_count(*args):
	return len(args)

########## DON'T EDIT CODES BELOW ##########

n = int(input())

if n == 1:
	print(parameters_count(1))
elif n == 2:
	print(parameters_count(1,2,3))
elif n == 3:
	print(parameters_count(1,2,3,4,5))
elif n == 4:
	print(parameters_count([1,2,3]))
elif n == 5:
	print(parameters_count())
