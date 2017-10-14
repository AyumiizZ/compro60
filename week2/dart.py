import math
x = int(input())
y = int(input())
R = int(input())
r = math.sqrt(x**2+y**2)
if R > 6*r:
    print ("20 points")
elif R > 3*r:
    print ("10 points")
elif R > 2*r:
    print ("5 points")
else:
    print ("0 point")
