from sys import stdin
from collections import deque
input = stdin.readline


def main():
    count = int(input().strip())
    p_list = list(map(int, input().split()))
    answer = 0
    for i in range(count-1, -1, -1):
        if p_list[i] >= answer:
            answer = p_list[i]
            continue
        if answer%p_list[i] == 0:
            answer = ((answer//p_list[i])) * p_list[i]
            continue
        answer = ((answer//p_list[i])+1) * p_list[i]
    print(answer)
    return
if __name__ == "__main__":
    main()