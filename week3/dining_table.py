def dining(customer):
	table = 1
	while table < customer:
		customer //= table
		table += 1
	return table
print(dining(int(input())))
