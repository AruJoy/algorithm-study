from sys import stdin
from collections import deque
from heapq import heappush, heappop
V = int(stdin.readline())
E = int(stdin.readline())
vertex = [list() for i in range(V+1)]
found = [False for i in range(V+1)]
found[0] = True
for i in range(E):
    node1, node2 = map(int, stdin.readline().split(' '))
    vertex[node1].append(node2)
    vertex[node2].append(node1)

def bfs(start):
    global count
    queue = deque([start])
    found[start] = True

    while queue:
        v = queue.popleft()
        for i in vertex[v]:
            if not found[i]:
                queue.append(i)
                found[i] = True
                count += 1
count = 0


bfs(1)
print(count)