##################################################
## Problem: inverse_roman_number.py
## Std: std61
## Name: 
## StudentId: 
##################################################
def to_Arabic(roman):
    value = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    temp = []
    res = 0
    for i in roman:
        temp.append(value[i])
    i = 0
    while i < len(roman)-1:
        if temp[i] < temp[i+1]:
            res += temp[i+1] - temp[i]
            i += 2
        else:
            res += temp[i]
            i += 1
    if temp[len(roman)-1] <= temp[len(roman)-2]:
        res += temp[i]
    return res
roman = input()
print(to_Arabic(roman))
