from sys import stdin
from collections import deque
input = stdin.readline

def decode(pass_word):
    if pass_word[0] == 0:
        return 0
    if len(pass_word) == 1:
        return 1
    length = len(pass_word)
    dp = [0 for _ in range(length)]
    if pass_word[-1] != 0:
        dp[-1] = 1
    if pass_word[-2] != 0:
        if pass_word[-1] != 0:
            dp[-2] += 1
        if pass_word[-2]*10 + pass_word[-1] <= 26:
            dp[-2] += 1
    for i in range(length-3, -1, -1):
        count = 0
        if pass_word[i] != 0:
            if pass_word[i+1] != 0:
                count += dp[i+1]
        if pass_word[i] != 0 and pass_word[i]*10 + pass_word[i+1] <= 26:
            count += dp[i+2]
        dp[i] = count % 1000000
    return dp[0]

def main():
    pass_word = list(map(int, input().strip()))
    print(decode(pass_word))
    return
if __name__ == "__main__":
    main()