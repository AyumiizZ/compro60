##################################################
## Problem: hen.py
## Std: std61
## Name: 
## StudentId: 
##################################################
idol = [input() for i in range(int(input()))]
meet = [input() for i in range(int(input()))]
c = 0
tmp = [False]*len(idol)
for i in range(len(meet)):
	tmp[idol.index(meet[i])] = True
	if tmp.count(True) == len(idol):
		tmp = [idol.index(meet[i]) == j for j in range(len(idol))]
		c+=1
print(c+int(True in tmp))
