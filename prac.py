from sys import stdin
from collections import deque
from heapq import heappop, heappush

def find_lcs(sequence, allowed_duplication):
    value_in_list = False
    sc = dict()
    cs_list = list()
    count = 0 
    for i in range(len(sequence)):
        if not sequence[i] in sc.keys():
            sc[sequence[i]] = deque()
            sc[sequence[i]].append((1,i,0))
            count += 1
            continue
        
        latest_condition = sc[sequence[i]][-1]
        if latest_condition[0] >= allowed_duplication:
            oldest_condition = sc[sequence[i]].popleft()
            value_in_list = True
            write_count = count -oldest_condition[2]
            heappush(cs_list, -write_count)
            count += 1
            sc[sequence[i]].append((latest_condition[0]+1, i, oldest_condition[1]))

        else:
            sc[sequence[i]].append((latest_condition[0]+1, i, sc[sequence[i]][-1][1]))
            count += 1
        
    for i in sc.keys():
        if len(sc[i]) != 0:
            condition = sc[i].popleft()
            heappush(cs_list, -(count-condition[1]))
    if value_in_list == False:
        return len(sequence)
    return -heappop(cs_list)

sequence_length, allowed_duplication = map(int, stdin.readline().split(' '))
sequence = list(map(int, stdin.readline().split()))
print(find_lcs(sequence, allowed_duplication))