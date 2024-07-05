from sys import stdin
import math
input = stdin.readline

def tiling(n):
    if n == 1: return 1
    if n == 2: return 3
    if n == 3: return 5
    dp = [0 for i in range(n+1)]
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n+1):
        dp[i] = 2*dp[i-2] + dp[i-1]
    return dp[n] % 10007

n = int(input())

print(tiling(n))