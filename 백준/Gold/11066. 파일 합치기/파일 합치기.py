from sys import stdin
input = stdin.readline
from collections import deque

def merge(chapter, c_list):
    dp = [[[0, 0] for _ in range(chapter)]for __ in range(chapter)]
    prefix = [0 for i in range(chapter+1)]
    for i in range(chapter):
        prefix[i+1] = prefix[i]+c_list[i]
    for c in range(chapter):
        dp[c][c][1] = c-1
    for dx in range(1, chapter):
        for y in range(chapter - dx):
            dp[y][y+dx][0] = 2147483647
            start = dp[y][y+dx-1][1]
            end = dp[y+1][y+dx][1]
            file = prefix[y+dx+1] - prefix[y]
            for i in range(start, end+1):
                time = dp[y][i][0] + dp[i+1][y+dx][0] + file
                if time < dp[y][y+dx][0]:
                    dp[y][y+dx][0] = time
                    dp[y][y+dx][1] = i
    return dp[0][chapter-1][0]
def main():
    t_count = int(input().strip())
    for _ in range(t_count):
        chapter = int(input().strip())
        c_list = list(map(int, input().split()))
        print(merge(chapter, c_list))
    return

if __name__ == "__main__":
    main()