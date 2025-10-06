from sys import stdin
input = stdin.readline
from collections import deque

def main():
    columns, rows = map(int, input().split())
    box = list()
    good_tomatoes = list()
    bad_tomatoes = 0
    for i in range(rows):
        row = list(map(int, input().split()))
        for j in range(columns):
            if row[j] == 1:
                good_tomatoes.append((i, j))
                continue
            if row[j] == 0:
                bad_tomatoes += 1
        box.append(row)
    if bad_tomatoes == 0:
        print(0)
        return
    que = deque()
    time = 0
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]
    for y, x in good_tomatoes:
        que.append((y, x, 0))
    while que and bad_tomatoes > 0:
        while que:
            if que[0][2] != time:
                break
            cur_y, cur_x, cur_time = que.popleft()
            for i in range(4):
                y, x = cur_y + dy[i], cur_x + dx[i]
                if (0 <= y < rows
                    and 0 <= x < columns
                    and box[y][x] == 0):
                    box[y][x] = 1
                    bad_tomatoes -= 1
                    que.append((y, x, cur_time + 1))
        time += 1
        if bad_tomatoes == 0:
            print(time)
            return
    print(-1)
    return
if __name__ == "__main__":
    main()