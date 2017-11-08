import math
def f(n):
    return ((2*(n**2))-10)/25
print(" n | f(n)")
print("----+-------------------------------------------------")
for n in range (-20,21,2) :
    spaces = " " * round(f(n))
    print(f" {n:2} | {spaces}*")