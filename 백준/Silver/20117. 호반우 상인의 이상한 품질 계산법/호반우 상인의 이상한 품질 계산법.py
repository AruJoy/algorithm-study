from sys import stdin
from collections import deque
input = stdin.readline

def ho_ban_woo(n_cow):
    cow_list = list(map(int, input().split(' ')))
    cow_list.sort()
    cow_list = deque(cow_list)

    count = 0
    while cow_list:
        count += cow_list[len(cow_list)//2]
        cow_list.popleft()

    return count

n_cow = int(input())

print(ho_ban_woo(n_cow))