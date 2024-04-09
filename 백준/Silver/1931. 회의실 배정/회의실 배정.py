from sys import stdin
from heapq import heappop, heapify

def meeting_room(meeting_list):
    count = 0
    end_time = 0
    for i in range(len(meeting_list)):
        end, start = heappop(meeting_list)
        if end_time <= start:
            count += 1
            end_time = end
    return count

n_meeting = int(stdin.readline())
meeting_list = list()
for _ in range(n_meeting):
    start, end = map(int, stdin.readline().split(' '))
    meeting_list.append([end, start])
    
heapify(meeting_list)
print(meeting_room(meeting_list))