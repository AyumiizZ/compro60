people_per_boat = int(input())
weight_per_boat = int(input())
people_in_group = 0
current_boat_weight = 0
group = 0

while (True) :
	people = int(input())
	if (people == -1):
		break
	weight_per_people = float(input())
	if (weight_per_people == -1):
		break
	while people > 0:
		if current_boat_weight + weight_per_people > weight_per_boat or people_in_group == people_per_boat:
			group += 1
			current_boat_weight = 0
			people_in_group = 0
		people_in_group += 1
		people -= 1
		current_boat_weight += weight_per_people
if current_boat_weight > 0 :
	group += 1		
print(group)
