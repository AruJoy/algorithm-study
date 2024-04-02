from sys import stdin
from collections import deque

def find_hub():
    node_is_checked = [False for node in range(number_of_nodes + 1)]
    node_is_checked[0] = True
    hub_list = list()
    hub_number = 0
    global line_walk_way
    for node in range(1, number_of_nodes+1):
        if vertex_is_indoor[node] == 1:
            for edge in vertex[node]:
                if vertex_is_indoor[edge] == 1:
                    line_walk_way += 1
        else:
            hub_list.append(list())
            if not node_is_checked[node]:
                stack = deque()
                if vertex_is_indoor[node] == 0:
                    hub_list[hub_number].append(node)
                    node_is_checked[node] = True
                    for edge in vertex[node]:
                        if vertex_is_indoor[edge] == 0:
                            stack.append(edge)
                while stack:
                    edge = stack.pop()
                    if vertex_is_indoor[edge] == 0:
                        hub_list[hub_number].append(edge)
                        node_is_checked[edge] = True
                        for next_edge in vertex[edge]:
                            if vertex_is_indoor[next_edge] == 0 and node_is_checked[next_edge] == False:
                                stack.append(next_edge)
            hub_number += 1
    return hub_list

line_walk_way = 0
number_of_nodes = int(stdin.readline())
vertex = [list() for i in range(number_of_nodes + 1)]
vertex_is_indoor = [0]
vertex_is_indoor.extend(list(map(int, stdin.readline().rstrip())))
for _ in range(number_of_nodes - 1):
    node1, node2 =map(int, stdin.readline().split(' '))
    vertex[node1].append(node2)
    vertex[node2].append(node1)
hub_list = find_hub()
for hub in hub_list:
    apex = 0
    for node in hub:
        for edge in vertex[node]:
            if vertex_is_indoor[edge] == 1:
                apex += 1
    walk_way_combination = apex * (apex-1)
    line_walk_way += walk_way_combination
print(line_walk_way)