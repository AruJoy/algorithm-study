from sys import stdin
from collections import deque

def is_bipartite(V, E, edges):
    graph = [[] for _ in range(V + 1)]
    for edge in edges:
        node1, node2 = edge
        graph[node1].append(node2)
        graph[node2].append(node1)

    colors = [0] * (V + 1)
    for i in range(1, V + 1):
        if colors[i] != 0:
            continue

        colors[i] = 1
        queue = deque([i])
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if colors[neighbor] == 0:
                    colors[neighbor] = -colors[node]
                    queue.append(neighbor)
                elif colors[neighbor] == colors[node]:
                    return False
    return True

number_of_tests = int(stdin.readline())
for _ in range(number_of_tests):
    V, E = map(int, stdin.readline().split())
    edges = [tuple(map(int, stdin.readline().split())) for _ in range(E)]
    if is_bipartite(V, E, edges):
        print('YES')
    else:
        print('NO')
