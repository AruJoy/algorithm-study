from sys import stdin
input = stdin.readline
from heapq import heappop, heappush
INF = float("INF")
def f_m(nodes, f_map):
    for m in range(nodes):
        for s in range(nodes):
            for e in range(nodes):
                if f_map[s][e] > f_map[s][m] + f_map[m][e]:
                    f_map[s][e] = f_map[s][m] + f_map[m][e]
    return
def main():
    nodes = int(input().strip())
    edges = int(input().strip())
    
    f_map = [[INF for _ in range(nodes)] for __ in range(nodes)]
    for i in range(nodes):
        f_map[i][i] = 0
    
    for _ in range(edges):
        start, end, w = map(int, input().split())
        f_map[start-1][end-1] = min(w, f_map[start-1][end-1])
    
    f_m(nodes, f_map)
    for row in f_map:
        for i in range(nodes):
            if row[i] == INF:
                row[i] = 0
        print(*row)
if __name__ == "__main__":
    main()