import heapq as hq
from sys import stdin
min_heap = []
max_heap = []

def findValue(value):
    if len(max_heap) == 0:
        hq.heappush(max_heap, -value)
        print(value)
        return
    if len(min_heap) == 0:
        if -max_heap[0] > value:
            print(value)
            hq.heappush(min_heap, -hq.heappop(max_heap))
        else:
            print(-max_heap[0])
            hq.heappush(min_heap, value)
        return
    
    
    if len(max_heap) > len(min_heap):
        if -max_heap[0] <= value:
            hq.heappush(min_heap, value)
        else:
            hq.heappush(min_heap, -hq.heappop(max_heap))
            hq.heappush(max_heap, -value)
    else:
        if min_heap[0] >= value:
            hq.heappush(max_heap, -value)
        else:
            hq.heappush(max_heap, -hq.heappop(min_heap))
            hq.heappush(min_heap, value)

    print(-max_heap[0])

inputSize = int(stdin.readline())
for i in range(inputSize):
    findValue(int(stdin.readline()))