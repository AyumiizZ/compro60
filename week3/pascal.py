import math

def Cn_r(n,r):
    return int(math.factorial(n)/(math.factorial(r) * math.factorial(n-r)))

def pascals_row(row):
    res = "" ; count = 0
    while count <= row:
        res += "{:^3} ".format(str(Cn_r(row,count)))
        count += 1
    return res

def print_pascal(size):
    row = 0
    while row < size:
        count = size - row
        while count > 1:
            print(" ",end =' ')
            count -= 1
        print(pascals_row(row))
        row += 1

size = int(input("Size : "))
if size < 0 or size > 13:
	print ("ERROR")
else:
	print_pascal(size)
