from sys import stdin
input = stdin.readline
from collections import deque
import math

def get_input():
    rows, columns, time = map(int, input().split(" "))
    dust_map = []
    air_cleaner = []
    for i in range(rows):
        new_row = list(map(int, input().split(" ")))
        for j in range(columns):
            if new_row[j] == -1:
                air_cleaner.append([i,j])
        dust_map.append(new_row)
    return rows, columns, dust_map, time, air_cleaner

def defuse_dust(rows:int, columns:int, dust_map:list):
    dx = [0, -1, 1, 0]
    dy = [-1, 0, 0, 1]
    defuse_list = []
    for current_y in range(rows):
        for current_x in range(columns):
            defuse_count = 0
            if dust_map[current_y][current_x] < 5:
                continue
            defuse_amount = math.floor(dust_map[current_y][current_x]/5)
            for i in range(4):
                y = current_y + dy[i]
                x = current_x + dx[i]
                if (y < 0 or rows-1 < y
                    or x < 0 or columns-1 < x):
                    continue
                if dust_map[y][x] == -1:
                    continue
                defuse_count += 1
                defuse_list.append([y, x, defuse_amount])
            dust_map[current_y][current_x] -= (defuse_amount * defuse_count)
    
    for defuse in defuse_list:
        if dust_map[defuse[0]][defuse[1]]>=5:
            dust_map[defuse[0]][defuse[1]] += defuse[2]
            continue
        dust_map[defuse[0]][defuse[1]] += defuse[2]
    return

def blow_upper_side(air_cleaner:list, columns:int, dust_map:list):
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
    return

def blow_lower_side(air_cleaner:list, columns:int, rows:int, dust_map:list):
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
    return

rows, columns, dust_map, time, air_cleaner = get_input()
for _ in range(time):
    defuse_dust(rows, columns, dust_map)
    blow_upper_side(air_cleaner[0], columns, dust_map)
    blow_lower_side(air_cleaner[1], columns, rows, dust_map)
result = 2147483647
result = 0
for row in dust_map:
    for value in row:
        result += value
print(result +2)