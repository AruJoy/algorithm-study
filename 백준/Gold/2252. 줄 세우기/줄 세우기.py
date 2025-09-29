from sys import stdin
from collections import deque
input = stdin.readline

def degree_sort(n, t_count, tree):
    answer = list()
    que = deque()
    for i in range(n):
        if tree[i][0] == 0:
            que.append(i)
    while que:
        cur = que.popleft()
        answer.append(cur+1)
        
        for nxt in tree[cur][1]:
            tree[nxt][0] -= 1
            if tree[nxt][0] == 0:
                que.append(nxt)
    return answer
def main():
    n, t_count = map(int, input().split())

    tree = [[0,list()] for _ in range(n)]

    for _ in range(t_count):
        a, b = map(int, input().split())
        tree[b-1][0] += 1
        tree[a-1][1].append(b-1)

    answer = degree_sort(n, t_count, tree)
    print(*answer)
    return

if __name__ == "__main__":
    main()
