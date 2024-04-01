from sys import stdin
from collections import deque

def bipartiteGraph():
    V,E = map(int, stdin.readline().split(' '))
    vertex = [list() for i in range(V+1)]
    node_label = [None for i in range(V+1)]
    node_label[0] = 0
    for i in range(E):
        node1, node2 = map(int, stdin.readline().split(' '))
        vertex[node2].append(node1)
        vertex[node1].append(node2)
    for start in range(1, V+1):
        if node_label[start] == None:
            node_label[start] = 1
            stack = deque()
            current_node = start
            current_node_label = node_label[start]
            
            for edge in vertex[start]:
                if node_label[edge] == None:
                    node_label[edge] = -current_node_label
                    stack.append(edge)
                while stack:
                    current_node = stack.pop()
                    current_node_label = node_label[current_node]
                    for edge in vertex[current_node]:
                        if node_label[edge] == None:
                            node_label[edge] = - current_node_label
                            stack.append(edge)
                        elif current_node_label == node_label[edge]:
                            return False
    return True

number_of_test = int(stdin.readline())
result_set = list()
for t in range(number_of_test):
    result_set.append(bipartiteGraph())
for i in result_set:
    if i == True:
        print('YES')
    else:
        print('NO')