from sys import stdin
input = stdin.readline
from collections import deque
import math

def get_input():
    rows, columns, time = map(int, input().split(" "))
    dust_map = []
    dirty_air = deque()
    air_cleaner = []
    for i in range(rows):
        new_row = list(map(int, input().split(" ")))
        for j in range(columns):
            if new_row[j] == -1:
                air_cleaner.append([i,j])
                continue
            if new_row[j] >= 5:
                dirty_air.append([i,j])
        dust_map.append(new_row)
    return rows, columns, dust_map, time, dirty_air, air_cleaner

def defuse_dust(rows:int, columns:int, dust_map:list, dirty_air:deque):
    dx = [0, -1, 1, 0]
    dy = [-1, 0, 0, 1]
    repeat = len(dirty_air)
    defuse_list = []
    for _ in range(repeat):
        defuse_count = 0
        dust = dirty_air.popleft()
        if dust[0] == -1 and dust[1] == -1:
            continue
        defuse_amount = math.floor(dust_map[dust[0]][dust[1]]/5)
        for i in range(4):
            y = dust[0] + dy[i]
            x = dust[1] + dx[i]
            if (y < 0 or rows-1 < y
                or x < 0 or columns-1 < x):
                continue
            if dust_map[y][x] == -1:
                continue
            defuse_count += 1
            defuse_list.append([y, x, defuse_amount])
        dust_map[dust[0]][dust[1]] -= (defuse_amount * defuse_count)
        if dust_map[dust[0]][dust[1]] >= 5:
            dirty_air.append(dust)
    
    for defuse in defuse_list:
        if dust_map[defuse[0]][defuse[1]]>=5:
            dust_map[defuse[0]][defuse[1]] += defuse[2]
            continue
        dust_map[defuse[0]][defuse[1]] += defuse[2]
        if dust_map[defuse[0]][defuse[1]] >= 5:
            dirty_air.append([defuse[0],defuse[1]])
    return

def fix_upper_dirty_air(ac_y:int, columns: int, dirty_air: list):
    delete_index = -1
    for i in range(len(dirty_air)):
        if dirty_air[i][1] == 0 and dirty_air[i][0] < ac_y:
            if dirty_air[i][0] == ac_y-1:
                delete_index = i
                continue
            dirty_air[i][0] += 1
            
        if dirty_air[i][0] == 0:
            if dirty_air[i][1] == 0:
                dirty_air[i][0] = 1
                continue
            dirty_air[i][1] -= 1
        
        if dirty_air[i][1] == columns - 1 and dirty_air[i][0] < ac_y:
            if dirty_air[i][0] == 0:
                dirty_air[i][1] -= 1
                continue
            dirty_air[i][0] -= 1
            
        if dirty_air[i][0] == ac_y:
            if dirty_air[i][1] == columns-1:
                dirty_air[i][0] -= 1
                continue
            dirty_air[i][1] += 1
    return delete_index

def blow_upper_side(air_cleaner:list, columns:int, dust_map:list, dirty_air:list):
    dust_map[air_cleaner[0]-1][0] = 0
    for y in range(air_cleaner[0]-1):
        dust_map[air_cleaner[0]-1-y][0] = dust_map[air_cleaner[0]-2-y][0]
    for x in range(columns-1):
        dust_map[0][x] = dust_map[0][x+1]
    for y in range(air_cleaner[0]):
        dust_map[y][columns-1] = dust_map[y+1][columns-1]
    for x in range(columns-2):
        dust_map[air_cleaner[0]][columns-1-x] = dust_map[air_cleaner[0]][columns-2-x]
    dust_map[air_cleaner[0]][1] = 0
    delete_index = fix_upper_dirty_air(air_cleaner[0], columns, dirty_air)
    if delete_index < 0: return
    dirty_air[delete_index] = [-1, -1]
    return

def fix_lower_dirty_air(ac_y:int, columns: int, rows:int, dirty_air: list):
    delete_index = -1
    for i in range(len(dirty_air)):
        if dirty_air[i][1] == 0 and dirty_air[i][0] > ac_y:
            if dirty_air[i][0] == ac_y+1:
                delete_index = i
                continue
            dirty_air[i][0] -= 1
            
        if dirty_air[i][0] == rows-1:
            if dirty_air[i][1] == 0:
                dirty_air[i][0] -= 1
                continue
            dirty_air[i][1] -= 1
        
        if dirty_air[i][1] == columns - 1 and dirty_air[i][0] > ac_y:
            if dirty_air[i][0] == rows-1:
                dirty_air[i][1] -= 1
                continue
            dirty_air[i][0] += 1
            
        if dirty_air[i][0] == ac_y:
            if dirty_air[i][1] == columns-1:
                dirty_air[i][0] += 1
                continue
            dirty_air[i][1] += 1
    return delete_index

def blow_lower_side(air_cleaner:list, columns:int, rows:int, dust_map:list, dirty_air:list):
    dust_map[air_cleaner[0]+1][0] = 0
    for y in range(rows - air_cleaner[0]-2):
        dust_map[air_cleaner[0]+1+y][0] = dust_map[air_cleaner[0]+y+2][0]
    for x in range(columns-1):
        dust_map[rows-1][x] = dust_map[rows-1][x+1]
    for y in range(rows - air_cleaner[0]-1):
        dust_map[rows-1-y][columns-1] = dust_map[rows-2-y][columns-1]
    for x in range(columns-2):
        dust_map[air_cleaner[0]][columns-1-x] = dust_map[air_cleaner[0]][columns-2-x]
    dust_map[air_cleaner[0]][1] = 0
    delete_index = fix_lower_dirty_air(air_cleaner[0], columns, rows, dirty_air)
    if delete_index < 0: return
    dirty_air[delete_index] = [-1, -1]
    return

rows, columns, dust_map, time, dirty_air, air_cleaner = get_input()
for _ in range(time):
    defuse_dust(rows, columns, dust_map, dirty_air)
    blow_upper_side(air_cleaner[0], columns, dust_map, dirty_air)
    blow_lower_side(air_cleaner[1], columns, rows, dust_map, dirty_air)
result = 2147483647
result = 0
for row in dust_map:
    for value in row:
        result += value
print(result +2)