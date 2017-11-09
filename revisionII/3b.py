def print_matrix(matrix):
    if matrix != []:
        for row in matrix:
            for i in row:
                print('{:.3f}'.format(i),end = ' ')
            print()
    else:
        print('ERROR')
def trans(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    ##OR
    # return zip(*matrix)
def plus(A,B):
    try:
        return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    except:
        return []
def minus(A,B):
    try:
        return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    except:
        return []
def mul(A,B):
    try:
        tmp = [[0 for i in range(len(B[0]))] for j in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    tmp[i][j] += A[i][k] * B[k][j]
        return tmp
    except:
        return []
def cmul(c,A):
    return [[c*A[i][j] for j in range(len(A[0]))] for i in range(len(A))]
A = [
    [7.7, 7.1, 1.0, 9.3], 
    [2.7, 1,6, 8.9, 4.7], 
    [4.0, 5.3, 8.2, 0.5]
]
B = [
    [7.0, 7.1, 5.1, 5.9],
    [1.4, 4.3, 2.2, 0.7],
    [8.0, 8.1, 4.0, 6.4],
    [1.8, 8.8, 1.2, 7.7]
]
C = [
    [1.7, 7.7, 0.1],
    [5.6, 9.1, 5.1],
    [2.0, 0.8, 5.5],
    [3.2, 2.7, 5.8]
]
print_matrix(cmul(2,A))
print('------')
print_matrix(trans(A))
print('------')
print_matrix(plus(trans(A),C))
print('------')
print_matrix(minus(trans(A),C))
print('------')
print_matrix(plus(cmul(2,trans(A)),minus(cmul(3,C),trans(mul(A,B)))))