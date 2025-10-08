from sys import stdin
input = stdin.readline
from collections import deque
INF = float("inf")

def find_path(rows, columns, n_break, board):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited_list = [[0 for __ in range(columns)]
                    for ___ in range(rows)]
    bit_list = list()
    bit = 1 << n_break
    cur_bit = 0
    for i in range(n_break+1):
        cur_bit = cur_bit | bit
        bit_list.append(cur_bit)
        bit =  bit >> 1
    bit_list.reverse()
    visited_list[0][0] = bit_list[0]
    
    que = deque()
    que.append((0, 0, 0, 1))
    while que:
        cur_y, cur_x, cur_break, cur_move = que.popleft()
        for i in range(4):
            y, x = cur_y + dy[i], cur_x + dx[i]
            if not (0 <= y < rows and 0 <= x < columns):
                continue
            if y == rows - 1 and x == columns -1:
                return cur_move + 1
            
            if board[y][x] == 1:
                if (cur_break >= n_break or visited_list[y][x] & (1 << (cur_break + 1))):
                    continue
                if cur_move % 2 == 0:
                    que.append((cur_y, cur_x, cur_break, cur_move+1))
                    continue
                visited_list[y][x] = bit_list[cur_break + 1]
                que.append((y, x, cur_break+1, cur_move+1))
                continue
            
            if visited_list[y][x] & (1 << cur_break):
                continue
            visited_list[y][x] = bit_list[cur_break]
            que.append((y, x, cur_break, cur_move + 1))
    return -1

def main():
    rows, columns, n_break = map(int, input().split())
    board = list()
    for _ in range(rows):
        board.append(list(map(int, input().strip())))
    if rows == 1 and columns == 1:
        print(1)
        return
    print(find_path(rows, columns, n_break, board))
    return
if __name__ == "__main__":
    main()