from sys import stdin
from collections import deque
from heapq import heappop, heappush
columns, rows = map(int, stdin.readline().split(' '))
maze = list()

for i in range(columns):
    maze.append(list(map(int, stdin.readline().rstrip())))
def find_path(maze):
    start_node = [0,0]
    que = deque([start_node])
    
    while que:
        current_coordinate = que.popleft()
        y = current_coordinate[0]
        x = current_coordinate[1]
        if 0 < y:
            if maze[y-1][x] == 1:
                que.append([y-1,x])
                maze[y-1][x] = maze[y][x]+1
            elif maze[y][x]+1 < maze[y-1][x]:
                maze[y-1][x] = maze[y][x]+1
                que.append([y-1,x])
        if y < columns-1:
            if maze[y+1][x] == 1:
                que.append([y+1,x])
                maze[y+1][x] = maze[y][x]+1
            elif maze[y][x]+1 < maze[y+1][x]:
                maze[y+1][x] = maze[y][x]+1
                que.append([y+1,x])
        if 0 < x:
            if maze[y][x-1] == 1:
                que.append([y,x-1])
                maze[y][x-1] = maze[y][x]+1
            elif maze[y][x]+1 < maze[y][x-1]:
                maze[y][x-1] = maze[y][x]+1
                que.append([y,x-1])
        if x < rows-1:
            if maze[y][x+1] == 1:
                que.append([y,x+1])
                maze[y][x+1] = maze[y][x]+1
            elif maze[y][x]+1 < maze[y][x+1]:
                maze[y][x+1] = maze[y][x]+1
                que.append([y,x+1])

find_path(maze)
print(maze[columns-1][rows-1])