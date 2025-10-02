from sys import stdin
input = stdin.readline
from collections import deque
INF = float("INF")

def floyd(n_planet, adj_list, dijk_list):
    for m in range(n_planet):
        for u in range(n_planet):
            for v in range(n_planet):
                cost = adj_list[u][m] + adj_list[m][v]
                if dijk_list[u][v] > cost:
                    dijk_list[u][v] = cost
    return

def find_min_cost(dijk_list, n_planet, position, mask, count, cost):
    ans = INF
    if n_planet == count:
        return cost
    bit = 1
    for i in range(n_planet):
        if mask & bit:
            bit = bit << 1
            continue
        cur_cost = cost + dijk_list[position][i]
        ans = min(ans, find_min_cost(dijk_list, n_planet, i, mask|bit, count+1, cur_cost))
        bit = bit << 1
    return ans
def main():
    n_planet, position = map(int, input().split())
    adj_list = list()
    for _ in range(n_planet):
        adj_list.append(list(map(int, input().split())))
    dijk_list = [[INF for _ in range(n_planet)] for __ in range(n_planet)]

    for i in range(n_planet):
        dijk_list[i][i] = 0
    floyd(n_planet, adj_list, dijk_list)

    print(find_min_cost(dijk_list, n_planet, position, 1<<position, 1, 0))
    return
if __name__ == "__main__":
    main()