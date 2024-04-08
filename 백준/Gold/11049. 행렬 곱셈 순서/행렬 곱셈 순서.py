from sys import stdin
from heapq import heappop, heappush
def matrix_chain(p, number_of_matrix):
    matrix_chain_table = dict()
    for i in range(1, number_of_matrix+1):
        matrix_chain_table[i] = [0 for i in range(number_of_matrix + 1)]
    for j in range(1, number_of_matrix):
        for i in range(1, number_of_matrix+1):
            list_of_calculation = list()
            if number_of_matrix < i+j:
                continue
            for k in range(1, j+1):
                value = matrix_chain_table[i][i+j-k] + matrix_chain_table[i+j-k+1][i+j] + p[i-1]*p[i+j-k]*p[i + j]
                heappush(list_of_calculation, value)
            matrix_chain_table[i][i+j] = heappop(list_of_calculation)
    
    return matrix_chain_table[1][number_of_matrix]

number_of_matrix = int(stdin.readline())
p = list()
for _ in range(number_of_matrix-1):
    p1 , p2 = map(int, stdin.readline().split(' '))
    p.append(p1)
p1 , p2 = map(int, stdin.readline().split(' '))
p.append(p1)
p.append(p2)

print(matrix_chain(p, number_of_matrix))