from sys import stdin
input = stdin.readline
import math
def get_input():
    scale = int(input().strip())
    start = math.floor((scale - 1)/2)
    sand_map = []
    for _ in range(scale):
        row = list(map(int, input().split(" ")))
        sand_map.append(row)
    return scale, sand_map, start
def move_tornado(scale:int, sand_map:list, start_y:int, start_x:int, direction:int, dust:list, dust_c:list):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    next_y = start_y + dy[direction]
    next_x = start_x + dx[direction]
    alpha_dust = sand_map[next_y][next_x]
    sand_map[next_y][next_x] = 0
    lost_dust = 0
    real_lost_dust = 0
    alpha_y = start_y + 2*dy[direction]
    alpha_x = start_x + 2*dx[direction]
    for i in range(9):
        target_y = next_y + dust_c[i][0]
        target_x = next_x + dust_c[i][1]
        dust_amount = math.floor(alpha_dust*dust[i]/100)
        lost_dust += dust_amount
        if (target_y < 0 or scale-1 < target_y
            or target_x < 0 or scale -1 < target_x):
            real_lost_dust += dust_amount
            continue
        sand_map[target_y][target_x] += dust_amount
    alpha_dust -= lost_dust
    if (alpha_y < 0 or scale-1 < alpha_y
            or alpha_x < 0 or scale -1 < alpha_x):
        real_lost_dust += alpha_dust
        return next_y, next_x, real_lost_dust
    sand_map[alpha_y][alpha_x] += alpha_dust
    return next_y, next_x, real_lost_dust
def get_answer(scale:int, sand_map:list, start:int):
    current_y = start
    current_x = start
    dust = [2, 10, 7, 1, 5, 10, 7, 1, 2]
    dust_c = [[-2,0],[-1,-1],[-1,0],[-1,1],[0,-2],[1,-1],[1,0],[1,1],[2,0]]
    direction = 0
    move_count = 1
    real_lost_dust = 0
    # rotation = [[0, -1],
    #             [1, 0]]
    while True:
        for _ in range(2):
            for __ in range(move_count):
                current_y, current_x, lost_dust = move_tornado(scale, sand_map, current_y, current_x, direction, dust, dust_c)
                real_lost_dust += lost_dust
                if current_x == 0 and current_y == 0:
                    return real_lost_dust
            direction = (direction+1) % 4
            for i in range(9):
                new_x = dust_c[i][0]
                new_y = -dust_c[i][1]
                dust_c[i][0] = new_y
                dust_c[i][1] = new_x
        move_count += 1
        if current_x == 0 and current_y == 0:
            return real_lost_dust
scale, sand_map, start = get_input()
print(get_answer(scale, sand_map, start))