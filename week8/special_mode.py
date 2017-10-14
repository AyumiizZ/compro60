##################################################
## Problem: special_mode.py
## Std: std61
## Name: 
## StudentId: 
##################################################
inp = ['']
while inp[len(inp)-1] != 'end':
    inp.append(input())
inp = inp[:len(inp)-1]
tmp = []
for i in range(1,len(inp)):
    if inp[i] != inp[i-1]:
        tmp.append(1)
    else:
        tmp[len(tmp)-1] += 1
res = ''
if tmp.count(max(tmp)) > 2:
    print('Don\'t have mode')
else:
    for i in range(len(tmp)):
        if tmp[i] == max(tmp):
            res += inp[sum(tmp[:i])+1] + ' '
print(res.strip())
