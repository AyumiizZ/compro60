inp = [float(i) for i in input().split(' ')]
print('AV:{:.2f} MAX:{:.2f} MIN:{:.2f}'.format(sum(inp)/len(inp),max(inp),min(inp)))