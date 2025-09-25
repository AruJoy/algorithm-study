from sys import stdin
from collections import deque
input = stdin.readline
INF = float("INF")

def bfs(board, v_list, block, s_y, s_x):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    que = deque()
    que.append((s_y, s_x))
    block_list = [(s_y, s_x)]
    while que:
        cur_y, cur_x = que.popleft()
        for i in range(4):
            y, x = cur_y + dy[i], cur_x + dx[i]
            if(0 <= y <= 11 and 0 <= x <= 5
                and not v_list[y][x] and board[y][x] == block):
                v_list[y][x] = True
                block_list.append((y,x))
                que.append((y,x))
    return block_list
def delete_block(board, y, x, blocks):
    x_set = set()
    for y, x in blocks:
        board[y][x] = '.'
        x_set.add(x)
    
    for x in x_set:
        perfect = False
        while not perfect:
            perfect = True
            for i in range(11, 0, -1):
                if board[i][x] == "." and board[i-1][x] != ".":
                    board[i][x], board[i-1][x] = board[i-1][x], board[i][x]
                    perfect = False
    return

def puyo(board):
    v_list = [[False for _ in range(6)]for __ in range(12)]
    block_list = []
    for y in range(11, -1, -1):
        for x in range(5, -1, -1):
            v_list[y][x] = True
            if board[y][x] == '.':
                continue
            block = board[y][x]
            result = bfs(board, v_list, block, y, x)
            if len(result) > 3:
                block_list = block_list + result
    if block_list:
        delete_block(board, y, x, block_list)
        return True
    return False
def main():
    board = []
    answer = 0
    for _ in range(12):
        board.append(list(input().strip()))
    while (puyo(board)):
        answer+=1
    print(answer)
    return
if __name__ == "__main__":
    main()