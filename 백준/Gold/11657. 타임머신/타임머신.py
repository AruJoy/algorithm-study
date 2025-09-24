from sys import stdin
input = stdin.readline
INF = 10**9
def b_f(nodes, adj_list, dijk):
    for _ in range(nodes-1):
        for s, e, w in adj_list:
            if dijk[s] != INF and dijk[e] > dijk[s] + w:
                dijk[e] = dijk[s] + w
    for s, e, w in adj_list:
        if dijk[e] != INF and dijk[e] > dijk[s] + w:
            return False
    return True
def main():
    nodes, edges = map(int, input().split())
    dijk = [INF for _ in range(nodes)]
    dijk[0] = 0
    adj_list = []
    for _ in range(edges):
        start, end, w = map(int, input().split())
        adj_list.append((start-1, end-1, w))
    result = b_f(nodes, adj_list, dijk)
    if result == False:
        print(-1)
        return
    for i in range(1, nodes):
        if dijk[i] == INF:
            print(-1)
            continue
        print(dijk[i])
    
    return

if __name__ == "__main__":
    main()