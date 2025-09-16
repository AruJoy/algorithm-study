from sys import stdin
input = stdin.readline
import math
def get_input():
    scale, fire_balls, time = map(int, input().split(" "))
    field_map = [[[] for _ in range(scale)] for __ in range(scale)]
    fire_ball_list = []
    total_mass = 0
    for _ in range(fire_balls):
        row, column, mass, speed, direction = map(int, input().split(" "))
        field_map[row-1][column-1].append([mass, speed, direction])
        total_mass += mass
        fire_ball_list.append([row-1, column-1, direction, speed, mass])
    return scale, time, total_mass, field_map, fire_ball_list

def move_fire_balls(scale:int, field_map:list, fire_ball_list:list):
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    for fire_ball in fire_ball_list:
        y = fire_ball[0] + (dy[fire_ball[2]] * fire_ball[3])
        x = fire_ball[1] + (dx[fire_ball[2]] * fire_ball[3])
        y = y % scale
        x = x % scale
        if y == fire_ball[0] and x == fire_ball[1]:
            continue
        for i in range(len(field_map[fire_ball[0]][fire_ball[1]])):
            if (field_map[fire_ball[0]][fire_ball[1]][i][0] == fire_ball[4]
                and field_map[fire_ball[0]][fire_ball[1]][i][1] == fire_ball[3]
                and field_map[fire_ball[0]][fire_ball[1]][i][2] == fire_ball[2]):
                field_map[fire_ball[0]][fire_ball[1]].pop(i)
                break
        fire_ball[0] = y
        fire_ball[1] = x
        field_map[y][x].append([fire_ball[4],fire_ball[3],fire_ball[2]])
    return

def merge_and_split_balls(field_map, fire_ball_list):
    pop_list = []
    merge_set = set()
    lose_mess = 0
    for i in range(len(fire_ball_list)):
        fire_ball = fire_ball_list[i]
        if len(field_map[fire_ball[0]][fire_ball[1]]) > 1:
            pop_list.append(i)
            merge_set.add((fire_ball[0], fire_ball[1]))
    for i in range(len(pop_list)):
        fire_ball_list.pop(pop_list[len(pop_list)-1-i])
    for y, x in merge_set:
        merge_mass = 0
        merge_speed = 0
        merge_count = len(field_map[y][x])
        first_is_odd = 0
        all_union = True
        for i in range(len(field_map[y][x])):
            fire_ball = field_map[y][x][i]
            if i == 0:
                first_is_odd = fire_ball[2] % 2
            elif first_is_odd != fire_ball[2] % 2:
                all_union = False
            merge_mass += fire_ball[0]
            merge_speed += fire_ball[1]
        field_map[y][x].clear()
        if merge_mass < 5:
            lose_mess += merge_mass
            continue
        direction = 0 if all_union else 1
        split_mass = math.floor(merge_mass/5)
        split_speed = math.floor(merge_speed / merge_count)
        lose_mess += merge_mass - (split_mass * 4)
        for i in range(4):
            field_map[y][x].append([split_mass, split_speed, i*2+direction])
        for i in range(4):
            fire_ball_list.append([y, x, i*2+direction, split_speed, split_mass])
    return lose_mess

def get_answer(scale:int, time:int, total_mass:int, field_map:list, fire_ball_list:list):
    current_mass = total_mass
    for _ in range(time):
        move_fire_balls(scale, field_map, fire_ball_list)
        current_mass -= merge_and_split_balls(field_map, fire_ball_list)
    return current_mass
scale, time, total_mass, field_map, fire_ball_list = get_input()
print(get_answer(scale, time, total_mass, field_map, fire_ball_list))