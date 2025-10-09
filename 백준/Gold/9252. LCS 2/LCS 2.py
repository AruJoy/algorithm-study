from sys import stdin
input = stdin.readline
INF = float("inf")

def find_LCS(first_str, second_str):
    n, m = len(first_str), len(second_str)
    dp = [[0 for _ in range(m+1)] for __ in range(n+1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if first_str[i - 1] == second_str[j - 1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    answer = list()
    i = n
    j = m
    # for row in dp:
    #     print(*row)
    while dp[i][j] > 0:
        if first_str[i-1] == second_str[j-1]:
            answer.append(first_str[i-1])
            i -= 1
            j -= 1
            continue
        if dp[i-1][j] >= dp[i][j - 1]:
            i -= 1
            continue
        j -= 1
    answer.reverse()
    print(dp[n][m])
    if dp[n][m] > 0:
        print("".join(answer))
    return

def main():
    first_str = list(input().strip())
    second_str = list(input().strip())
    find_LCS(first_str, second_str)
    return

if __name__ == "__main__":
    main()