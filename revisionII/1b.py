inp = int(input())
print('\n'.join(['  '*(inp-i//2-1)+'**'*(2*(i//2)+1) for i in range(0,2*inp)]))
