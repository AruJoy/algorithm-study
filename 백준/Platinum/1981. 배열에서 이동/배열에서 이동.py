from sys import stdin
input = stdin.readline
from collections import deque
def bfs(scale, matrix, m, dx, dy, max_in_m, min_in_m):
    for low in range(min_in_m, max_in_m - m + 1):
        high = low + m
        if not (low <= matrix[0][0] <= high and
                low <= matrix[scale-1][scale-1] <= high):
            continue

        visited_list = [[False for _ in range(scale)] for __ in range(scale)]
        visited_list[0][0] = True
        que = deque()
        que.append((0,0))
        while que:
            cur_y, cur_x = que.popleft()
            for i in range(4):
                y, x = cur_y + dy[i], cur_x + dx[i]
                if (y < 0 or scale - 1 < y
                    or x < 0 or scale - 1 < x
                    or visited_list[y][x]):
                    continue
                if low <= matrix[y][x] <= high:
                    visited_list[y][x] = True
                    if y == scale-1 and x == scale-1:
                        return True
                    que.append((y, x))
    return False
def main():
    scale = int(input().strip())
    matrix = []
    for _ in range(scale):
        row = list(map(int, input().split()))
        matrix.append(row)
    min_val = min(min(row) for row in matrix)
    max_val = max(max(row) for row in matrix)
    lo, hi = 0, max_val - min_val
    max_in_m = max_val
    min_in_m = min_val
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]
    while True:
        m = (lo+hi)//2
        result = bfs(scale, matrix, m, dx, dy, max_in_m, min_in_m)
        if result:
            hi = m
        else:
            lo = m +1
        if lo == hi:
            break
    print (lo)
    return

if __name__ == "__main__":
    main()
