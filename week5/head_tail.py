##################################################
## Problem: head_tail.py
## Std: std61
## Name: 
## StudentId: 
##################################################
inp = input().upper()
H = 0
for i in inp:
	if i not in ['H','T']:
		print("Error: Wrong input")
		exit()
	if i == 'H':
		H+=1
print("H: {:.2f}%\nT: {:.2f}%".format(H*100/len(inp),(len(inp)-H)*100/len(inp)))
