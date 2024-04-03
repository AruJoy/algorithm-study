from sys import stdin
from collections import deque
from heapq import heappop, heappush

def find_min_cost():
    start_node = [0,0]
    que = deque([start_node])
    
    while que:
        current_coordinate = que.popleft()
        y = current_coordinate[0]
        x = current_coordinate[1]
        if 0 < y:
            if maze[y-1][x] == 0:
                que.append([y-1,x])
                maze[y-1][x] = maze[y][x]+board[y][x]
            elif maze[y][x]+1 < maze[y-1][x]:
                maze[y-1][x] = maze[y][x]+board[y][x]
                que.append([y-1,x])
        if y < columns-1:
            if maze[y+1][x] == 0:
                que.append([y+1,x])
                maze[y+1][x] = maze[y][x]+board[y][x]
            elif maze[y][x]+1 < maze[y+1][x]:
                maze[y+1][x] = maze[y][x]+board[y][x]
                que.append([y+1,x])
        if 0 < x:
            if maze[y][x-1] == 0:
                que.append([y,x-1])
                maze[y][x-1] = maze[y][x]+board[y][x]
            elif maze[y][x]+1 < maze[y][x-1]:
                maze[y][x-1] = maze[y][x]+board[y][x]
                que.append([y,x-1])
        if x < columns-1:
            if maze[y][x+1] == 0:
                que.append([y,x+1])
                maze[y][x+1] = maze[y][x]+board[y][x]
            elif maze[y][x]+1 < maze[y][x+1]:
                maze[y][x+1] = maze[y][x]+board[y][x]
                que.append([y,x+1])

columns = int(stdin.readline())
board = list()
maze = [[0 for i in range(columns)] for i in range(columns)]
for column in range(columns):
    line =list(map(int, stdin.readline().rstrip()))
    for room in range(columns):
        if line[room] == 0:
            line[room] = 10000
    board.append(line)

find_min_cost()
print(maze[columns - 1][columns - 1] // 10000)
