from sys import stdin
input = stdin.readline

def attach(n, board):
    if n == 1:
        return max(board[0][0], board[1][0])

    dp = [[0]*n for _ in range(2)]
    dp[0][0], dp[1][0] = board[0][0], board[1][0]
    dp[0][1] = board[1][0] + board[0][1]
    dp[1][1] = board[0][0] + board[1][1]

    for j in range(2, n):
        dp[0][j] = max(dp[1][j-1], dp[1][j-2]) + board[0][j]
        dp[1][j] = max(dp[0][j-1], dp[0][j-2]) + board[1][j]

    return max(dp[0][n-1], dp[1][n-1])

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        board = [list(map(int, input().split())) for _ in range(2)]
        print(attach(n, board))

if __name__ == "__main__":
    main()
