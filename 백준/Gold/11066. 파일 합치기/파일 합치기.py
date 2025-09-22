from sys import stdin
input = stdin.readline
from collections import deque

def merge(chapter, c_list):
    dp = [[[-1, 0] for _ in range(chapter)]for __ in range(chapter)]
    for c in range(chapter):
        dp[c][c][0] = c_list[c]
    for dx in range(1, chapter):
        for y in range(chapter - dx):
            min_time = 2147483647
            file = dp[y][y+dx-1][0] + dp[y+dx][y+dx][0]
            for i in range(dx):
                min_time = min(min_time, dp[y][y+i][1] + dp[y+1+i][y+dx][1] + file)
            dp[y][y+dx][0] = file
            dp[y][y+dx][1] = min_time 
    return dp[0][chapter-1][1]
def main():
    t_count = int(input().strip())
    for _ in range(t_count):
        chapter = int(input().strip())
        c_list = list(map(int, input().split()))
        print(merge(chapter, c_list))
    return

if __name__ == "__main__":
    main()