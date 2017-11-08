def print_matrix(matrix):
    for row in matrix:
        for i in row:
            print('{:.5f}'.format(i),end = ' ')
        print()
def elim(row1, row2, col):
    row_tmp = [i*row2[col]/row1[col] for i in row1]
    return [row2[i] - row_tmp[i] for i in range(0,len(row2))]
def row_echelon(matrix):
    for i in range(len(matrix)-1):
        for j in range(i+1,len(matrix)):
            matrix[j] = elim(matrix[i],matrix[j],i)
    return matrix
def input_matrix():
    return [[float(i) for i in input().split(' ')] for i in range(int(input('How many row?: ')))]
matrix = input_matrix()
matrix = row_echelon(matrix)
print_matrix(matrix)
