from sys import stdin
input = stdin.readline
from collections import deque
INF = float("inf")
def main():
    n_number = int(input().strip())
    number_list = list(map(int, input().split()))
    number_list.sort()
    ans = INF
    ans_list = list()
    for i in range(n_number-2):
        lo = i + 1
        hi = n_number-1
        while lo < hi:
            value = number_list[i] + number_list[lo] + number_list[hi]
            if abs(value) < ans:
                ans = abs(value)
                ans_list = [number_list[i], number_list[lo], number_list[hi]]
            if value == 0:
                break
            if value < 0:
                lo += 1
                continue
            hi -= 1
        if ans == 0:
            break
    print(*ans_list)
    return

if __name__ == "__main__":
    main()