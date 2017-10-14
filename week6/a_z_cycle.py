##################################################
## Problem: a_z_cycle.py
## Std: std61
## Name: 
## StudentId: 
##################################################
alpha = 'abcdefghijklmnopqrstuvwxyz'
num = int(input())
char = input()
ans = alpha[(num+alpha.index(char.lower()))%26]
print(ans.upper()) if char.upper() == char else print(ans)
