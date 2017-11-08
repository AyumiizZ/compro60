# # sol 1
# i = 0
# k = 1
# temp = k
# while i <= 144 :
#     print (i ,end = ' ')
#     i,k = k,i+k
# print ()

# # sol 2
# def fibo(n):
#     return n if n < 2 else fibo(n-1)+fibo(n-2)
# print(' '.join([str(fibo(i)) for i in range(0,14)]))

# sol 3
fibo = lambda n: n if n < 2 else fibo(n-1) + fibo(n-2)
print(' '.join([str(fibo(i)) for i in range(0,13)]))