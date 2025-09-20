from sys import stdin
input = stdin.readline
from collections import deque
def main():
    rows, columns, dy, dx = map(int, input().split())
    matrix = []
    for _ in range(rows):
        matrix.append(list(map(int, input().split())))
    o_matrix = [[0 for _ in range(columns)] for __ in range(rows)]
    for i in range(dy):
        for j in range(columns):
            o_matrix[i][j] = matrix[i][j]
    for j in range(dx):
        for i in range(rows):
            o_matrix[i][j] = matrix[i][j]
    for i in range(rows - dy):
        for j in range(columns - dx):
            o_matrix[dy+i][dx+j] = matrix[dy+i][dx+j] - o_matrix[i][j]
    print("\n".join(" ".join(map(str, row))for row in o_matrix))
    return
if __name__ == "__main__":
    main()
