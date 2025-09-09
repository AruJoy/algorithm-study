from sys import stdin
import math
input = stdin.readline

def get_input():
    shark_list = list()
    rows, columns, shark_count = map(int, input().split(" "))
    for i in range(shark_count):
        y, x, speed, direction, size = map(int, input().split(" "))
        shark_list.append([y, x, size, speed, direction])
    shark_list.sort(reverse=True)
    return rows, columns, shark_list

def catch_shark(x:int, shark_list:list):
    shark = 0
    for i in range(len(shark_list)):
        if shark_list[len(shark_list)-1 -i][1] == x:
            shark = shark_list[len(shark_list)-1 -i][2]
            shark_list.pop(len(shark_list)-1 -i)
            break
    return shark

def move_up(rows:int, shark:list):
    if shark[3] < shark[0]-1:
        shark[0] = shark[0] - shark[3]
        return
    run = shark[3] - shark[0] + 1
    times = math.floor(run / (rows-1))
    move = run % (rows-1)
    if times % 2 == 0:
        shark[4] = 2
        shark[0] = 1 + move
        return
    shark[0] = rows - move
    return
def move_down(rows:int, shark:list):
    if shark[3] < rows - shark[0]:
        shark[0] = shark[0] + shark[3]
        return
    run = shark[3] - rows + shark[0]
    times = math.floor(run / (rows-1))
    move = run % (rows-1)
    if times % 2 == 0:
        shark[4] = 1
        shark[0] = rows - move
        return
    shark[0] = 1 + move
    return
def move_left(columns:int, shark:list):
    if shark[3] < shark[1]-1:
        shark[1] = shark[1] - shark[3]
        return
    run = shark[3] - shark[1] + 1
    times = math.floor(run / (columns-1))
    move = run % (columns-1)
    if times % 2 == 0:
        shark[4] = 3
        shark[1] = 1 + move
        return
    shark[1] = columns - move
    return
def move_right(columns:int, shark:list):
    if shark[3] < columns - shark[1]:
        shark[1] = shark[1] + shark[3]
        return
    run = shark[3] - columns + shark[1]
    times = math.floor(run / (columns-1))
    move = run % (columns-1)
    if times % 2 == 0:
        shark[4] = 4
        shark[1] = columns - move
        return
    shark[1] = 1 + move
    return
def move_shark(rows:int, columns:int, shark_list:list):
    for shark in shark_list:
        if shark[4] == 1:
            move_up(rows, shark)
            continue
        if shark[4] == 2:
            move_down(rows, shark)
            continue
        if shark[4] == 3:
            move_right(columns, shark)
            continue
        if shark[4] == 4:
            move_left(columns, shark)
            continue
    shark_list.sort(reverse=True)
    delete_list = list()
    for i in range(len(shark_list)):
        if i == 0:
            continue
        if (shark_list[i][0] == shark_list[i-1][0]
            and shark_list[i][1] == shark_list[i-1][1]):
            delete_list.append(i)
    delete_list.sort(reverse=True)
    for index in delete_list:
        shark_list.pop(index)
    return

rows, columns, shark_list = get_input()
answer = 0
for i in range(columns):
    answer += catch_shark(i+1, shark_list)
    move_shark(rows, columns, shark_list)
print(answer)