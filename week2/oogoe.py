f = float(input())
v = 340.0-((340.0-20.0)*f/440)
if f > 440:
    print ("H")
elif f < 440:
    print ("L")
else:
    print ("O")
print ("{:.2f}".format(v))
