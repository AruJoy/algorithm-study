from sys import stdin
from heapq import heappush, heappop
V, E= map(int, stdin.readline().split(' '))
vertex = [list() for i in range(V+1)]
found = [False for i in range (V+1)]
found[0] = True
for i in range(E):
    node1, node2 = map(int, stdin.readline().split(' '))
    vertex[node1-1].append(node2)
    vertex[node2-1].append(node1)
for node in vertex:
    node.sort()

def bfs(start):
    que = []
    found[start] = True
    for next_node in vertex[start]:
        que.append(next_node)
    while que:
        next_node = que.pop(0)
        if not found[next_node]:
            found[next_node] = True
            for nodes in vertex[next_node]:
                que.append(nodes)
count = 0
while False in found:
    for i in range(len(found)):
        if found[i] == False:
            bfs(i)
            count += 1

print(count)