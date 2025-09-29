from sys import stdin
import sys
sys.setrecursionlimit(1003)
input = stdin.readline
INF = float('INF')
def draw(n_house, cost_list):
    ans = INF
    for i in range(3):
        dp = [[INF for _ in range(3)] for __ in range(n_house)]
        dp[0][i] = cost_list[0][i]
        for j in range(1,n_house):
            for c in range(3):
                if j == n_house-1 and c == i:
                    continue
                cost = min(dp[j-1][c-1], dp[j-1][c-2])
                dp[j][c] = cost + cost_list[j][c]
            ans = min(ans, min(dp[n_house-1]))
    return ans
def main():
    n_house = int(input().strip())
    cost_list = []
    for _ in range(n_house):
        cost_list.append(list(map(int, input().split())))
    print(draw(n_house, cost_list))
    return

if __name__ == "__main__":
    main()
