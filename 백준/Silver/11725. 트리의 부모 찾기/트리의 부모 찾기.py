from sys import stdin
from collections import deque
V = int(stdin.readline())
initValue = 0
node_level = [None for i in range(V+1)]
vertex = [list() for i in range(V+1)]
for i in range(V-1):
    node1, node2 = map(int, stdin.readline().split(' '))
    vertex[node2].append(node1)
    vertex[node1].append(node2)
node_level[0] = 0
node_level[1] = 0

que = deque()
current_node = 1
for i in vertex[1]:
    que.append([1,i])
while que:
    current_node, nextNode = que.popleft()
    if not node_level[nextNode]:
        node_level[nextNode] = node_level[current_node] + 1
        for i in vertex[nextNode]:
            que.append([nextNode,i])
node_level[1] = 0
for i in range (2, V+1):
    for node in vertex[i]:
        if node_level[node] < node_level[i]:
            print(node)