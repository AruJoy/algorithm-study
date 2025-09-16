from sys import stdin
import math
input = stdin.readline
from collections import deque
def get_input():
    power, skills = map(int, input().split(" "))
    scale = 2**power
    ice_map = []
    for _ in range(scale):
        row = list(map(int, input().split(" ")))
        ice_map.append(row)
    skill_list = list(map(int, input().split(" ")))
    return scale, ice_map, skill_list

def rotate_iceberg(scale:int, ice_map:list, skill:int):
    if skill == 0:
        return
    split_scale = 2**skill
    repeat = math.floor(scale/split_scale)
    middle = (split_scale-1)/2
    for i in range(repeat):
        for j in range(repeat):
            start_y = i*split_scale
            start_x = j*split_scale
            end_y = (i+1)*split_scale
            end_x = (j+1)*split_scale
            split_map = split_map = [row[start_x:end_x] for row in ice_map[start_y:end_y]]
            for k in range(split_scale):
                for l in range(split_scale):
                    dy = k-middle
                    dx = l-middle
                    ice_map[math.floor(start_y+middle+dx)][math.floor(start_x+middle-dy)] = split_map[math.floor(middle+dy)][math.floor(middle+dx)]
    return
def ice_melt_down(scale:int, ice_map:list):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    melt_down_list = []
    for i in range(scale):
        for j in range(scale):
            if ice_map[i][j] == 0: continue
            adjacent_count = 0
            for k in range(4):
                y = i + dy[k]
                x = j + dx[k]
                if (y < 0 or scale-1 < y
                    or x < 0 or scale-1 < x
                    or ice_map[y][x]<1):
                    continue
                adjacent_count += 1
            if adjacent_count < 3:
                melt_down_list.append((i,j))
    for y, x in melt_down_list:
        ice_map[y][x] -= 1
    return

def count_ice(scale:int, ice_map:list):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    ice_values = 0
    biggest_iceberg = 0
    union_map = [[False for _ in range(scale)]for __ in range(scale)]
    for i in range(scale):
        for j in range(scale):
            ice_values += ice_map[i][j]
            if union_map[i][j]:
                continue
            if ice_map[i][j] == 0:
                union_map[i][j] = True
                continue
            union_map[i][j] = True
            que = deque()
            que.append((i,j))
            ice_berg_size = 1
            while que:
                current_y, current_x = que.popleft()
                for k in range(4):
                    y = current_y + dy[k]
                    x = current_x + dx[k]
                    if (y < 0 or scale-1 < y
                        or x < 0 or scale-1 < x
                        or union_map[y][x]):
                        continue
                    union_map[y][x] = True
                    if ice_map[y][x] > 0:
                        ice_berg_size += 1
                        que.append((y,x))
                biggest_iceberg = max(biggest_iceberg, ice_berg_size)
    return ice_values, biggest_iceberg
def get_answer(scale:int, ice_map:list, skill_list:list):
    for skill in skill_list:
        rotate_iceberg(scale, ice_map, skill)
        ice_melt_down(scale, ice_map)
    ice_values, biggest_iceberg = count_ice(scale, ice_map)
    print(ice_values)
    print(biggest_iceberg)
    return
scale, ice_map, skill_list = get_input()
get_answer(scale, ice_map, skill_list)