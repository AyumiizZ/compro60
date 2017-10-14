import math
n = int(input())
def a(n):
    return 1+(2*(n-1))
def b(n):
    return math.factorial(n-1)
def sum_a(n):
    return int((n/2)*(2+(2*(n-1))))
def sum_b(n):
    i,res = 1,0
    while i <= n:
        res += b(i)
        i+=1
    return res
print("a({}) = {}".format(n,a(n)))
print("b({}) = {}".format(n,b(n)))
print("sum_a({}) = {}".format(n,sum_a(n)))
print("sum_b({}) = {}".format(n,sum_b(n)))


