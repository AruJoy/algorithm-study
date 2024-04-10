from sys import stdin
from heapq import heappop, heappush
def revolving_salesman(n_of_cities, route):
    shortest_condition = dict()
    init_condition = dict()
    
    for i in range(n_of_cities):
        if i == 0:
            continue
        init_condition[i] = route[0][i]
    shortest_condition[1] = init_condition
    
    for remain_node in range(2, n_of_cities+1):
        before_conditions = shortest_condition[remain_node - 1]
        current_conditions = dict()
        for before_condition in before_conditions.keys():
            for current_city in range(n_of_cities):
                if (remain_node-1) == current_city:
                    continue
                
                if type(before_condition) == int:
                    remain_condition = [before_condition]
                else: remain_condition = list(before_condition)
                route_condition = before_conditions[before_condition]
                
                if current_city in remain_condition:
                    continue
                else:
                    remain_condition.append(current_city)
                    remain_condition_tuple = tuple(remain_condition)
                    if not remain_condition_tuple in current_conditions.keys():
                        current_conditions[remain_condition_tuple] = route_condition + route[remain_node - 1][current_city]
                    else:
                        current_conditions[remain_condition_tuple] = (min(current_conditions[remain_condition_tuple],
                                                                                current_conditions[remain_condition_tuple] + route[remain_node - 1][current_city]))
        shortest_condition[remain_node] = current_conditions
        min_value = 10 ** 9
    for result in shortest_condition[n_of_cities].keys():
        count = 1
        start = result[0]
        end = result[start]
        while count <= n_of_cities:
            end = result[end]
            count += 1
            if start == end:
                break
        if count == n_of_cities:
            min_value = min(min_value, shortest_condition[n_of_cities][result])

    return min_value

n_of_cities = int(stdin.readline())
route = dict()
route_table = dict()
for _ in range(n_of_cities):
    line = list(map(int, stdin.readline().split(' ')))
    route[_]= line

for _ in range(n_of_cities):
    route_table[_] = [0 for i in range(n_of_cities)]


print(revolving_salesman(n_of_cities, route))