def gcd(a,b):
	if a<b:
		a,b = b,a
	while b!=0:
		a,b = b,a%b
	return a
p = int(input())
q = int(input())
print(gcd(p,q))
	