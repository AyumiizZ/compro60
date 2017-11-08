town = [[int(i) for i in input().split(' ')] for j in range(int(input('Size of town: ')))]
even = [0]
def print_town(town):
    for row in town:
        for i in row:
            print(i,end = ' ')
        print()
while even[0] != 'END':
    even = [i for i in input('Event: ').split(',')]
    if even[0] == 'EARTHQUAKE':
        for i in range(int(even[2])):
            for j in range(int(even[2])):
                if int(even[3]) + i < len(town) and int(even[4]) + j < len(town):
                    town[int(even[3])+i][int(even[4])+j] -= int(even[1])
                    if town[int(even[3])+i][int(even[4])+j] < 0:
                        town[int(even[3])+i][int(even[4])+j] = 0
    if even[0] == 'GOVERNMENT':
        if even[2] == 'C':
            for i in range(len(town)):
                if town[i][int(even[3])] != 0:
                    town[i][int(even[3])] += int(even[1])
        if even[2] == 'R':
            for i in range(len(town)):
                if town[int(even[3])][i] != 0:
                    town[int(even[3])][i] += int(even[1])
print('The result is')
print_town(town)
    
            