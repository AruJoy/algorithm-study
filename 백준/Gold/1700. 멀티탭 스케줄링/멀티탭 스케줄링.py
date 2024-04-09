from sys import stdin
from heapq import heappop, heappush
from collections import deque

def multi_tab(appliances, holes, uses):
    current_plug = list()
    change_candidate = list()
    count = 0
    index_controller = 0
    
    while len(current_plug) < holes and 0 < len(appliances):
        appliance = appliances.popleft()
        index_controller += 1
        if not appliance in current_plug:
            current_plug.append(appliance)
        else:
            for change in range(len(change_candidate)):
                if change_candidate[change][1] == appliance:
                    del change_candidate[change]
                    break
        if not appliance in appliances:
            heappush(change_candidate, [-10**9, appliance])
        else:
            next_use = appliances.index(appliance)
            heappush(change_candidate, [-(next_use+index_controller), appliance])

    while 0 < len(appliances):
        appliance = appliances.popleft()
        index_controller += 1
        if not appliance in current_plug:
            trash, remove_plug = heappop(change_candidate)
            current_plug.remove(remove_plug)
            count += 1
            current_plug.append(appliance)
        else:
            for change in range(len(change_candidate)):
                if change_candidate[change][1] == appliance:
                    del change_candidate[change]
                    break
        if not appliance in appliances:
            heappush(change_candidate, [-10**9, appliance])
        else: 
            next_use = appliances.index(appliance)
            heappush(change_candidate, [-(next_use+index_controller), appliance])
    return count

holes, uses = map(int, stdin.readline().split(' '))
appliances = deque(map(int, stdin.readline().split(' ')))
uses = len(appliances)

print(multi_tab(appliances, holes, uses))