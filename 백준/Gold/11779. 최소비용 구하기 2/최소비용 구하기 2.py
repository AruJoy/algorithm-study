from sys import stdin
input = stdin.readline
from collections import deque
INF = float("inf")
def bfs(adj_list, n_node, start, target):
    bfs_table = [[INF, list()] for _ in range(n_node)]
    bfs_table[start][0] = 0
    que = deque()
    que.append((start, 0, [start+1]))
    while que:
        m, cur_w, cur_path = que.popleft()
        if bfs_table[m][0] < cur_w:
            continue
        for v, w in adj_list[m]:
            cost = cur_w + w
            if bfs_table[v][0] > cost:
                new_list = [value for value in cur_path]
                new_list.append(v+1)
                bfs_table[v] = (cost, new_list)
                que.append((v, cost, new_list))
    print(bfs_table[target][0])
    print(len(bfs_table[target][1]))
    print(*bfs_table[target][1])
    return
def main():
    n_node = int(input().strip())
    n_edge = int(input().strip())
    adj_list = [list() for __ in range(n_node)]
    for _ in range(n_edge):
        u, v, w  = map(int, input().split())
        u, v = u-1, v-1
        adj_list[u].append((v,w))
    start, target = map(int, input().split())
    start, target = start-1, target-1
    bfs(adj_list, n_node, start, target)
    return
if __name__ == "__main__":
    main()