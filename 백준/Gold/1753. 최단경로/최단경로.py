from sys import stdin
input = stdin.readline
from heapq import heappop, heappush
INF = float("INF")
def dijk(start, adj_list):
    dijk_list = [INF for _ in range(len(adj_list))]
    dijk_list[start] = 0
    heap = list()
    heap.append((0,start))
    while heap:
        cur_w, u = heappop(heap)
        if dijk_list[u] < cur_w:
            continue
        for v, w in adj_list[u]:
            cost = cur_w + w
            if dijk_list[v] > cost:
                dijk_list[v] = cost
                heappush(heap, (cost, v))
    for ans in dijk_list:
        if ans == INF:
            print("INF")
            continue
        print(ans)
    return

def main():
    nodes, edges = map(int, input().split())
    start = int(input().strip())-1
    adj_list = [[] for _ in range(nodes)]
    for _ in range(edges):
        s, e, w = map(int, input().split())
        adj_list[s-1].append((e-1, w))
    dijk(start, adj_list)
    return
if __name__ == "__main__":
    main()