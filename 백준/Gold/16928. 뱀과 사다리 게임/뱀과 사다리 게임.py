from sys import stdin
from collections import deque
input = stdin.readline
INF = float("INF")
def roll_dice(move_map, visited_list):
    visited_list[0] = True
    que = deque()
    que.append((0, 0))

    while que:
        cul_number, cur_move = que.popleft()
        for i in range(6, 0, -1):
            nxt_number = cul_number+i
            if nxt_number > 99:
                continue
            if nxt_number == 99:
                return cur_move+1
            if visited_list[nxt_number]:
                continue
            y, x = nxt_number//10, nxt_number%10
            
            while move_map[y][x] != -1:
                nxt_number = move_map[y][x]
                y, x = nxt_number//10, nxt_number%10
            visited_list[nxt_number] = True
            que.append((nxt_number, cur_move+1))
    return
def main():
    n_ladder, n_snake = map(int, input().split())

    move_map = [[-1 for _ in range(10)]for __ in range(10)]

    for _ in range(n_ladder):
        start, end = map(int, input().split())
        s_y, s_x = (start-1)//10, (start-1)%10
        move_map[s_y][s_x] = end-1

    for _ in range(n_snake):
        start, end = map(int, input().split())
        s_y, s_x = (start-1)//10, (start-1)%10
        move_map[s_y][s_x] = end-1
    visited_list = [False for _ in range(100)]
    print(roll_dice(move_map, visited_list))
    return
if __name__ == "__main__":
    main()