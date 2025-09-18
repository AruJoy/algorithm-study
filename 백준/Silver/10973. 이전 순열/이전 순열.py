from sys import stdin
import sys
sys.setrecursionlimit(10**5)
input = stdin.readline

def get_input():
    numbers = int(input().strip())
    sequence = list(map(int, input().split(" ")))
    return numbers, sequence
def solution(numbers, sequence):
    i = numbers - 2
    while i >= 0 and sequence[i] <= sequence[i+1]:
        i -= 1

    if i < 0:
        print(-1)
    else:
        j = numbers - 1
        while sequence[j] >= sequence[i]:
            j -= 1
        sequence[i], sequence[j] = sequence[j], sequence[i]

        sequence[i+1:] = reversed(sequence[i+1:])
        print(*sequence)
        return

numbers, sequence = get_input()
solution(numbers, sequence)