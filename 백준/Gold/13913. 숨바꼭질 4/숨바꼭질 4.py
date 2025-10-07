from sys import stdin
input = stdin.readline
from collections import deque
def print_answer(visited_list, nxt):
    answer = list()
    cur = nxt
    answer.append(cur)
    while cur != visited_list[cur]:
        cur = visited_list[cur]
        answer.append(cur)
    print(len(answer)-1)
    answer.reverse()
    print(*answer)
    return
def judge(nxt, cur, max_range,visited_list, que, b):
    if (nxt < 0 or max_range-1 < nxt or visited_list[nxt] >= 0):
        return False
    visited_list[nxt]=cur  
    if nxt == b:
        return True
    que.append((nxt))
    
    return False

def catch_b(s, b):
    
    max_range = max(b + (b//2) +1, s+1)
    visited_list = [-1 for _ in range(max_range)]
    visited_list[s] = s
    que = deque()
    que.append((s))
    
    while que:
        cur = que.popleft()
        if cur < b:
            nxt = cur * 2
            if judge(nxt, cur, max_range,visited_list, que, b):
                print_answer(visited_list, nxt)
                return
        if cur < b:
            nxt = cur + 1
            if judge(nxt, cur, max_range,visited_list, que, b):
                print_answer(visited_list, nxt)
                return
        nxt = cur - 1
        if judge(nxt, cur, max_range,visited_list, que, b):
            print_answer(visited_list, nxt)
            return
    return

def main():
    s, b = map(int, input().split())
    if s == b:
        print(0)
        print(s)
        return
    catch_b(s, b)
    return
if __name__ == "__main__":
    main()