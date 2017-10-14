##################################################
## Problem: my_calculator.py
## Std: std61
## Name: 
## StudentId: 
##################################################
change = {'[':'(',']':')','^':'**'}
try:
	inp = input()
	for key in change:
		inp = inp.replace(key,change[key])
	print(eval(inp))
except:
	print('invalid')

