from sys import stdin
input = stdin.readline
from heapq import heappush, heappop
def dijk(dijk_map, adj_list, people):
    hq = [(0, 0, [])]
    while hq:
        m_w, m, now_list = heappop(hq)
        if m_w != dijk_map[m][0]:
            continue
        for w, end in adj_list[m]:
            new_w = m_w + w
            if new_w < dijk_map[end][0]:
                new_list = [i for i in now_list]
                new_list.append(m)
                dijk_map[end][0] = new_w
                dijk_map[end][1] = new_list
                heappush(hq, (new_w, end, new_list))
    return
def main():
    t_count = int(input().strip())
    for _ in range(t_count):
        count, people = map(int, input().split())
        dijk_map = [[float("INF"),[]] for i in range(people)]
        dijk_map[0][0] = 0
        adj_list = {}
        for i in range(people):
            adj_list[i] = []
        for count in range(count):
            start, end, w = map(int, input().split())
            adj_list[start].append((w, end))
            adj_list[end].append((w, start))
        dijk(dijk_map, adj_list, people)
        if len(dijk_map[people-1][1])<1:
            print("Case #"+str(_+1)+": -1")
            continue
        print("Case #"+str(_+1)+": "+" ".join(map(str, dijk_map[people-1][1])) + " " + str(people-1))
    return
if __name__ == "__main__":
    main()
