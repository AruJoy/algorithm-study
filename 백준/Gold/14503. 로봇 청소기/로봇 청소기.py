from sys import stdin
input = stdin.readline
from collections import deque

def act_1(room, y, x):
    if room[y][x] == 0 :
        room[y][x] = 2
        return 1
    return 0
def act_2(room, y, x, direction):
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    if (y + dy[direction] < 0
        or rows-1 < y + dy[direction]
        or x + dx[direction] < 0
        or columns - 1 < x + dx[direction]):
        return y + dy[direction], x + dx[direction], True
    if room[y + dy[direction]][x + dx[direction]] == 1:
        return y + dy[direction], x + dx[direction], True
    return y + dy[direction], x + dx[direction], False

def act_3(room, y, x, direction):
    new_direction = (direction + 3)%4
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    if (y + dy[new_direction] < 0
            or rows-1 < y + dy[new_direction]
            or x + dx[new_direction] < 0
            or columns - 1 < x + dx[new_direction]):
        return y, x, new_direction
    if room[y + dy[new_direction]][x + dx[new_direction]] == 0:
        return y + dy[new_direction], x + dx[new_direction], new_direction
    return y, x, new_direction

def judge_around(room, y, x):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        if (y + dy[i] < 0
            or rows-1 < y + dy[i]
            or x + dx[i] < 0
            or columns - 1 < x + dx[i]):
            continue 
        if room[y + dy[i]][x + dx[i]] == 0:
            return True
    return False

def clean_room(start_y, start_x, direction, room):
    answer = 0
    clean_end = False
    y = start_y
    x = start_x
    current_direction = direction
    while(not clean_end):
        answer += act_1(room, y, x)
        judge = judge_around(room, y, x)
        if not judge:
            y, x, clean_end = act_2(room, y, x, current_direction)
        if judge:
            y, x, current_direction = act_3(room, y, x, current_direction)
        if(y == start_y
            and x == start_x
            and current_direction == direction):
            clean_end = True
    return answer

rows, columns = map(int, input().split(" "))
start_y, start_x, direction = map(int, input().split(" "))

room = []
for _ in range(rows):
    new_row = list(map(int,input().split(" ")))
    room.append(new_row)

print(clean_room(start_y, start_x, direction, room))