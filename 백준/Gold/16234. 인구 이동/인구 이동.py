from sys import stdin
from collections import deque
import math
input = stdin.readline

def get_input():
    state_map = []
    scale, min_delta, max_delta = map(int,input().split(" "))
    for _ in range(scale):
        new_row = list(map(int, input().split(" ")))
        state_map.append(new_row)
    return scale, state_map, min_delta, max_delta

def get_union(scale:int, state_map:list, min_delta:int, max_delta:int):
    union_map = [[False for _ in range(scale)] for __ in range(scale)]
    visited_map = [[False for _ in range(scale)] for __ in range(scale)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    union_list = []
    
    for i in range(scale):
        for j in range(scale):
            if union_map[i][j]: continue
            que = deque()
            union = [[i,j]]
            union_count = 1
            total_people = state_map[i][j]
            visited_map[i][j] = True
            union_map[i][j] = True
            que.append([i,j, state_map[i][j]])
            while que:
                current_y, current_x, people = que.popleft()
                for k in range(4):
                    y = current_y + dy[k]
                    x = current_x + dx[k]
                    if (y < 0
                        or scale - 1 < y
                        or x < 0
                        or scale - 1 < x):
                        continue
                    if visited_map[y][x]:
                        continue
                    delta = abs(people - state_map[y][x])
                    if (min_delta <= delta and delta <= max_delta):
                        visited_map[y][x] = True
                        union_map[y][x] = True
                        que.append([y, x, state_map[y][x]])
                        union.append([y,x])
                        union_count += 1
                        total_people += state_map[y][x]
            if union_count > 1:
                union_list.append([union,union_count,total_people])

    return union_list

def emigrate(state_map:list, union_list:list):
    for i in range(len(union_list)):
        average_people = math.floor(union_list[i][2]/union_list[i][1])
        for state in union_list[i][0]:
            state_map[state[0]][state[1]] = average_people
    return

def get_answer(scale:int, state_map:list, min_delta:int, max_delta:int):
    answer = 0
    while True:
        union_list= get_union(scale, state_map, min_delta, max_delta)
        if len(union_list) < 1:
            break
        answer += 1
        emigrate(state_map, union_list)
    return answer

scale, state_map, min_delta, max_delta = get_input()
print(get_answer(scale, state_map, min_delta, max_delta))