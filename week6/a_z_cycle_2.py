##################################################
## Problem: a_z_cycle.py
## Std: std61
## Name: 
## StudentId: 
##################################################
num = int(input())
char = input()
ans = chr((num+ord(char.lower())-97)%26+97)
print(ans.upper()) if char.upper() == char else print(ans)
