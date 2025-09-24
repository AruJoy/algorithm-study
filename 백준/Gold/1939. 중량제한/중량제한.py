from sys import stdin
from collections import deque
input = stdin.readline
INF = float("INF")

def find_path(nodes, adj, start, end, mid):
    visited_list = [False for _ in range(nodes)]
    visited_list[start] = True
    que = deque()
    que.append(start)
    while que:
        cur_n = que.popleft()
        for n, w in adj[cur_n]:
            if (not visited_list[n]) and w >= mid:
                if n == end: return True
                que.append(n)
                visited_list[n] = True
    return False

def main():
    nodes, edges = map(int, input().split())
    adj = [[] for _ in range(nodes)]
    lo = 100000
    hi = 0
    for _ in range(edges):
        a, b, w = map(int, input().split())
        adj[a-1].append((b-1,w))
        adj[b-1].append((a-1,w))
        lo = min(lo, w)
        hi = max(hi, w)
    start, end = map(int, input().split())
    for i in range(nodes):
        adj[i].sort(reverse=True)
    while lo <= hi:
        mid = (lo + hi) // 2
        if find_path(nodes, adj, start-1, end-1, mid):
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    print(ans)
    return
if __name__ == "__main__":
    main()