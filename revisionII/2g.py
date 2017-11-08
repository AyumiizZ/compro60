list = [1 for x in range(16)]
for x in list:
    print(x, end = ' ')
print()
list = [x for x in range(2,17,2)]
for x in list:
    print(x, end = ' ')
print()
list = [x for x in range(5,22,2)]
for x in list:
    print(x, end = ' ')
print()
list = [x**3 for x in range(9,-1,-1)]
for x in list:
    print(x, end = ' ')
print()
list = [x**2+1 for x in range(3,12)]
for x in list:
    print(x, end = ' ')
print()
list = [2**x for x in range(5,12)]
for x in list:
    print(x, end = ' ')
print()
list = [(-1)**x*(18+x*2) for x in range(11)]
for x in list:
    print(x, end = ' ')
print()
list = [chr(x) for x in range(ord('A'),ord('O')+1)]
for x in list:
    print(x, end = ' ')
print()