from sys import stdin
input = stdin.readline
from collections import deque
def main():
    start, target = map(int, input().split())
    que = deque()
    if start == target:
        print(1)
        return
    que.append((target, 0))
    while que:
        cur, count = que.popleft()
        if cur % 10 == 1:
            nxt = cur // 10
            if nxt == start:
                print(count + 2)
                return
            if nxt > start:
                que.append((nxt, count + 1))
        if cur % 2 == 0:
            nxt = cur // 2
            if nxt == start:
                print(count + 2)
                return
            if nxt > start:
                que.append((nxt, count + 1))
    print(-1)
    return
if __name__ == "__main__":
    main()