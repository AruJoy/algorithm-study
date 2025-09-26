from sys import stdin
from collections import deque
from heapq import heapify, heappop, heappush
input = stdin.readline
INF = float("INF")

def main():
    numbers, length = map(int, input().split())
    number_list = list(map(int, input().split()))
    que = deque()
    answer = []
    for i in range(numbers):
        while que and que[-1][0] > number_list[i]:
            que.pop()
        que.append((number_list[i], i))
        if que[0][1] <= i - length:
            que.popleft()
        answer.append(que[0][0])
    print(*answer)
    return
if __name__ == "__main__":
    main()