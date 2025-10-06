from sys import stdin
input = stdin.readline
from collections import deque

def main():
    start_number = int(input().strip())
    if start_number == 1:
        print(0)
        print(1)
        return
    visited_list = [False for _ in range(start_number)]
    que = deque()
    que.append((start_number, [start_number]))
    while que:
        cur_number, cur_list = que.popleft()
        if cur_number % 3 == 0:
            nxt = cur_number // 3
            if nxt == 1:
                print(len(cur_list))
                cur_list.append(1)
                print(*cur_list)
                return
            if not visited_list[nxt]:
                visited_list[nxt] = True
                nxt_list = [num for num in cur_list]
                nxt_list.append(nxt)
                que.append((nxt, nxt_list))
        if cur_number % 2 == 0:
            nxt = cur_number // 2
            if nxt == 1:
                print(len(cur_list))
                cur_list.append(1)
                print(*cur_list)
                return
            if not visited_list[nxt]:
                visited_list[nxt] = True
                nxt_list = [num for num in cur_list]
                nxt_list.append(nxt)
                que.append((nxt, nxt_list))
        nxt = cur_number - 1
        if nxt == 1:
            print(len(cur_list))
            cur_list.append(1)
            print(*cur_list)
            return
        if not visited_list[nxt]:
            visited_list[nxt] = True
            nxt_list = [num for num in cur_list]
            nxt_list.append(nxt)
            que.append((nxt, nxt_list))
    return
if __name__ == "__main__":
    main()