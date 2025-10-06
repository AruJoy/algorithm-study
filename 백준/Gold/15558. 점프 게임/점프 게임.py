from sys import stdin
input = stdin.readline
from collections import deque

def judge(que, y, x, columns, cur_time, ladder,visited_list):
    if x <= cur_time:
        return False
    if x >= columns:
        return True
    if ladder[y][x] == 1 and not visited_list[y][x]:
        visited_list[y][x] = True
        que.append((y, x, cur_time+1))
    return False
def main():
    columns, skip = map(int, input().split())
    ladder = list()
    for _ in range(2):
        ladder.append(list(map(int, input().strip())))
    visited_list = [[False for _ in range(columns)] for __ in range(2)]
    que = deque()
    visited_list[0][0] = True
    que.append((0, 0, 0))
    time = 0
    while que and time < columns:
        while que:
            if que[0][2] != time:
                break
            cur_y, cur_x, cur_time = que.popleft()
            
            y, x = (cur_y+1) % 2, cur_x + skip
            if(judge(que, y, x, columns, cur_time, ladder,visited_list)):
                print(1)
                return
            y, x = cur_y, cur_x + 1
            if(judge(que, y, x, columns, cur_time, ladder,visited_list)):
                print(1)
                return
            y, x = cur_y, cur_x - 1
            if(judge(que, y, x, columns, cur_time, ladder,visited_list)):
                print(1)
                return
        time += 1
    print(0)
    return
if __name__ == "__main__":
    main()