##################################################
## Problem: tae_histogram.py
## Std: std61
## Name: 
## StudentId: 
##################################################
def can_place(pos,height):
	if max(his[:pos]) >= height and max(his[pos+1:]) >= height and his[pos] < height:
		return True
	return False
his = [int(i) for i in input().split(' ')]
c = 0
for i in range(1,max(his)+1):
	for j in range(1,len(his)-1):
		if can_place(j,i):
			c+=1
print(c)
