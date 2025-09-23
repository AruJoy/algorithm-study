from sys import stdin
input = stdin.readline

def main():
    n = int(input().strip())
    w_map = [list(map(int, input().split())) for _ in range(n)]

    INF = 10**9
    FULL = (1 << n) - 1
    dp = [[INF] * (1 << n) for _ in range(n)]

    dp[0][1] = 0

    for mask in range(1 << n):
        for u in range(n):
            if dp[u][mask] == INF:
                continue
            for v in range(n):
                if mask & (1 << v):
                    continue
                if w_map[u][v] == 0:
                    continue
                next_mask = mask | (1 << v)
                dp[v][next_mask] = min(dp[v][next_mask],
                                        dp[u][mask] + w_map[u][v])

    ans = INF
    for u in range(n):
        if w_map[u][0] != 0:
            ans = min(ans, dp[u][FULL] + w_map[u][0])

    print(ans)

if __name__ == "__main__":
    main()
