from sys import stdin
from collections import deque
from heapq import heappop, heappush

def find_min_cost(adj, start_city):
    cost[start_city] = 0
    current_city = start_city
    min_heap = list()
    min_heap.append([0, current_city])
    
    while min_heap:
        min_cost, current_city = heappop(min_heap)
        for bus_charge, next_city in adj[current_city]:
            if cost[next_city] < min_cost:
                continue
            if  min_cost + bus_charge < cost[next_city]:
                cost[next_city] = min_cost + bus_charge
                heappush(min_heap, [cost[next_city], next_city])
    return

cities = int(stdin.readline())
bus_lines = int(stdin.readline())
adj = [list() for i in range(cities + 1)]
cost = [2*(10**9) for i in range(cities + 1)]
for bus_line in range(bus_lines):
    start_city, end_city, bus_charge = map(int, stdin.readline().split(' '))
    heappush(adj[start_city], [bus_charge, end_city])
start_city, end_city = map(int, stdin.readline().split(' '))

find_min_cost(adj, start_city)
print(cost[end_city])