from sys import stdin
input = stdin.readline
from heapq import heappop, heappush
INF = float("inf")
def find(union_table, x):
    if union_table[x] != x:
        union_table[x] = find(union_table, union_table[x])
    return union_table[x]

def union(union_table, x, y):
    root_a, root_b = find(union_table, x), find(union_table, y)
    min_root = min(root_a, root_b)
    max_root = max(root_a, root_b)
    union_table[max_root] = min_root
    return

def main():
    n_house, n_load = map(int, input().split())
    adj_list = list()
    for _ in range(n_load):
        u, v, w = map(int, input().split())
        u, v = u-1, v-1
        heappush(adj_list, (w, u, v))
    total_w = 0
    large_w = 0
    union_table = [i for i in range(n_house)]

    while adj_list:
        w, u, v = heappop(adj_list)
        u_root, v_root = find(union_table, u), find(union_table, v)
        if u_root == v_root:
            continue
        total_w += w
        large_w = max(large_w, w)
        union(union_table, u, v)
    print(total_w - large_w)
    return
if __name__ == "__main__":
    main()