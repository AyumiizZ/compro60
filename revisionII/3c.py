res = [i for i in range(1,53)]
n = int(input('N = '))
c = 0
while len(res) > 0:
    c+=1
    if c == n:
        print(res[:1][0],end = ' ')
        res = res[1:]
        c = 0
    else:
        res = res[1:]+res[:1]
print()