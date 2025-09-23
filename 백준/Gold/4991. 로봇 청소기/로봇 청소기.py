from sys import stdin
input = stdin.readline
from collections import deque
def bfs(bfs_map, columns, rows, room, point_list, index, dy, dx):
    visited_list = [[False for _ in range(columns)]for __ in  range(rows)]
    start_y, start_x = point_list[index]
    que = deque()
    visited_list[start_y][start_x] = True
    que.append((start_y, start_x, 1))
    while que:
        cur_y, cur_x, cur_move = que.popleft()
        for i in range(4):
            y = cur_y + dy[i]
            x = cur_x + dx[i]
            if (y < 0 or rows-1 < y
                or x < 0 or columns-1 < x
                or visited_list[y][x]
                or room[y][x] == -2):
                continue
            visited_list[y][x] = True
            if room[y][x] >= 0:
                bfs_map[room[y][x]][index] = cur_move
                bfs_map[index][room[y][x]] = cur_move
            que.append((y, x, cur_move+1))
    return
def clean_up(dp, point_list, bfs_map, before_index, mask, last):
    if mask == last:
        return 0
    min_val = 2**31 - 1
    if dp[before_index][mask] != 2**31 - 1:
        return dp[before_index][mask]
    for i in range(len(point_list)):
        if i == 0 or i == before_index:
            continue
        bit = 1 << (i-1)
        if  mask & bit:
            continue
        result = clean_up(dp, point_list, bfs_map, i, mask | bit, last) + bfs_map[before_index][i]
        min_val = min(min_val, result)
    dp[before_index][mask] = min_val
    return min_val
    
def main():
    while True:
        columns, rows = map(int, input().split())
        if columns == 0 or rows == 0:
            break
        room = []
        point_list = []
        dust_index = 1
        for i in range(rows):
            row = list(input().strip())
            for j in range(columns):
                if row[j] == ".":
                    row[j] = -1
                if row[j] == "o":
                    row[j] = 0
                    point_list.insert(0, (i,j))
                if row[j] == "*":
                    row[j] = dust_index
                    dust_index += 1
                    point_list.append((i,j))
                if row[j] == "x":
                    row[j] = -2
            room.append(row)
        dy = [0, 0, -1, 1]
        dx = [-1, 1, 0, 0]
        bfs_map = [[-1 for _ in range(len(point_list))]for __ in range(len(point_list))]
        for i in range(len(point_list)):
            bfs_map[i][i] = 0
        for i in range(len(point_list)):
            bfs(bfs_map, columns, rows, room, point_list, i, dy, dx)
        disable = False
        for i in range(len(point_list)):
            if -1 in bfs_map[i]:
                disable = True
                break
        if disable:
            print(-1)
            continue
        dp = [[2**31-1 for _ in range(2**(len(point_list)-1))] for __ in range(len(point_list))]
        print(clean_up(dp, point_list, bfs_map, 0, 0, (1 << (len(point_list)-1)) - 1))
    return

if __name__ == "__main__":
    main()