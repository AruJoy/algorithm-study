from sys import stdin
input = stdin.readline
from collections import deque

def play(board, archer_positions, total_enemy, rows, columns, a_range):
    dy = [0, -1, 0]
    dx = [-1, 0, 1]
    cur_enemy = total_enemy
    ans = 0
    while cur_enemy > 0:
        kill_list = set()
        for archer_p in archer_positions:
            visited_list = [[False for _ in range(columns)] for __ in range(rows)]
            que = deque()
            que.append((rows, archer_p, 1))
            min_range = 40
            find_enemy = list()
            while que:
                cur_y, cur_x, cur_r = que.popleft()
                if cur_r >= min_range:
                    break
                for i in range(3):
                    y, x = cur_y + dy[i], cur_x + dx[i]
                    if (y < 0 or rows-1 < y
                        or x < 0 or columns-1 < x
                        or visited_list[y][x]):
                        continue
                    if board[y][x] == 1:
                        find_enemy.append((x,y))
                        min_range = min(cur_r+1, min_range)
                    if cur_r < a_range:
                        que.append((y, x, cur_r+1))
            if find_enemy:
                find_enemy.sort()
                kill_list.add((find_enemy[0][1], find_enemy[0][0]))
        for y, x in kill_list:
            board[y][x] = 0
            ans += 1
            cur_enemy -= 1
        row = board.pop()
        cur_enemy -= sum(row)
        board.appendleft([0 for _ in range(columns)])
    
    return ans

def place_archer(board, total_enemy, rows, columns, a_range):
    ans = 0
    for i in range(columns):
        for j in range(i+1, columns):
            for k in range(j+1, columns):
                ans = max(ans, play(deque([row[:] for row in board]), [i, j, k], total_enemy, rows, columns, a_range))
    
    return ans
def main():
    rows, columns, a_range = map(int, input().split())
    board = deque()
    total_enemy = 0
    for _ in range(rows):
        row = list(map(int, input().split()))
        for s in row:
            if s == 1:
                total_enemy += 1
        board.append(row)
    print(place_archer(board, total_enemy, rows, columns, a_range))
    return
if __name__ == "__main__":
    main()