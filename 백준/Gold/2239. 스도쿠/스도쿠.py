from sys import stdin
input = stdin.readline
from collections import deque
INF = float("inf")
def get_answer(sudoku, row_list, column_list, block_list, index):
    if index == 81:
        return True
    y, x = index // 9, index % 9 
    block_index = (y//3)*3 + x//3
    if sudoku[y][x] != 0:
        return get_answer(sudoku, row_list, column_list, block_list, index+1)
    for i in range(9):
        if row_list[y][i] or column_list[x][i] or block_list[block_index][i]:
            continue
        row_list[y][i] = True
        column_list[x][i] = True
        block_list[block_index][i] = True
        sudoku[y][x] = i + 1
        if(get_answer(sudoku, row_list, column_list, block_list, index+1)):
            return True
        row_list[y][i] = False
        column_list[x][i] = False
        block_list[block_index][i] = False
        sudoku[y][x] = 0
    return False

def main():
    sudoku = list()
    for _ in range(9):
        sudoku.append(list(map(int, input().strip())))
    row_list = [[ False for _ in range(9) ] for __ in range(9)]
    column_list = [[ False for _ in range(9) ] for __ in range(9)]
    block_list = [[ False for _ in range(9) ] for __ in range(9)]
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                continue
            row_list[i][sudoku[i][j] - 1] = True
            column_list[j][sudoku[i][j] - 1] = True
            block_index = (i//3)*3 + j//3
            block_list[block_index][sudoku[i][j] - 1] = True
    get_answer(sudoku, row_list, column_list, block_list, 0)
    for row in sudoku:
        print("".join(map(str,row)))
    return

if __name__ == "__main__":
    main()