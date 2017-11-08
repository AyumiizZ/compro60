inp = [0]
while inp[len(inp)-1] != '':
    inp.append(input('Enter student score (or ENTER to finish): '))
inp = [int(i) for i in inp[1:len(inp)-1]]
print('\n'.join(['STD{:02d} score: {}'.format(i+1,inp[i]) for i in range(0,len(inp))]))
print('Average score is {:.2f}\nMinimum score is {}\nMaximum score is {}'.format(sum(inp)/len(inp),min(inp),max(inp)))