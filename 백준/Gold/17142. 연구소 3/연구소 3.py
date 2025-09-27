from sys import stdin
input = stdin.readline
from collections import deque

def get_input():
    scale, active_count = map(int, input().split(" "))
    lab_map = []
    empty_spaces = 0
    virus_list = []
    for i in range(scale):
        row = list(map(int, input().split(" ")))
        for j in range(scale):
            if row[j] == 1:
                row[j] = -1
                continue
            if row[j] == 2:
                row[j] = 1
                virus_list.append((i, j))
                continue
            empty_spaces += 1
        lab_map.append(row)
    return scale, active_count, empty_spaces ,lab_map, virus_list

def simulate_virus(scale: int, lab_map: list, active_list: list, empty_spaces: int, min_result: list):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    day = 0
    target_count = empty_spaces
    detect_list = deque(active_list)
    for y, x in detect_list:
        lab_map[y][x] = 2
    while detect_list:
        if target_count <= 0:
            return day
        if min_result[0] - 1 <= day:
            return day + 1
        today_length = len(detect_list)
        for _ in range(today_length):
            current_y, current_x = detect_list.popleft()
            for i in range(4):
                y = current_y + dy[i]
                x = current_x + dx[i]
                if (y < 0 or scale - 1 < y
                    or x < 0 or scale - 1 < x
                    or lab_map[y][x] == -1
                    or lab_map[y][x] == 2):
                    continue
                if lab_map[y][x] == 0:
                    target_count -= 1
                lab_map[y][x] = 2
                detect_list.append((y,x))
        day += 1
    if target_count == 0:
        return day
    return min_result[0]

def active_virus(scale: int, active_count:int, empty_spaces:int ,lab_map: list, virus_list: list,
                                        active_list: list, last_index: int, min_result: list):
    if len(active_list) == active_count:
        copy_map = [row[:] for row in lab_map]
        return simulate_virus(scale, copy_map, active_list, empty_spaces, min_result)
    for i in range(last_index, len(virus_list)):
        active_list.append(virus_list[i])
        new_result = active_virus(scale, active_count, empty_spaces, lab_map, virus_list, active_list, i+1, min_result)
        active_list.pop()  
        min_result[0] = min(min_result[0], new_result)
    return min_result[0]

def get_answer(scale: int, active_count:int, empty_spaces:int ,lab_map: list, virus_list: list,
                                        ):
    answer = active_virus(scale, active_count, empty_spaces ,lab_map, virus_list, [], 0, [float('inf')])
    if answer == float('inf'):
        return -1
    return answer
scale, active_count, empty_spaces ,lab_map, virus_list = get_input()
print(get_answer(scale, active_count, empty_spaces ,lab_map, virus_list))