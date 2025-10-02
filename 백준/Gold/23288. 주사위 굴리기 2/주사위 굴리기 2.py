from sys import stdin
input = stdin.readline
from collections import deque
def mark_score(board, score_board, rows, columns, s_y, s_x, dy, dx):
    multi = board[s_y][s_x]
    count = 1
    union_list = [(s_y, s_x)]
    score_board[s_y][s_x] = -1
    que = deque()
    que.append((s_y, s_x))
    while que:
        cur_y, cur_x = que.popleft()
        for i in range(4):
            y, x = cur_y + dy[i], cur_x + dx[i]
            if (y < 0 or rows-1 < y
                or x < 0 or columns - 1 < x
                or score_board[y][x] != 0
                or board[y][x] != multi):
                continue
            count += 1
            score_board[y][x] = -1
            union_list.append((y, x))
            que.append((y,x))
    score = multi * count
    for y, x in union_list:
        score_board[y][x] = score
    return
    
def change_position(d_position, direction):
    # 0 1 2 3 4 5 
    # U B R L F D
    if direction == 0:
        (d_position[0], d_position[1],
        d_position[2], d_position[3],
        d_position[4], d_position[5]
        ) = (
        d_position[3], d_position[1],
        d_position[0], d_position[5],
        d_position[4], d_position[2])
        return
    if direction == 1:
        (d_position[0], d_position[1],
        d_position[2], d_position[3],
        d_position[4], d_position[5]
        ) = (
        d_position[1], d_position[5],
        d_position[2], d_position[3],
        d_position[0], d_position[4])
        return
    if direction == 2:
        (d_position[0], d_position[1],
        d_position[2], d_position[3],
        d_position[4], d_position[5]
        ) = (
        d_position[2], d_position[1],
        d_position[5], d_position[0],
        d_position[4], d_position[3])
        return
    (d_position[0], d_position[1],
    d_position[2], d_position[3],
    d_position[4], d_position[5]
    ) = (
    d_position[4], d_position[0],
    d_position[2], d_position[3],
    d_position[5], d_position[1])
    return
def reflect(board, score_board, dice, d_position, dy, dx, cur):
    cur[2] = (cur[2] + 2) % 4
    nxt_y, nxt_x = cur[0] + dy[cur[2]], cur[1] + dx[cur[2]]
    change_position(d_position, cur[2])
    cur[0], cur[1] = nxt_y, nxt_x
    cur_point = board[nxt_y][nxt_x]
    bottom = dice[d_position[5]]
    if bottom > cur_point:
        cur[2] = (cur[2] + 1) % 4
    if bottom < cur_point:
        cur[2] = (cur[2] + 3) % 4
    return score_board[nxt_y][nxt_x]
def roll_dice(board, score_board, dice, d_position, rows, columns, dy, dx, cur):
    nxt_y, nxt_x = cur[0] + dy[cur[2]], cur[1] + dx[cur[2]]
    if (nxt_y < 0 or rows-1 < nxt_y
        or nxt_x < 0 or columns - 1 < nxt_x):
        return reflect(board, score_board, dice, d_position, dy, dx, cur)
    
    change_position(d_position, cur[2])
    cur[0], cur[1] = nxt_y, nxt_x
    cur_point = board[nxt_y][nxt_x]
    bottom = dice[d_position[5]]
    if bottom > cur_point:
        cur[2] = (cur[2] + 1) % 4
    if bottom < cur_point:
        cur[2] = (cur[2] + 3) % 4
        
    return score_board[nxt_y][nxt_x]
def main():
    dice = [1, 2, 3, 4, 5, 6]
    d_position = [0, 1, 2, 3, 4, 5]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    cur = [0, 0, 0]
    rows, columns, move = map(int, input().split())
    board = list()
    ans = 0
    score_board = [[0 for _ in range(columns)]for __ in range(rows)]
    for _ in range(rows):
        board.append(list(map(int, input().split())))
    
    for i in range(rows):
        for j in range(columns):
            if score_board[i][j] == 0:
                mark_score(board, score_board, rows, columns, i, j, dy, dx)
    
    for _ in range(move):
        score = roll_dice(board, score_board, dice, d_position, rows, columns, dy, dx, cur)
        ans += score
    print(ans)
    return
if __name__ == "__main__":
    main()