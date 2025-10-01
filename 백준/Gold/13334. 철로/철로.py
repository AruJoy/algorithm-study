from sys import stdin
input = stdin.readline
from heapq import heappop, heappush
def main():
    heap = list()
    n_people = int(input().strip())
    event_list = []
    for _ in range(n_people):
        a, b = map(int, input().split())
        event_list.append((a, b))
    
    length = int(input().strip())
    point_list = dict()
    
    for a, b in event_list:
        a, b = min(a, b), max(a, b)
        if b - a > length: continue
        add_point = b - length
        if add_point in point_list:
            point_list[add_point] += 1
        else: point_list[add_point] = 1
        
        if a+1 in point_list:
            point_list[a+1] -= 1
        else: point_list[a+1] = -1
    ans = 0
    cur = 0
    keys = list(point_list.keys())
    keys.sort()
    for key in keys:
        cur += point_list[key]
        ans = max(ans, cur)
    print(ans)
    return

if __name__ == "__main__":
    main()
