from sys import stdin
from collections import deque
from heapq import heappop, heappush, heapify

def dijkstra(adj, start):
    distance[start] = 0
    min_distance = list()
    min_distance.append([0, start])

    while min_distance:
        current_distance, current_city = heappop(min_distance)
        if current_distance > distance[current_city]:
            continue
        for next_city in adj[current_city]:
            if distance[next_city] > current_distance + 1:
                distance[next_city] = current_distance + 1
                heappush(min_distance, (distance[next_city], next_city))

cities, edges, target_distance, start = map(int, stdin.readline().split(' '))
distance = [10**9 for _ in range(cities+1)]
adj = [list() for i in range(cities+1)]
for i in range(edges):
    S, E = map(int, stdin.readline().split(' '))
    adj[S].append(E)
dijkstra(adj, start)
if distance.count(target_distance) == 0:
    print(-1)
else:
    for city in range(len(distance)):
        if distance[city] == target_distance:
            print(city)