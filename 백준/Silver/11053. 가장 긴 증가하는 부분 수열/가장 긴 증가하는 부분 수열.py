from sys import stdin

def LIS(sequence, length_of_sequence):
    dp = [1] * length_of_sequence
    for i in range(1, length_of_sequence):
        for j in range(i):
            if sequence[i] > sequence[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

length_of_sequence = int(stdin.readline())
sequence = list(map(int, stdin.readline().split(' ')))