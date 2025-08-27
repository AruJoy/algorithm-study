from sys import stdin
from collections import deque
from heapq import heappop, heappush

dice = [0 for i in range(6)]
dice_map = [1,2,3,4,5,6]

map_rows, map_columns, start_y, start_x, n_command = map(int, stdin.readline().split(' '))
game_map = []

x = start_x
y = start_y
for i in range(map_rows):
    row = list(map(int, stdin.readline().split(' ')))
    game_map.append(row)

def roll_dice(commend):
    global x, y, dice_map
    if commend == 1:
        if map_columns -1 <= x:
            return False
        x += 1
        dice_map = [dice_map[3], dice_map[1], dice_map[0], dice_map[5], dice_map[4], dice_map[2]]
        return True
    if commend == 2:
        if x <= 0:
            return False
        x -= 1
        dice_map = [dice_map[2], dice_map[1], dice_map[5], dice_map[0], dice_map[4], dice_map[3]]
        return True
    if commend == 3:
        if y <= 0:
            return False
        y -= 1
        dice_map = [dice_map[4], dice_map[0], dice_map[2], dice_map[3], dice_map[5], dice_map[1]]
        return True
    if commend == 4:
        if map_rows - 1 <= y:
            return False
        y += 1
        dice_map = [dice_map[1], dice_map[5], dice_map[2], dice_map[3], dice_map[0], dice_map[4]]
        return True

commands = list(map(int, stdin.readline().split(' ')))

for i in range(n_command):
    if not roll_dice(commands[i]):
        continue
    map_value = game_map[y][x]
    if map_value == 0:
        game_map[y][x] = dice[dice_map[5]-1]
    if map_value != 0:
        dice[dice_map[5]-1] = map_value
        game_map[y][x] = 0
    print (dice[dice_map[0] - 1])