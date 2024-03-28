from sys import stdin
from heapq import heappop, heappush
left_max = []
right_min = []
inputSize = int(stdin.readline())
for i in range(inputSize):
    value = int(stdin.readline())
    if len(left_max) == len(right_min):
        heappush(left_max, -value)
    else:
        heappush(right_min, value)
    if len(left_max) != 0 and len(right_min) != 0:
        value1 = heappop(left_max)
        value2 = right_min[0]
        if value1 > value2:
            heappush(left_max, -value1)
            heappush(right_min, value2)
    
    print(-left_max[0])