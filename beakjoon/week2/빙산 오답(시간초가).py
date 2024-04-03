from sys import stdin
from collections import deque

def tears_of_the_antarctic():
    delete_list = list()
    for glacier in glacier_list:
        X,Y = coordinate[glacier]
        for x in range(X-1, X+2):
            if glacier_map[Y][x] == 0:
                vertex[glacier] = max(vertex[glacier]-1, 0)
        for y in range(Y-1, Y+2):
            if glacier_map[y][X] == 0:
                vertex[glacier] = max(vertex[glacier]-1, 0)
        if vertex[glacier] < 1:
            delete_list.append(glacier)
    for glacier in glacier_list:
        x,y = coordinate[glacier]
        glacier_map[y][x] = vertex[glacier]
    for delete in delete_list:
        glacier_list.remove(delete)
    linked = list()
    for i in range(len(vertex)):
        if i in glacier_list:
            linked.append(False)
        else:linked.append(True)
    if glacier_list:
        start = glacier_list[0]
        que = deque([start])
        linked[glacier_list[0]] = True
        while que:
            current_node = que.popleft()
            for next_node in adj[current_node]:
                if not linked[next_node]:
                    que.append(next_node)
                    linked[next_node] = True
    if False in linked:
        return False
    else: return True

column, row = map(int, stdin.readline().split(' '))
coordinate = list()
vertex = list()

adj = list()
glacier_map = list()
for y in range(column):
    line = list(map(int, stdin.readline().split(' ')))
    glacier_map.append(line)
    
    for x in range(len(line)):
        if line[x] != 0:
            adj.append(list())
            coordinate.append([x,y])
            vertex.append(line[x])#
            for point in range(len(coordinate)):
                check = coordinate[point]
                if check[1] == y and check[0] == x-1:
                    adj[point].append(len(vertex)-1)
                    adj[len(vertex)-1].append(point)
                elif check[1] == y-1 and check[0] == x:
                    adj[point].append(len(vertex)-1)
                    adj[len(vertex)-1].append(point)
                
glacier_list = [i for i in range(len(vertex))]
count = 0
condition = True
while condition:
    condition = tears_of_the_antarctic()
    count += 1
    if sum(vertex) == 0:
        count = 0
        condition = False

print(count)