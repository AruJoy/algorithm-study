from sys import stdin
input = stdin.readline
from collections import deque
def find_index(lis, value):
    lo = 0
    hi = len(lis)-1
    while lo < hi:
        mi = (lo+hi)//2
        if lis[mi] < value:
            lo = mi + 1
        else:
            hi = mi
    return lo
def repair(pos, sequence, parent):
    result = []
    cur = pos[-1]
    while cur != -1:
        result.append(sequence[cur])
        cur = parent[cur]
    return result[::-1]
def main():
    length = int(input().strip())
    sequence = list(map(int, input().split()))
    lis = [sequence[0]]
    pos = [0]
    parent = [-1 for _ in range(length)]
    for i in range(1, length):
        value = sequence[i]
        if value > lis[-1]:
            parent[i] = pos[-1] if pos else -1
            lis.append(value)
            pos.append(i)
            continue
        index = find_index(lis, sequence[i])
        lis[index] = value
        pos[index] = i
        parent[i] = pos[index-1] if index > 0 else -1
    original_lis = repair(pos, sequence, parent)
    print(len(lis))
    print(*original_lis)
    return

if __name__ == "__main__":
    main()
