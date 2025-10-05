from sys import stdin
input = stdin.readline
from collections import deque


def main():
    n = int(input().strip())
    num_list = list(map(int, input().split()))
    stack = deque()
    answer = list()
    for i in range(n-1, -1, -1):
        while stack and stack[-1] <= num_list[i]:
            stack.pop()
        if not stack:
            answer.append(-1)
            stack.append(num_list[i])
            continue
        answer.append(stack[-1])
        stack.append(num_list[i])
    answer.reverse()
    print(*answer)
    return
if __name__ == "__main__":
    main()