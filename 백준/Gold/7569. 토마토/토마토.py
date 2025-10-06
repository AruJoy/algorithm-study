from sys import stdin
input = stdin.readline
from collections import deque
INF = float("inf")


def main():
    columns, rows, heights = map(int, input().split())
    container = list()
    good_tomatoes = list()
    bad_tomatoes = 0
    for i in range(heights):
        surface = list()
        for j in range(rows):
            row = list(map(int, input().split()))
            for k in range(columns):
                if row[k] == 1:
                    good_tomatoes.append((i, j, k))
                    continue
                if row[k] == 0:
                    bad_tomatoes += 1
            surface.append(row)
        container.append(surface)
    if bad_tomatoes == 0:
        print(0)
        return
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    que = deque()
    day = 0
    for z, y, x in good_tomatoes:
        que.append((z, y, x, 0))
    while que and bad_tomatoes > 0:
        while que:
            if que[0][3] != day:
                break
            cur_z, cur_y, cur_x, cur_day = que.popleft()
            for i in range(6):
                z, y, x = cur_z + dz[i], cur_y + dy[i], cur_x + dx[i]
                if(0 <= z < heights
                    and 0 <= y < rows
                    and 0 <= x < columns
                    and container[z][y][x] == 0):
                    container[z][y][x] = 1
                    bad_tomatoes -= 1
                    que.append((z, y, x, cur_day + 1))
        day += 1
    
    print(-1 if bad_tomatoes > 0 else day)
    return
if __name__ == "__main__":
    main()