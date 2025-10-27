from collections import deque
from sys import stdin
input = stdin.readline

INF = float("inf")


def dijk(adj_list, s):
    dijk_list = [INF for _ in range(len(adj_list))]
    dijk_list[s] = 0
    que = deque()
    que.append((s, 0))
    while que:
        u, l = que.popleft()
        if l > dijk_list[u]:
            continue
        for v, w in adj_list[u]:
            cost = l + w
            if dijk_list[v] <= cost:
                continue
            dijk_list[v] = cost
            que.append((v, cost))
    node = 0
    length = 0
    for i in range(1, len(dijk_list)):
        w = dijk_list[i]
        if w > length:
            node = i
            length = w
    return node, length


def main():
    n_node = int(input().strip())
    adj_list = [list()for i in range(n_node + 1)]
    for _ in range(n_node):
        line = list(map(int, input().split()))
        u = line[0]
        for i in range(1, len(line) - 1):
            if i % 2 == 0:
                continue
            v, weight = line[i], line[i + 1]
            adj_list[u].append((v, weight))
            adj_list[v].append((u, weight))
    node, length = dijk(adj_list, 1)
    _, ans = dijk(adj_list, node)
    print(ans)
    return


if __name__ == "__main__":
    main()
