from sys import stdin
from collections import deque
input = stdin.readline
INF = float("INF")

def put_paper(board, y, x, size):
    for i in range(size):
        for j in range(size):
            if board[y + i][x + j] == 0:
                return False, i, j
            board[y + i][x + j] = 0
    return True, size, size + 1
def restore_paper(board, start_y, start_x, size, dy, dx):
    for i in range(size):
        for j in range(size):
            if i == dy and j == dx:
                return
            board[start_y + i][start_x + j] = 1
    return
def put_papers(paper_list, board, cur_y, cur_x):
    paper_size = [5, 4, 3, 2, 1]
    min_answer = INF
    all_0 = True
    for i in range(cur_y, 10):
        for j in range(cur_x if i == cur_y else 0, 10):
            if board[i][j] == 1:
                all_0 == False
                for k in range(5):
                    size = paper_size[k]
                    if 10 - i < size or 10 - j < size or paper_list[k] == 0:
                        continue
                    success, y, x = put_paper(board, i, j, size)
                    if success:
                        paper_list[k] -= 1
                        result = put_papers(paper_list, board, i, j)
                        paper_list[k] += 1
                        if result != -1:
                            answer = 1 + result
                            min_answer = min(min_answer, answer)
                    restore_paper(board, i, j, size, y, x)
                if min_answer == INF:
                    return -1
                return min_answer
            if i == 9 and j == 9:
                if all_0:
                    return 0
    return -1 if min_answer == INF else min_answer

def main():
    paper_list = [5 for _ in range(5)]
    board = []
    for i in range(10):
        row = list(map(int, input().split()))
        board.append(row)
    print(put_papers(paper_list, board, 0, 0))
    return
if __name__ == "__main__":
    main()