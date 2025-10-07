from sys import stdin
input = stdin.readline
from heapq import heappush, heappop

def degree_sort(n_problem, degree_table):
    answer = list()
    heap = list()
    for i in range(n_problem):
        if degree_table[i][0] == 0:
            heappush(heap, i)
            while heap:
                cur = heappop(heap)
                answer.append(cur+1)
                degree_table[cur][0] -= 1
                for l in degree_table[cur][1]:
                    degree_table[l][0] -= 1
                    if degree_table[l][0] == 0:
                        heappush(heap, l)
    return answer
def main():
    n_problem, n_priority = map(int, input().split())
    degree_table = [[0,list()] for _ in range(n_problem)]
    for _ in range(n_priority):
        f, l = map(int, input().split())
        f, l = f-1, l-1
        degree_table[l][0] += 1
        degree_table[f][1].append(l)
    answer = degree_sort(n_problem, degree_table)
    for i in range(n_problem):
        degree_table[i][1].sort()
    print(*answer)
    return
if __name__ == "__main__":
    main()