from sys import stdin
from collections import deque
input = stdin.readline
INF = float("INF")

def bfs(nodes, adj_list, line_list):
    if nodes == 1:
        return 1
    v_list = [False for _ in range(nodes+1)]
    t_v_list = [False for _ in range(len(line_list))]
    v_list[1] = True
    que = deque()
    que.append((1,1))
    while que:
        cur_node, n_visit = que.popleft()
        for line in adj_list[cur_node]:
            if t_v_list[line]:
                continue
            t_v_list[line] = True
            for n in line_list[line]:
                if v_list[n]:
                    continue
                if n == nodes:
                    return n_visit+1
                v_list[n] = True
                que.append((n, n_visit+1))
    return -1

def main():
    nodes, _, lines = map(int, input().split())
    adj_list = [[] for _ in range(nodes+1)]
    line_list = []
    for lines in range(lines):
        line = list(map(int, input().split()))
        line_list.append(line)
        line_index = len(line_list)-1
        for node in line:
            adj_list[node].append(line_index)
    print(bfs(nodes, adj_list, line_list))
    return
if __name__ == "__main__":
    main()