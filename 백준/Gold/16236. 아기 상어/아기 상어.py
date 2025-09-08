from sys import stdin
input = stdin.readline
from collections import deque
from heapq import heappop, heappush

def get_input():
    scale = int(input())
    feed_map = []
    shark = []
    for i in range(scale):
        new_row = list(map(int, input().split(" ")))
        for j in range(scale):
            if new_row[j] == 9:
                new_row[j] = 0
                shark.append(i)
                shark.append(j)
                shark.append(2)
                shark.append(0)
        feed_map.append(new_row)
    return scale, feed_map, shark

def shark_eat_food(shark:list, feed_map:list, y:int, x:int):
    feed_map[y][x] = 0
    shark[1] = x
    shark[0] = y
    if shark[3] == shark[2]-1:
        shark[2] += 1
        shark[3] = 0
        return
    shark[3] += 1
    return

def find_food(scale:int, feed_map:list, shark:list):
    v_list = [[False for _ in range(scale)] for __ in range(scale)]
    dy = [-1, 0, 0, 1]
    dx = [0, -1, 1, 0]
    
    que = deque()
    v_list[shark[0]][shark[1]] = True
    que.append([shark[0],shark[1],0])
    
    move = 0
    heap = list()
    while que:
        current_status = que.popleft()
        if 0 < move and current_status[2] >= move:
            break
        for i in range(4):
            y = current_status[0] + dy[i]
            x = current_status[1] + dx[i]
            if (y < 0 or scale - 1 < y
                or x < 0 or scale - 1 < x
                or feed_map[y][x] > shark[2]
                or v_list[y][x]):
                continue
            if 0 < feed_map[y][x] < shark[2]:
                move = current_status[2] + 1
                heappush(heap, (y,x))
            v_list[y][x] = True
            que.append([y, x, current_status[2]+1])
    if not heap:
        return 0
    y, x = heappop(heap)
    shark_eat_food(shark, feed_map, y, x)
    return move

def get_ans(scale:int, feed_map:list, shark:list):
    move = 2147483647
    move = 0
    last_move = -1
    
    while last_move != 0:
        last_move = find_food(scale, feed_map, shark)
        move += last_move
    return move
scale, feed_map, shark = get_input()
print(get_ans(scale, feed_map, shark))