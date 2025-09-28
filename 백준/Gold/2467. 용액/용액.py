from sys import stdin
input = stdin.readline
from collections import deque
INF = float("INF")

def main():
    length = int(input().strip())
    number_list = list(map(int, input().split()))
    a, b = -1, -1
    i = 0
    j = length-1
    answer = abs(number_list[j] + number_list[i])
    a, b = number_list[i], number_list[j]
    while i < j:
        cur_diff = abs(number_list[j] + number_list[i])
        nxt_diff_1 = abs(number_list[j-1] + number_list[i])
        nxt_diff_2 = abs(number_list[j] + number_list[i+1])
        if cur_diff < answer:
            a, b = number_list[i], number_list[j]
            answer = cur_diff
        if nxt_diff_1 > nxt_diff_2:
            i += 1
            continue
        j -= 1
    print(a, b)
    return
if __name__ == "__main__":
    main()