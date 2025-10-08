from sys import stdin
input = stdin.readline
from collections import deque
INF = float("inf")

def main():
    n, m, k = map(int, input().split())
    total_count = 1
    for i in range(m):
        total_count *= n - i
        total_count /= i+1
    hit_count = 0
    for hit in range(k, m+1):
        cur = 1
        for j in range(hit):
            cur *= m - j
            cur /= j + 1
        for j in range(m - hit):
            cur *= n - m - j
            cur /= j + 1
        hit_count += cur
    print(hit_count/total_count)
    return
if __name__ == "__main__":
    main()