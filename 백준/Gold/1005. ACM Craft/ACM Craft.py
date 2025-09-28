from sys import stdin
input = stdin.readline
from collections import deque
import sys
sys.setrecursionlimit(10**9)

def build(target, time_table, bf_list, dp):
    load = 0
    for before in bf_list[target]:
        if before in dp:
            load = max(load, dp[before])
            continue
        load = max(load, build(before, time_table, bf_list, dp))
    dp[target] = load+ time_table[target]
    return dp[target]
def main():
    t_count = int(input().strip())
    for _ in range(t_count):
        dp = dict()
        count, edges = map(int, input().split())
        time_table = list(map(int, input().split()))
        bf_list = [[] for _ in range(count)]
        for __ in range(edges):
            before, after = map(int, input().split())
            bf_list[after-1].append(before-1)
        target = int(input().strip())-1
        print(build(target, time_table, bf_list, dp))
    return
if __name__ == "__main__":
    main()