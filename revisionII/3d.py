
A = [2,3,7,4,1]
B = [1,2,5,6,9,8]

def union(A,B):
    return sorted(A + [i for i in B if i not in A])
def intersect(A,B):
    return sorted([i for i in A if i in B])
def difference(A,B):
    return sorted([i for i in A if i not in B])
def print_int_list(A):
    print(' '.join([str(i) for i in A]))
print_int_list(union(A,B))
print_int_list(intersect(A,B))
print_int_list(difference(A,B))