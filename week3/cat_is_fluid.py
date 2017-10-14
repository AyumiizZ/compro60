def func(t):
    if t>0 and t<3:
		return ((27*t-(t**4)/4)/10-0.075)
    return 0 if t==0 else 6
inp = int(input())
print (func(inp%5) + (inp//5)*func(3))

