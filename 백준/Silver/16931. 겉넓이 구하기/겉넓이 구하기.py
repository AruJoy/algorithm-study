from sys import stdin
input = stdin.readline
from collections import deque

def main():
    rows, columns = map(int, input().split())
    blocks = []
    for _ in range(rows):
        blocks.append(list(map(int, input().split())))
    answer = 2 * rows * columns
    for i in range(rows):
        for j in range(columns):
            if i == 0:
                answer += blocks[i][j]
            if i == rows-1: 
                answer += blocks[i][j]
            if j == 0:
                answer += blocks[i][j]
            if j == columns-1: 
                answer += blocks[i][j]
            if i < rows-1:
                answer += abs( blocks[i][j]- blocks[i+1][j] )
            if j < columns-1:
                answer += abs( blocks[i][j]- blocks[i][j+1] )
    print(answer)
    return

if __name__ == "__main__":
    main()