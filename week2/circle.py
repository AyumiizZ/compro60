import math
def given_circumference(C):
    r = C/(2*math.pi)
    A = C*r/2
    print ("r = {:.5f} m\nA = {:.5f} m^2".format(r,A))

def given_radius(r):
    A = math.pi*(r**2)
    C = 2*math.pi*r
    print ("A = {:.5f} m^2\nC = {:.5f} m".format(A,C))

def given_area(A):
    r = (math.sqrt(A/math.pi))
    C = A/r*2
    print ("r = {:.5f} m\nC = {:.5f} m".format(r,C))

mode = input()
inp = float(input())
if mode == "r":
    given_radius(inp)
elif mode == "c":
    given_circumference(inp)
elif mode == "a":
    given_area(inp)
