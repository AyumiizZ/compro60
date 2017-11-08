inp = [0]
while inp[len(inp)-1] != '':
    inp.append(input('Enter student score (or ENTER to finish): '))
inp = [int(i) for i in inp[1:len(inp)-1]]
tmp = [i for i in inp]
while inp != []:
    print('STD{:02d}: {}'.format(tmp.index(max(inp))+1, max(inp)))
    inp.remove(max(inp))