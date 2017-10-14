##################################################
## Problem: real_tower_of_hanoi.py
## Std: std61
## Name: 
## StudentId: 
##################################################
# Please do not forget to `genheader`

def hanoi_solve(no_disk, start, temp, target):
	if no_disk < 2 or no_disk > 10:
		print('Wrong input')
	elif no_disk == 2:
		print('Move disk 1 from pole {} to pole {}'.format(start, temp))
		print('Move disk 2 from pole {} to pole {}'.format(start, target))
		print('Move disk 1 from pole {} to pole {}'.format(temp, target))
	else:
		hanoi_solve(no_disk-1, start, target, temp)
		print('Move disk {} from pole {} to pole {}'.format(no_disk, start, target))
		hanoi_solve(no_disk-1, temp, start, target)

########## DON'T EDIT CODES BELOW ##########
hanoi_solve(int(input()),input(),input(),input())
