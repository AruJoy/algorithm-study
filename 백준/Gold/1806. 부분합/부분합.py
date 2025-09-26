from sys import stdin
from collections import deque
input = stdin.readline
INF = float("INF")

def main():
    length, lo = map(int, input().split())
    numbers = list(map(int, input().split()))
    sum_list = [0 for _ in range(length)]
    sum_list[0] = numbers[0]
    for i in range(1,length):
        sum_list[i] = sum_list[i-1]+numbers[i]
    if sum_list[0] >= lo or sum_list[length-1] - sum_list[length-2] >= lo:
        print(1)
        return
    if sum_list[-1] < lo:
        print(0)
        return
    answer = INF
    i = 1
    j = 0
    while i < length:
        while sum_list[i] - sum_list[j] >= lo:
            answer = min(i - j, answer)
            j += 1
        i += 1
    print(length if answer == INF else answer)
    return
if __name__ == "__main__":
    main()