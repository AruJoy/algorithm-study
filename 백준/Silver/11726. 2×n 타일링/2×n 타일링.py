from sys import stdin
input = stdin.readline

def main():
    length = int(input().strip())
    dp = [0 for _ in range(length)]
    dp[0] = 1
    if length>1:
        dp[1] = 1
    for i in range(length-1):
        dp[i+1] += dp[i]
        dp[i+1] = dp[i+1] % 10007 
        if length - i > 2:
            dp[i+2] += dp[i]
            dp[i+2] = dp[i+2] % 10007 
    print(dp[-1])
    return
if __name__ == "__main__":
    main()