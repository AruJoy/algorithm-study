from sys import stdin
input = stdin.readline
from collections import deque

map_size, runway_length = map(int, input().split(" "))

load_map = []

for _ in range(map_size):
    new_row = list(map(int,input().split(" ")))
    load_map.append(new_row)

for i in range(map_size):
    new_row = [load_map[j][i] for j in range(map_size)]
    load_map.append(new_row)

def able_putting_runway(runway_road, direction, height, current_space, way, map_size, runway_length):
    if (direction):
        if current_space + runway_length > map_size - 1:
            return False
        for i in range(runway_length):
            if way[current_space + i + 1] == height-1 and not runway_road[current_space + i + 1]:
                runway_road[current_space + i + 1] = True
                continue
            return False
    if (not direction):
        if current_space - runway_length + 1 < 0:
            return False
        for i in range(runway_length):
            if way[current_space - i] == height and not runway_road[current_space - i]:
                runway_road[current_space - i] = True
                continue
            return False
    return True

def put_runway(way, map_size, runway_length):
    runway_road = [False for _ in range(map_size)]
    for i in range(map_size-1):
        if way[i] == way[i+1]:
            continue
        if way[i]+1 == way[i+1]:
            if(able_putting_runway(runway_road, False, way[i], i, way, map_size, runway_length)):
                continue
            return False
        if way[i]-1 == way[i+1]:
            if(able_putting_runway(runway_road, True, way[i], i, way, map_size, runway_length)):
                i+=runway_length
                continue
            return False
        return False
    return True

def get_answer(load_map, map_size, runway_length):
    answer = 0
    for i in range(2 * map_size):
        if(put_runway(load_map[i], map_size, runway_length)):
            answer+=1
    return answer
print(get_answer(load_map, map_size, runway_length))