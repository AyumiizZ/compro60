##################################################
## Problem: 52.py
## Std: std61
## Name: 
## StudentId: 
##################################################
def satu_48(n):
	return satu_48(int(str(n)[0]))+satu_48(int(str(n)[1:])) if len(str(n)) > 1 else int(n in [2,5])
print(satu_48(int(input())))
