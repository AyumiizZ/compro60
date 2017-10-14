##################################################
## Problem: pa_ti_sed_yang_rai.py
## Std: std61
## Name: 
## StudentId: 
##################################################
def count_in_row(inp):
    count = 0
    for i in range(len(inp)-4):
        if inp[i:i+6].lower() == 'somrak':
            return True
    return False
i = 0;res = 0;check = False;no = 0
while i < 5:
    inp = input()
    if count_in_row(inp):
        res += 1
        no += 1
    else:
        no = 0
    if no == 3:
        check = True
    i+=1
if check:
    print('Love Love Somsri')
else:
    print('Mai rak mai tong ma care')
print ('\"somrak\" :: {} sentences'.format(res))
