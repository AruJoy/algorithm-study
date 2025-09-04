from sys import stdin
from collections import deque
import math
input = stdin.readline

def get_input():
    scale, n_tree, target_years = map(int, input().split(' '))
    farm = [[deque() for _ in range(scale)] for __ in range(scale)]
    nutrition_map = []

    for _ in range(scale):
        new_row = list(map(int, input().split(" ")))
        row = []
        for i in range(scale):
            sector = [5, new_row[i], 0]
            row.append(sector)
        nutrition_map.append(row)
    for i in range(n_tree):
        y, x, age = map(int, input().split(" "))
        farm[y-1][x-1].append(age)
    return scale, target_years, farm, nutrition_map

def spring(scale: int, farm: list, nutrition_map: list):
    tree_count = 0
    for i in range(scale):
        for j in range(scale):
            if len(farm[i][j]) == 0 :
                continue
            live_tree_count = 0
            for k in range(len(farm[i][j])):
                if farm[i][j][k] <= nutrition_map[i][j][0]:
                    tree_count += 1
                    live_tree_count += 1
                    nutrition_map[i][j][0] -= farm[i][j][k]
                    farm[i][j][k] += 1
                    continue
                nutrition_map[i][j][2] += math.floor(farm[i][j][k]/2)
            if live_tree_count == 0:
                farm[i][j].clear()
                continue
            for _ in range(len(farm[i][j]) - live_tree_count):
                farm[i][j].pop()
    return tree_count

def summer(scale:int, nutrition_map:list):
    for i in range(scale):
        for j in range(scale):
            nutrition_map[i][j][0] += (nutrition_map[i][j][1]
                                        + nutrition_map[i][j][2])
            nutrition_map[i][j][2] = 0
    return

def judge_tree(scale:int, current_y: int, current_x: int, farm:list):
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    
    tree_count = 0
    for tree in farm[current_y][current_x]:
        if tree % 5 == 0:
            for i in range(8):
                y = current_y + dy[i]
                x = current_x + dx[i]
                if ( x < 0 or scale-1 < x
                    or y < 0 or scale-1 < y):
                    continue
                tree_count += 1
                farm[y][x].appendleft(1)
    return tree_count

def autumn(scale:int, farm: list):    
    tree_count = 0
    for current_y in range(scale):
        for current_x in range(scale):
            if len(farm[current_y][current_x]) == 0:
                continue
            tree_count += judge_tree(scale, current_y, current_x, farm)
    return tree_count

def get_answer(scale: list, target_years: int, farm: list, nutrition_map: list):
    answer = 0
    for _ in range(target_years):
        answer = 0
        answer += spring(scale, farm, nutrition_map)
        summer(scale, nutrition_map)
        answer += autumn(scale, farm)
    return answer
scale, target_years, farm, nutrition_map = get_input()
print(get_answer(scale, target_years, farm, nutrition_map))