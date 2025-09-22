from sys import stdin
input = stdin.readline

def attach(length, sticker_board):
    dp = [row[:] for row in sticker_board]
    dp[0][0] = sticker_board[0][0]
    dp[1][0] = sticker_board[1][0]
    for j in range(length-1):
        if length - j > 2:
            for i in range(2):
                dp[i][j+2] = max(dp[i][j+2], dp[i][j] + sticker_board[i][j+2])
                dp[1-i][j+2] = max(dp[1-i][j+2], dp[i][j] + sticker_board[1-i][j+2])
        for i in range(2):
            dp[1-i][j+1] = max(dp[1-i][j+1], dp[i][j] + sticker_board[1-i][j+1])
    return max(dp[0][length-1], dp[1][length-1])

def main():
    t_count = int(input().strip())
    for _ in range(t_count):
        sticker_board = []
        length = int(input().strip())
        for _ in range(2):
            sticker_board.append(list(map(int, input().split())))
        print(attach(length, sticker_board))
    return
if __name__ == "__main__":
    main()