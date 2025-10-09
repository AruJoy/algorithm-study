from sys import stdin
input = stdin.readline
INF = float("inf")

def tiling(columns):
    dp = [0 for _ in range(columns+1)]
    dp[0] = 1
    for i in range(2, columns+1):
        if 2 <= i:
            dp[i] += dp[i-2]*3
        if i % 2 == 0:
            j = i-4
            add = 0
            while 0 <= j:
                add += dp[j]
                j -= 2
            dp[i] += 2 * add
    return dp[columns]

def main():
    columns = int(input().strip())
    print(tiling(columns))
    return

if __name__ == "__main__":
    main()