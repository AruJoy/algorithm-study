from sys import stdin
input = stdin.readline
import sys
sys.setrecursionlimit(10**8)

def go_down(rows, columns, mountain, dp,
            cur_y, cur_x, dy, dx, cur_height, visited_list):
    if cur_y == rows-1 and cur_x == columns-1:
        return 1
    if dp[cur_y][cur_x] != -1:
        return dp[cur_y][cur_x]
    count = 0
    for i in range(4):
        y = cur_y + dy[i]
        x = cur_x + dx[i]
        if (0 <= y <= rows-1
            and 0 <= x <= columns-1
            and (not visited_list[y][x])
            and mountain[y][x] < cur_height):
            visited_list[y][x] = True
            count += go_down(rows, columns, mountain, dp,
                            y, x, dy, dx, mountain[y][x], visited_list)
            visited_list[y][x] = False
    dp[cur_y][cur_x] = count
    return count
def main():
    rows, columns = map(int, input().split())
    mountain = []
    for _ in range(rows):
        mountain.append(list(map(int, input().split())))
    dp = [[-1 for _ in range(columns)] for __ in range(rows)]
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]
    visited_list = [[False for _ in range(columns)] for __ in range(rows)]
    visited_list[0][0] = True
    print(go_down(rows, columns, mountain, dp, 0, 0, dy, dx, mountain[0][0], visited_list))
    return
if __name__ == "__main__":
    main()