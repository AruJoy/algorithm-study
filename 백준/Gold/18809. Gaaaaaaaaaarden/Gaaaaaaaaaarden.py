from sys import stdin
input = stdin.readline
from collections import deque
INF = float("INF")
def simulate(garden, color_map, rows, columns, cur_green, cur_red):
    for y in range(rows):
        for x in range(columns):
            color_map[y][x] = 0
    ans = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    red_que = deque()
    green_que = deque()
    for y, x in cur_green:
        green_que.append((y,x,1))
        color_map[y][x] = 1
    for y, x in cur_red:
        red_que.append((y, x, -1))
        color_map[y][x] = -1
    move = 1
    while red_que and green_que:
        while green_que:
            if not green_que or green_que[0][2] != move:
                break
            cur_y, cur_x, cur_move = green_que.popleft()
            if color_map[cur_y][cur_x] != cur_move:
                continue
            for i in range(4):
                y, x = cur_y + dy[i], cur_x + dx[i]
                if (y < 0 or rows-1 < y
                    or x < 0 or columns-1 < x
                    or garden[y][x] == 0
                    or color_map[y][x] != 0):
                    continue
                green_que.append((y, x, cur_move+1))
                color_map[y][x] = cur_move + 1
        while red_que:
            if not red_que or red_que[0][2] != -move:
                break
            cur_y, cur_x, cur_move = red_que.popleft()
            if color_map[cur_y][cur_x] != cur_move:
                continue
            for i in range(4):
                y, x = cur_y + dy[i], cur_x + dx[i]
                if (y < 0 or rows-1 < y
                    or x < 0 or columns-1 < x
                    or garden[y][x] == 0):
                    continue
                if color_map[y][x] + cur_move -1 == 0:
                    ans += 1
                    color_map[y][x] = INF
                    continue
                if color_map[y][x] != 0:
                    continue
                red_que.append((y, x, cur_move - 1))
                color_map[y][x] = cur_move - 1
        move += 1
    if ans == 10:
        ans = 10
    return ans
def place_red(garden, color_map, seed_point, rows, columns, n_green, n_red, cur_green, cur_red, index):
    ans = 0
    if len(cur_red) == n_red:
        return simulate(garden, color_map, rows, columns, cur_green, cur_red)
    if len(seed_point) - index < n_red - len(cur_red):
        return 0
    else:
        for i in range(index, len(seed_point)):
            if seed_point[i] in cur_green:
                continue
            cur_red.append(seed_point[i])
            ans = max(ans, place_red(garden, color_map, seed_point, rows, columns, n_green, n_red, cur_green, cur_red, i+1))
            cur_red.pop()
    return ans
def place_green(garden, color_map, seed_point, rows, columns, n_green, n_red, cur_green, index):
    ans = 0
    if len(cur_green) == n_green:
        return place_red(garden, color_map, seed_point, rows, columns, n_green, n_red, cur_green, list(), 0)
    if len(seed_point) - index < n_green - len(cur_green):
        return 0
    else:
        for i in range(index, len(seed_point)):
            cur_green.append(seed_point[i])
            ans = max(ans, place_green(garden, color_map, seed_point, rows, columns, n_green, n_red, cur_green, i+1))
            cur_green.pop()
    return ans
def main():
    rows, columns, n_green, n_red = map(int, input().split())
    garden = list()
    seed_point = list()
    color_map = [[0 for _ in range(columns)] for __ in range(rows)]
    for i in range(rows):
        row = list(map(int, input().split()))
        for j in range(columns):
            if row[j] == 2:
                seed_point.append((i, j))
        garden.append(row)
    print(place_green(garden, color_map, seed_point, rows, columns, n_green, n_red, list(), 0))
    return
if __name__ == "__main__":
    main()