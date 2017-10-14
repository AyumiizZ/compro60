##################################################
## Problem: needle_the_perfectionist.py
## Std: std61
## Name: 
## StudentId: 
##################################################
inp = input().lower()
uniq = [inp.count(i) for i in set(inp)]
if (len(set(uniq)) == 2 and max(uniq) - min(uniq) == 1 and ((min(uniq) == 1 and uniq.count(min(uniq)) == 1) or uniq.count(max(uniq)) == 1)) or len(set(uniq)) == 1: print('Perfect')
else: print('Imperfect')
