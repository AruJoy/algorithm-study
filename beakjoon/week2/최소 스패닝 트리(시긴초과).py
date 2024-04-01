from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)
from heapq import heappop, heappush
V, E = stdin.readline().split(' ')
V = int(V)
E = int(E)
vertex = [list() for i in range(V +1)]
visited = []
visited.append(1)
ans = 10**9

for i in range(E):
    edge = stdin.readline().split(' ')
    heappush(vertex[int(edge[0])], [(int(edge[2])), int(edge[1])])
    heappush(vertex[int(edge[1])], [(int(edge[2])), int(edge[0])])

def mst(n, value):
    global ans
    global visited
    
    if len(visited) == V:
        if value < ans:
            ans = value
    if not vertex[n]:
        return
    
    for j in range(len(vertex[n])):
        tmp_value = value
        tmp_visited = visited
        weight, go_to = heappop(vertex[n])
        if go_to in visited:
            continue
        else:
            value += weight
            visited.append(go_to)
            mst(go_to, value)
        if ans < 10**9:
            break
        value = tmp_value
        visited = tmp_visited

mst(1, 0)
print(ans)