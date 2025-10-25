from collections import deque
from sys import stdin
input = stdin.readline


def main():
    n_number, n_remove = map(int, input().split())
    number = list(map(int, input().strip()))
    stack = list()
    for num in number:
        while n_remove and stack and stack[-1] < num:
            stack.pop()
            n_remove -= 1
        stack.append(num)

    if n_remove > 0:
        stack = stack[:-n_remove]
    print("".join(map(str, stack)))
    return


if __name__ == "__main__":
    main()
