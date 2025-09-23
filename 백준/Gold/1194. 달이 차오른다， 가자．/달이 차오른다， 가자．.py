from sys import stdin
from collections import deque
input = stdin.readline
INF = float("INF")

def find_exit(rows, columns, maze, start_y, start_x):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited_list = [[[False for _ in range(64)] for __ in range(columns)] for ___ in range(rows)]
    key_map = {'a':1, 'b':1<<1, 'c':1<<2, 'd':1<<3, 'e':1<<4, 'f':1<<5,
                'A':1, 'B':1<<1, 'C':1<<2, 'D':1<<3, 'E':1<<4, 'F':1<<5}
    que = deque()
    visited_list[start_y][start_x][0] = True
    que.append((start_y, start_x, 0, 0))
    while que:
        cur_y, cur_x, mask, cur_move = que.popleft()
        for i in range(4):
            y, x = cur_y + dy[i], cur_x + dx[i]
            if (0 <= y < rows and 0 <= x < columns):
                if maze[y][x] == '#':
                    continue
                if maze[y][x] == '1':
                    return cur_move +1
                new_mask = mask
                if (maze[y][x] != '.'):
                    if (maze[y][x].lower() == maze[y][x]):
                        key_mask = key_map[maze[y][x]]
                        new_mask = mask | key_mask
                    else:
                        key_mask = key_map[maze[y][x]]
                        if not mask & key_mask:
                            continue
                if visited_list[y][x][new_mask]:
                    continue
                visited_list[y][x][new_mask] = True
                que.append((y, x, new_mask, cur_move + 1))
    return -1
def main():
    rows, columns = map(int, input().split())
    maze = []
    start_y, start_x = 0, 0
    for i in range(rows):
        row = list(input().strip())
        for j in range(columns):
            if row[j] == '0':
                start_y, start_x = i, j
                row[j] = '.'
        maze.append(row)
    print(find_exit(rows, columns, maze, start_y, start_x))
    return
if __name__ == "__main__":
    main()