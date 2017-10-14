import math
N = int(input())
K = int(input())
i = 1
while i <= math.factorial(N):
	if i % N == 0 and i % K == 0:
		print(i)
	i+=1
