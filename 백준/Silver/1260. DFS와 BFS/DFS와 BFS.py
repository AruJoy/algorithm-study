from sys import stdin
from heapq import heappush, heappop
V, E, start = map(int, stdin.readline().split(' '))
vertex = [list() for i in range(V + 1)]
dfs = []
bfs = []
found = [False for i in range (V + 1)]
for i in range(E):
    node1, node2 = map(int, stdin.readline().split(' '))
    vertex[node1].append(node2)
    vertex[node2].append(node1)
for node in vertex:
    node.sort()

que = []
bfs.append(start)
found[start] = True
for next_node in vertex[start]:
    que.append(next_node)
while que:
    next_node = que.pop(0)
    if not found[next_node]:
        found[next_node] = True
        bfs.append(next_node)
        for nodes in vertex[next_node]:
            que.append(nodes)

stack = []
for i in range(len(found)):
    found[i] = False

def df_search(current_node):
    if not found[current_node]:
        found[current_node] = True
        dfs.append(current_node)
        for node in vertex[current_node]:
            df_search(node)
df_search(start)

for i in dfs:
    print(i, end=' ')
print()
for i in bfs:
    print(i, end=' ')
print()