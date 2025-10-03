from sys import stdin
input = stdin.readline
from collections import deque

def main():
    s, b = map(int, input().split())
    visited_list = [False for _ in range(100001)]
    visited_list[s] = True
    que = deque()
    que.append((s, 0))
    if s == b:
        print(0)
        return
    while que:
        cur, cur_move = que.popleft()
        nxt = cur + 1
        if nxt <=100000 and not visited_list[nxt]:
            visited_list[nxt] = True
            if nxt == b:
                print(cur_move+1)
                break
            que.append((nxt, cur_move+1))
        
        nxt = cur - 1
        if 0<= nxt and not visited_list[nxt]:
            visited_list[nxt] = True
            if nxt == b:
                print(cur_move+1)
                break
            que.append((nxt, cur_move+1))
        
        nxt = cur * 2
        if nxt <=100000 and not visited_list[nxt]:
            visited_list[nxt] = True
            if nxt == b:
                print(cur_move+1)
                break
            que.append((nxt, cur_move+1))
    return
if __name__ == "__main__":
    main()