days = [31,29,31,30,31,30,31,31,30,31,30,31]
def isLeap(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    days[1] = 28
    return False
day = 1
month = int(input())
year = int(input())
leap = isLeap(year)
for i in range(1900,year):
    if isLeap(i):
        day+=366
    else:
       day+=365
for i in range(month-1):
    day+=days[i]
day%=7
print('Sun Mon Tue Wed Thu Fri Sat')
print('    '*day,end = '')
for i in range(days[month-1]):
    print('{:3d}'.format(i+1),end = ' ')
    day += 1
    if day % 7 == 0:
        print()
if day % 7 != 0:
    print()