from sys import stdin
input = stdin.readline
MOD = 1000000007
from collections import deque
def union(union_number, board, s_y, s_x, rows, columns):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    que = deque()
    board[s_y][s_x] = union_number
    que.append((s_y,s_x))
    count = 1
    while que:
        cur_y, cur_x = que.popleft()
        for i in range(4):
            y, x = cur_y + dy[i], cur_x + dx[i]
            if (y < 0 or rows-1 < y
                or x < 0 or columns-1 < x
                or board[y][x] != 0):
                continue
            board[y][x] = union_number
            count += 1
            que.append((y,x))
    return count
def get_count(board, union_list, s_y, s_x, rows, columns):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    count = 1
    merge_set = set()
    for i in range(4):
        y, x = s_y + dy[i], s_x + dx[i]
        if (y < 0 or rows-1 < y
            or x < 0 or columns-1 < x
            or board[y][x] < 2
            or board[y][x] in merge_set):
            continue
        count += union_list[board[y][x]]
        merge_set.add(board[y][x])
    return count
def main():
    rows, columns = map(int, input().split())
    board = list()
    for _ in range(rows):
        board.append(list(map(int,input().strip())))
    union_list = dict()
    union_number = 2
    for i in range(rows):
        for j in range(columns):
            if board[i][j] != 0:
                continue
            count = union(union_number, board, i, j, rows, columns)
            union_list[union_number] = count
            union_number += 1
    answer = list()
    for i in range(rows):
        row = list()
        for j in range(columns):
            if board[i][j] != 1:
                row.append(0)
                continue
            row.append(get_count(board, union_list, i, j, rows, columns)%10)
        answer.append(row)
    for row in answer:
        print("".join(map(str, row)))
    return

if __name__ == "__main__":
    main()