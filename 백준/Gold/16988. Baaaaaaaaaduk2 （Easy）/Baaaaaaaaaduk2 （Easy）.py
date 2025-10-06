from sys import stdin
input = stdin.readline
from collections import deque
INF = float("inf")

def simulate(rows, columns, board, place_points, visited_list):
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]
    
    ans = 0
    for y, x in place_points:
        board[y][x] = 1
    
    for seek_y, seek_x in place_points:
        for i in range(4):
            start_y, start_x = seek_y + dy[i], seek_x + dx[i]
            if (start_y < 0 or rows - 1 < start_y
                or start_x < 0 or columns - 1 < start_x
                or visited_list[start_y][start_x] or board[start_y][start_x] != 2):
                continue
            cur_count = 1
            que = deque()
            que.append((start_y, start_x))
            visited_list[start_y][start_x] = True
            is_survive = False
            while que:
                cur_y ,cur_x = que.popleft()
                for j in range(4):
                    y, x = cur_y + dy[j], cur_x + dx[j]
                    if (y < 0 or rows-1 < y
                        or x < 0 or columns-1 < x
                        or visited_list[y][x]):
                        continue
                    if board[y][x] == 0:
                        is_survive = True
                    if board[y][x] == 2:
                        cur_count += 1
                        visited_list[y][x] = True
                        que.append((y, x))
            if not is_survive:
                ans += cur_count
    
    for y, x in place_points:
        board[y][x] = 0
    for i in range(rows):
        for j in range(columns):
            visited_list[i][j] = False
    return ans
def main():
    rows, columns = map(int, input().split())
    board = list()
    place_points = list()
    for i in range(rows):
        row = list(map(int, input().split()))
        for j in range(columns):
            if row[j] == 0:
                place_points.append((i, j))
        board.append(row)
    visited_list = [[False for _ in range(columns)] for __ in range(rows)]
    ans = 0
    if len(place_points) == 1:
        print(simulate(rows, columns, board, [place_points[0]], visited_list))
        return
    for i in range(len(place_points)):
        for j in range(i+1, len(place_points)):
            ans = max(ans, simulate(rows, columns, board, [place_points[i], place_points[j]], visited_list))
    print(ans)
    return
if __name__ == "__main__":
    main()