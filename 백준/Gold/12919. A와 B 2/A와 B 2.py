from sys import stdin
input = stdin.readline
from collections import deque

def main():
    start_string = input().strip()
    target_string = input().strip()
    que = deque()
    que.append(target_string)
    while que:
        cur_str = que.popleft()
        if cur_str[-1] == "A":
            nxt = cur_str[: len(cur_str)-1]
            if nxt == start_string:
                print(1)
                return
            if len(nxt) > len(start_string):
                que.append(nxt)
        if cur_str[0] == "B":
            nxt = cur_str[1:]
            nxt = nxt[::-1]
            if nxt == start_string:
                print(1)
                return
            if len(nxt) > len(start_string):
                que.append(nxt)
    print(0)
    return
if __name__ == "__main__":
    main()