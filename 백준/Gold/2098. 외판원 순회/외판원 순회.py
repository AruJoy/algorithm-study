from sys import stdin
input = stdin.readline
from collections import deque
max_val = 10**9
def tsp(scale, w_map, dp, mask, before_i, last):
    min_val = max_val
    if dp[before_i][mask] != -1:
        return dp[before_i][mask]
    for i in range(1, scale):
        bit = 1 << (i-1)
        if w_map[before_i][i] == 0: 
            continue
        if mask & bit:
            continue
        cost = 0
        if dp[i][mask|bit] != -1:
            cost = w_map[before_i][i] + dp[i][mask|bit]
        else: 
            cost = w_map[before_i][i] + tsp(scale, w_map, dp, mask|bit, i, last)
        min_val = min(min_val, cost)
    dp[before_i][mask] = min_val
    return min_val
def main():
    scale = int(input().strip())
    w_map = []
    for _ in range(scale):
        w_map.append(list(map(int, input().split())))
    last = (1 << (scale-1))-1
    dp = [[-1 for _ in range(last+1)] for __ in range(scale)]
    for i in range(scale):
        dp[i][-1] = w_map[i][0] if w_map[i][0] != 0 else max_val
    print(tsp(scale, w_map, dp, 0, 0, last))
    return

if __name__ == "__main__":
    main()