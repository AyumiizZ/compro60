##################################################
## Problem: predict.py
## Std: std61
## Name: 
## StudentId: 
##################################################
# Please do not forget to `genheader`

# You can edit the parameters in parenthesis ().
def predict(n):
	# Write your `predict()` here
	return n*200000*1.05**n if type(n)==int else [i*200000*1.05**i for i in n]


########## DON'T EDIT CODES BELOW ##########

print(predict(eval(input())))
