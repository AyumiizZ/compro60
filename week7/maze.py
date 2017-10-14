maze_map = [list(input()) for i in range(int((input().split(' ')[0])))]
def find_path(
'''
def find_path(x,y,path):
	if x < 0 or y < 0 or x >= len(maze_map) or y >= len(maze_map[0]): return
	if maze_map[x][y] == 'F': print(path)
	if maze_map[x][y] != ' ' and maze_map[x][y] != 'I': return
	maze_map[x][y] = 'pass'
	
	find_path(x-1,y,path+'U')
	find_path(x+1,y,path+'D')
	find_path(x,y-1,path+'L')
	find_path(x,y+1,path+'R')
	maze_map[x][y] = ' '
'''	
find_path(0,maze_map[0].index('I'),'')
