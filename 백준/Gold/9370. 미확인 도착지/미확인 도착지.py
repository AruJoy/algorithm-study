from sys import stdin
input = stdin.readline
from heapq import heappop, heappush
INF = float("INF")

def dijk(crosses, start, dijk_list, adj_list, m1, m2):
    heap = list()
    heappush(heap, (0, start, False))
    while heap:
        cur_w, cur_node, validate = heappop(heap)
        if dijk_list[cur_node][0] < cur_w:
            continue
        for i in range(crosses):
            if cur_node == i or i == start: continue
            if adj_list[cur_node][i] == -1: continue
            cost = cur_w + adj_list[cur_node][i]
            new_validate = validate or ((m1==cur_node and m2==i) or (m2==cur_node and m1==i))
            if cost < dijk_list[i][0]:
                dijk_list[i][0] = cost
                dijk_list[i][1] = new_validate
                heappush(heap, (cost, i, new_validate))
                continue
            elif cost == dijk_list[i][0] and new_validate and not dijk_list[i][1]:
                dijk_list[i][1] = True
                heappush(heap, (cost, i, new_validate))
    return
def main():
    t_count = int(input().strip())
    for _ in range(t_count):
        crosses, edges, targets = map(int, input().split())
        start, m1, m2 = map(int, input().split())
        adj_list = [[-1 for _ in range(crosses)] for __ in range(crosses)]
        for i in range(crosses):
            adj_list[i][i] = 0
        dijk_list = [[INF,False] for _ in range(crosses)]
        dijk_list[start-1][0] = 0
        
        for _ in range(edges):
            v1, v2, w = map(int, input().split())
            adj_list[v1-1][v2-1] = w
            adj_list[v2-1][v1-1] = w
        target_list = []
        
        for _ in range(targets):
            target_list.append(int(input().strip()))
        
        dijk(crosses, start-1, dijk_list, adj_list, m1-1, m2-1)
        answer = []
        for i in range(crosses):
            if not i+1 in target_list:
                continue
            if dijk_list[i][0]!=INF and dijk_list[i][1]:
                answer.append(i+1)
        answer.sort()
        print(" ".join(str(node) for node in answer))
    return

if __name__ == "__main__":
    main()
