days = [31,29,31,30,31,30,31,31,30,31,30,31]
def invalid():
    print ("Invalid input!")
    exit()
def isLeap(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return str(year) + " is leap year."
    days[1] = 28
    return str(year) + " is not leap year."
try:
    year = int(input())
    leap = isLeap(year)
    month = int(input())
    day = int(input())
    if day > days[month-1] or day<0:
        invalid()
except (ValueError,IndexError) :
    invalid()
day += 1
if day >= days[month-1]:
    day = 1; month+=1
if month >= 12:
    month = 1; year+=1
print ("The next date is {}-{:02d}-{:02d}\nYear ".format(year,month,day) +leap)
