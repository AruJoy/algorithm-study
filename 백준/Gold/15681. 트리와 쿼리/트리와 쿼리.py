from sys import stdin
input = stdin.readline
from collections import deque
INF = float("INF")

def arrange_tree(nodes, root, adj_list):
    tree = [(5, -1)]
    que = deque()
    que.append((root, -1, 0))
    dp = [1 for _ in range(nodes)]
    while que:
        cur, parent, depth = que.popleft()
        for child in adj_list[cur]:
            if child == parent: continue
            if len(tree) < depth+2:
                tree.append([])
            tree[depth+1].append((cur, child))
            que.append((child, cur, depth+1))
    for i in range(len(tree)-1, 0, -1):
        for parent, child in tree[i]:
            dp[parent] += dp[child]
    return dp
def main():
    nodes, root, t_count = map(int, input().split())
    adj_list = [[] for _ in range(nodes)]
    for _ in range(nodes-1):
        a, b = map(int, input().split())
        adj_list[a-1].append(b-1)
        adj_list[b-1].append(a-1)
    result = arrange_tree(nodes, root-1, adj_list)
    for _ in range(t_count):
        print(result[int(input().strip())-1])
    return
if __name__ == "__main__":
    main()