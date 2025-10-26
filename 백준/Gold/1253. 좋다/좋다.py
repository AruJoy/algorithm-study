from collections import deque
from sys import stdin
input = stdin.readline


def test(cond_list, number):
    last_index = len(cond_list) - 1
    for i in range(last_index):
        lo = i + 1
        hi = last_index
        while lo <= hi:
            mid = (lo + hi) // 2
            result = cond_list[i] + cond_list[mid]
            if result == number:
                return True
            if result < number:
                lo = mid + 1
                continue
            hi = mid - 1
    return False


def main():
    n_number = int(input().strip())
    if n_number < 3:
        print(0)
        return
    ans = 0
    numbers = list(map(int, input().split()))
    numbers.sort()
    for i in range(n_number):
        if (test(numbers[:i] + numbers[i + 1:], numbers[i])):
            ans += 1
    print(ans)
    return


if __name__ == "__main__":
    main()
