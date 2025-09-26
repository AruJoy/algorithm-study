from sys import stdin
from collections import deque
from heapq import heapify, heappop, heappush
input = stdin.readline
INF = float("INF")

def main():
    numbers, length = map(int, input().split())
    number_list = list(map(int, input().split()))
    heap = []
    que = deque()
    remove_list = dict()
    answer = []
    for i in range(length):
        heappush(heap, number_list[i])
        que.append(number_list[i])
        answer.append(heap[0])
    for i in range(length, numbers):
        pop_number = que.popleft()
        if pop_number in remove_list.keys():
            remove_list[pop_number] += 1
        else:
            remove_list[pop_number] = 1
        while heap and heap[0] in remove_list.keys():
            remove_list[heap[0]] -= 1
            if remove_list[heap[0]] == 0:
                remove_list.pop(heap[0])
            heappop(heap)
        heappush(heap, number_list[i])
        que.append(number_list[i])
        answer.append(heap[0])
    print(*answer)
    return
if __name__ == "__main__":
    main()