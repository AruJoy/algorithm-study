from sys import stdin
input = stdin.readline
from collections import deque

def main():
    n_room, start, end = map(int, input().split())
    adj_list = [list() for i in range(n_room)]
    for i in range(n_room-1):
        u, v, w = map(int, input().split())
        adj_list[u-1].append((v-1, w))
        adj_list[v-1].append((u-1, w))
    if start == end:
        print(0)
        return
    que = deque()
    que.append((-1, start-1, 0, 0))
    while que:
        before, cur, cur_w, max_w = que.popleft()
        for nxt, w in adj_list[cur]:
            if before == nxt:
                continue
            if nxt == end - 1:
                print(cur_w + w - max(w, max_w))
                return
            que.append((cur, nxt, cur_w + w, max(max_w, w)))
    return
if __name__ == "__main__":
    main()