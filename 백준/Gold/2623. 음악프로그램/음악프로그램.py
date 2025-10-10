from sys import stdin
input = stdin.readline
from collections import deque
INF = float("inf")

def solution(n_group, degree_table):
    ans = list()
    for i in range(n_group):
        if degree_table[i][0] == 0:
            que = deque()
            que.append(i)
            
            while que:
                cur = que.popleft()
                ans.append(cur+1)
                degree_table[cur][0] -= 1
                for nxt in degree_table[cur][1]:
                    degree_table[nxt][0] -= 1
                    if degree_table[nxt][0] == 0:
                        que.append(nxt)
    return ans
def main():
    n_group, n_pd = map(int, input().split())
    degree_table = [[0,list()] for _ in range(n_group)]
    for _ in range(n_pd):
        input_list = list(map(int, input().split()))
        if input_list[0] < 2:
            continue
        for i in range(input_list[0]-1):
            prev, nxt = input_list[i+1], input_list[i+2]
            degree_table[prev-1][1].append(nxt-1)
            degree_table[nxt-1][0] += 1
    ans = solution(n_group, degree_table)
    if len(ans) == n_group:
        for a in ans:
            print(a)
        return
    print(0)
    return

if __name__ == "__main__":
    main()