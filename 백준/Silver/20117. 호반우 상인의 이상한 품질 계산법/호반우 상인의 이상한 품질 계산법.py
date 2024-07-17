from sys import stdin
from collections import deque
input = stdin.readline

def ho_ban_woo(n_cow):
    cow_list = list(map(int, input().split(' ')))
    cow_list.sort()

    count = 0
    length = len(cow_list)
    index = (length + 1)//2
    count += sum(cow_list[index:length])*2
    if length % 2 :
        count += cow_list[length // 2]

    return count

n_cow = int(input())

print(ho_ban_woo(n_cow))