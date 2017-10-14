##################################################
## Problem: tiling_colours.py
## Std: std61
## Name: 
## StudentId: 
##################################################
# Please do not forget to `genheader`

def tiling_colours(n):
	# Write your `tiling_colours(n)` here
	return 2*(tiling_colours(n-1)+tiling_colours(n-2)) if n > 2 else 3+5*(n-1)


########## DON'T EDIT CODES BELOW ##########
print(tiling_colours(int(input())))
