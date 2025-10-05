from sys import stdin
input = stdin.readline
from collections import deque
def main():
    rows, columns, timer = map(int, input().split())
    original = list()
    for _ in range(rows):
        original.append(input().strip())
    if timer == 1:
        for row in original:
            print("".join(row))
        return
    after_1 = [["O" for _ in range(columns)] for __ in range(rows)]
    after_2 = [["O" for _ in range(columns)] for __ in range(rows)]
    full = [["O" for _ in range(columns)] for __ in range(rows)]
    dx = [-1, 0, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]
    
    for i in range(rows):
        for j in range(columns):
            if original[i][j] == "O":
                for k in range(5):
                    y = i + dy[k]
                    x = j + dx[k]
                    if 0 <= x < columns and 0 <= y < rows:
                        after_1[y][x] = '.'
    for i in range(rows):
        for j in range(columns):
            if after_1[i][j] == "O":
                for k in range(5):
                    y = i + dy[k]
                    x = j + dx[k]
                    if 0 <= x < columns and 0 <= y < rows:
                        after_2[y][x] = '.'
    if timer%4 == 1:
        for row in after_2:
            print("".join(row))
        return
    if timer%4 == 3:
        for row in after_1:
            print("".join(row))
        return
    for row in full:
        print("".join(row))
    return
if __name__ == "__main__":
    main()