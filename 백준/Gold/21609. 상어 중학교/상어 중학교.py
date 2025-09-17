from sys import stdin
input = stdin.readline
from collections import deque
import math
def get_input():
    scale, colors = map(int, input().split(" "))
    block_map = []
    for _ in range(scale):
        row = list(map(int, input().split(" ")))
        block_map.append(row)
    return scale, colors, block_map
def find_largest_group(scale:int, block_map:list, block:int, dy:list, dx:list):
    visited_map = [[False for _ in range(scale)] for __ in range(scale)]
    list = []
    size = -1
    start_y = -1
    start_x = -1
    rainbow_count = -1
    for i in range(scale):
        for j in range(scale):
            if visited_map[i][j]:
                continue
            if block_map[i][j] == block:
                visited_map[i][j]=True
                current_size = 1
                current_y = i
                current_x = j
                current_list = []
                current_rainbow_count = 0
                que = deque()
                que.append((i,j))
                current_list.append([i,j])
                while que:
                    now_y, now_x = que.popleft()
                    for k in range(4):
                        y = now_y + dy[k]
                        x = now_x + dx[k]
                        if (y < 0 or scale-1 < y
                            or x < 0 or scale-1 < x
                            or visited_map[y][x]):
                            continue
                        if block_map[y][x] == 0 or block_map[y][x]==block:
                            if block_map[y][x] == 0:
                                current_rainbow_count+=1
                            current_size += 1
                            visited_map[y][x] = True
                            que.append((y,x))
                            current_list.append([y,x])
                if current_size < size:
                    continue
                if current_size == size:
                    if current_rainbow_count < rainbow_count:
                        continue
                    if current_rainbow_count == rainbow_count:
                        if start_y > current_y:
                            continue
                        if start_y == current_y and start_x > current_x:
                            continue
                size = current_size
                start_y = current_y
                start_x = current_x
                list = current_list
                rainbow_count = current_rainbow_count
    return size, rainbow_count, start_y, start_x, list
def delete_group(block_map:list, group:list):
    for coordinate in group:
        block_map[coordinate[0]][coordinate[1]] = -2
    return len(group)**2
def pull_down(scale:int, block_map:list):
    for i in range(scale):
        for j in range(scale):
            if block_map[scale - i - 1][j] == -2:
                for k in range(scale - i - 1):
                    if block_map[scale - i - 2 - k][j] == -1:
                        break
                    if block_map[scale - i - 2 - k][j] > -1:
                        block_map[scale - i - 1][j] = block_map[scale - i - 2 - k][j]
                        block_map[scale - i - 2 - k][j] = -2
                        break
    return
def rotate(scale:int, block_map:list):
    middle = (scale-1)/2
    copy_map = [row[:] for row in block_map]
    for i in range(scale):
        for j in range(scale):
            dx = j - middle
            dy = i - middle
            block_map[math.floor(middle-dx)][math.floor(middle+dy)] = copy_map[i][j]
def get_solution(scale:int, colors:int, block_map:list):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    score = 0
    while True:
        group_list = []
        for i in range (colors):
            size, rainbow_count, start_y, start_x, list  =find_largest_group(scale, block_map, i+1, dy, dx)
            group_list.append([size, rainbow_count, start_y, start_x, list])
        group_list.sort(reverse=True)
        if group_list[0][0] < 2:
            break
        score += delete_group(block_map, group_list[0][4])
        pull_down(scale, block_map)
        rotate(scale, block_map)
        pull_down(scale, block_map)
    return score
scale, colors, block_map = get_input()
print(get_solution(scale, colors, block_map))