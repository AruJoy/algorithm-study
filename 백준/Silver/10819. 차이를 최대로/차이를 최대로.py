from sys import stdin
input = stdin.readline

def get_input():
    numbers = int(input().strip())
    num_list = list(map(int, input().split(" ")))
    return numbers, num_list
def solution(numbers, num_list, sequence, dp, depth):
    if depth == numbers:
        sum = 0
        for i in range(numbers - 1):
            sum += abs(sequence[i] - sequence[i + 1])
        return sum
    answer = 0
    for i in range(numbers):
        if not dp[i]:
            sequence.append(num_list[i])
            dp[i] = True
            answer = max(answer, solution(numbers, num_list, sequence, dp, depth+1))
            sequence.pop()
            dp[i] = False
    return answer

numbers, num_list = get_input()
sequence = []
dp = [False for _ in range(numbers)]
print(solution(numbers, num_list, sequence, dp, 0))