from sys import stdin
input = stdin.readline
from collections import deque

INF = 10**9
def find_coors(rows, columns, start_y, start_x, pipe_map, visited_list):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    pipe = {"|": [2, 3], "-": [0, 1], "+": [0, 1, 2, 3],
            "1": [1, 3], "2": [1, 2], "3": [0, 2], "4": [0, 3]}
    visited_list[start_y][start_x] = True
    que = deque()
    que.append((start_y, start_x))
    while que:
        cur_y, cur_x = que.popleft()
        if pipe_map[cur_y][cur_x] == "M" or pipe_map[cur_y][cur_x] == "Z":
            for i in range(4):
                y = cur_y + dy[i]
                x = cur_x + dx[i]
                if (y < 0 or rows-1 < y
                    or x < 0 or columns-1 <x
                    or visited_list[y][x]
                    or pipe_map[y][x] == "."):
                    continue
                visited_list[y][x] = True
                que.append((y, x))
            continue
        delta_list = pipe[pipe_map[cur_y][cur_x]]
        for i in delta_list:
            y = cur_y + dy[i]
            x = cur_x + dx[i]
            if (y < 0 or rows-1 < y
                or x < 0 or columns-1 <x
                or visited_list[y][x]):
                continue
            if pipe_map[y][x] == '.':
                return y, x
            visited_list[y][x] = True
            que.append((y, x))
    return -1, -1

def find_lose(rows, columns, pipe_map, start, end):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited_list = [[False for _ in range(columns)] for __ in range(rows)]
    lose_y, lose_x = find_coors(rows, columns, start[0], start[1], pipe_map, visited_list)
    if lose_y == -1 or lose_x == -1:
        lose_y, lose_x = find_coors(rows, columns, end[0], end[1], pipe_map, visited_list)
    
    l_list = []
    pipe = {"|": [2, 3], "-": [0, 1], "+": [0, 1, 2, 3],
            "1": [1, 3], "2": [1, 2], "3": [0, 2], "4": [0, 3]}
    key_list = list(pipe.keys())
    for i in range(4):
        y = lose_y + dy[i]
        x = lose_x + dx[i]
        if (y < 0 or rows-1 < y
            or x < 0 or columns-1 < x):
            continue
        if pipe_map[y][x] == "M" or pipe_map[y][x] == "Z":
            continue
        if pipe_map[y][x] != ".":
            if i in pipe[pipe_map[y][x]]:
                if i % 2 == 0:
                    i += 1
                else: i -= 1
                l_list.append(i)
    for key_i in range(len(key_list)-1, -1, -1):
        if len(pipe[key_list[key_i]]) != len(l_list):
            key_list.pop(key_i)
            continue
        for i in l_list:
            if not i in pipe[key_list[key_i]]:
                key_list.pop(key_i)
                break
    return lose_y+1, lose_x+1, key_list[0]
def main():
    rows, columns = map(int, input().split())
    pipe_map = []
    start = []
    end = []
    for i in range(rows):
        row = list(input().strip())
        pipe_map.append(row)
        for j in range(columns):
            if row[j] == "M":
                start.append(i)
                start.append(j)
                break
            if row[j] == "Z":
                end.append(i)
                end.append(j)
                break
    answer = list(find_lose(rows, columns, pipe_map, start, end))
    print(*answer)
    return

if __name__ == "__main__":
    main()