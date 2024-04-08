from sys import stdin
from heapq import heappop, heappush
def LIS(sequence, length_of_sequence):
    lis_list = list()
    min_val = sequence[0]
    max_val = sequence[0]
    lis_list.append(sequence[0])
    for i in range(1, length_of_sequence):
        if max_val < sequence[i]:
            lis_list.append(sequence[i])
            min_val = min(lis_list)
            max_val = max(lis_list)
        elif sequence[i] <= min_val:
            lis_list[0] = sequence[i]
            min_val = min(lis_list)
            max_val = max(lis_list)
        else:
            for j in range(len(lis_list)):
                if sequence[i] < lis_list[j]:
                    lis_list[j] = sequence[i]
                    if j == len(lis_list) - 1:
                        max_val = sequence[i]
                    break
    return len(lis_list)

length_of_sequence = int(stdin.readline())
sequence = list(map(int, stdin.readline().split(' ')))
print(LIS(sequence, length_of_sequence))