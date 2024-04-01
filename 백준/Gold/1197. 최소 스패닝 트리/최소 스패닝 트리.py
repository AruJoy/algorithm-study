from sys import stdin
from heapq import heappop, heappush
V, E = stdin.readline().split(' ')
V = int(V)
E = int(E)
vertex = [list() for i in range(V +1)]
for i in range(E):
    edge = stdin.readline().split(' ')
    heappush(vertex[int(edge[0])], [(int(edge[2])), int(edge[1])])
    heappush(vertex[int(edge[1])], [(int(edge[2])), int(edge[0])])

current_node = 1
ans = 10**9
visited = [False for i in range(V+1)]
visited[current_node] = True


que = list()
for weight, next_node in vertex[current_node]:
    heappush(que, (weight, next_node))

weight_sum = 0

while que:
    node_weight, next_node = heappop(que)
    if not visited[next_node]:
        visited[next_node] = True
        weight_sum += node_weight
        for weight, node in vertex[next_node]:
            heappush(que, (weight, node))

print(weight_sum)