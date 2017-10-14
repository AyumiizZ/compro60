new_soilder_bee = int(input())
new_work_bee = int(input())
year = int(input())
while year > 0:
	year -= 1
	soilder_bee = new_soilder_bee
	work_bee = new_work_bee
	new_soilder_bee = work_bee
	new_work_bee = work_bee + soilder_bee + 1
	kill = int(input())
	if kill > soilder_bee:
		kill -= soilder_bee
		if kill > work_bee:
			kill -= work_bee
			if kill > new_soilder_bee:
				kill -= new_soilder_bee
				new_soilder_bee = 0
				if kill > new_work_bee:
					new_work_bee = 0
				else:
					new_work_bee -= kill
			else:
				new_soilder_bee -= kill

print(new_work_bee)
print(new_soilder_bee)
