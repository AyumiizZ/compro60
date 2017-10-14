##################################################
## Problem: pascal_triangle.py
## Std: std61
## Name: 
## StudentId: 
##################################################
def pascal_triangle(row, col):
	if col == 0 or col == row:
		return 1
	return pascal_triangle(row - 1, col -1) + pascal_triangle(row -1, col)
print(pascal_triangle(int(input()),int(input())))
