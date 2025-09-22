from sys import stdin
input = stdin.readline
from collections import deque
def get_input():
    columns, rows = map(int, input().split(" "))
    maze = []
    for _ in range(rows):
        row = list(map(int, input().strip()))
        maze.append(row)
    return columns, rows, maze

def solution(columns, rows, maze):
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]
    bfs_map = [[False for _ in range(columns)] for __ in range(rows)]
    bfs_map[0][0] = 0
    que = deque()
    que.append((0, 0, 0))
    while(que):
        c_y, c_x, count = que.popleft()
        for i in range(4):
            y = c_y + dy[i]
            x = c_x + dx[i]
            if y == rows-1 and x == columns-1:
                return count
            if ( y < 0 or rows-1 < y
                or x < 0 or columns-1 < x
                or bfs_map[y][x]):
                continue
            if maze[y][x] == 1:
                bfs_map[y][x] = True
                que.append((y, x, count + 1))
                continue
            bfs_map[y][x] = count
            bfs_map[y][x] = True
            que.appendleft((y, x, count))
    return 0
columns, rows, maze = get_input()
print(solution(columns, rows, maze))