def matrix_multiplication(a,b):
	# Write your programme here.


# Do not edit code further this line.
a = []
b = []
a_line_len = int(input())
for _ in range(a_line_len):
	a.append([int(x) for x in input().split()])
b_line_len = int(input())
for _ in range(b_line_len):
	b.append([int(x) for x in input().split()])
print(matrix_multiplication(a,b))
