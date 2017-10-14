##################################################
## Problem: min_cut.py
## Std: std61
## Name: 
## StudentId: 
##################################################
size = int(input())
link = [0] * (size-1)
while True:
    x,y = input().split(' ')
    x,y = int(x),int(y)
    if x < 1 or x > size or y < 1 or y > size: break
    if x > y: x,y = y,x
    for i in range(x,y):
        link[i-1] += 1
for i in range(size-1):
    if link[i] == min(link):
        print("{} {}".format(i+1,i+2))
