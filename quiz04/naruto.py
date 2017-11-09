max_life = life = int(input('Number of boruto\'s life: '))
Map = [[int(i) for i in input().split(',')] for j in range(int(input('Input Area Map:\nNumber of Area Map\'s row: ')))]
Round = int(input('Input Walk Path Map:\nNumber of Walk Path Map: '))
for r in range(Round):
    x_y = [int(i) for i in input('#'+str(r+1)+' Start position in Area Map: ').split(',')]
    minimap = [[int(i) for i in input().split(',')] for j in range(int(input('#'+str(r+1)+' Number of Path Map\'s row: ')))]
    for x in range(len(minimap)):
        for y in range(len(minimap[0])):
            if x_y[0] + x < len(Map) and x_y[1] + y < len(Map):
                life -= Map[x_y[0]+x][x_y[1]+y] and minimap[x][y]
    print('Boruto\'s status [ Life: {} of {} : {:.2f}% ]'.format(life,max_life,life/max_life*100) if life > 0 else 'Boruto\'s status [ Die ]')
