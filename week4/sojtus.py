def is_prime(x):
	i = 2 
	while i < x:
		if x % i == 0:
			return False
		i += 1
	return True
i = 2; count = 0
inp = int(input())
while i <= inp/2:
	if is_prime(i) and is_prime(inp-i):
		count += 1
	i += 1
print (count)
