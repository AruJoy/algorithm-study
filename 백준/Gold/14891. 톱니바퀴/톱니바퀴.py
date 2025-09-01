from sys import stdin
from collections import deque
input = stdin.readline

def get_input():
    gears = []
    for _ in range(4):
        gears.append(list(map(int, input().strip())))
    rotation_count = int(input())
    rotations = []
    for _ in range(rotation_count):
        rotations.append(list(map(int, input().split(" "))))
    return gears, rotation_count, rotations

gear_states = [0 for _ in range(4)]

def get_left(gear: list, gear_state: int):
    if gear_state < 2:
        return gear[7 - 1 + gear_state]
    return gear[gear_state - 2]

def get_right(gear: list, gear_state: int):
    if gear_state > 5:
        return gear[1 - 7 + gear_state]
    return gear[gear_state + 2]

def rotate(direction: int, gear_state: int):
    if(direction == 1): 
        return 7 if gear_state == 0 else gear_state - 1
    return 0 if gear_state == 7 else gear_state + 1

def left_diffusion(gear_number: int, direction: int, gears:list, gear_states:list):
    if gear_number == 0:
        return
    before_gear_left = get_left(gears[gear_number], gear_states[gear_number])
    current_gear_right = get_right(gears[gear_number-1], gear_states[gear_number-1])
    if before_gear_left == current_gear_right: 
        return
    
    gear_state_after_rotate = rotate(direction, gear_states[gear_number-1])
    left_diffusion(gear_number-1, -direction, gears, gear_states)
    gear_states[gear_number-1] = gear_state_after_rotate
    return

def right_diffusion(gear_number: int, direction: int, gears:list, gear_states:list):
    if gear_number == 3:
        return
    before_gear_left = get_right(gears[gear_number], gear_states[gear_number])
    current_gear_right = get_left(gears[gear_number+1], gear_states[gear_number+1])
    if before_gear_left == current_gear_right: 
        return
    
    gear_state_after_rotate = rotate(direction, gear_states[gear_number+1])
    right_diffusion(gear_number+1, -direction, gears, gear_states)
    gear_states[gear_number+1] = gear_state_after_rotate
    return
    
def rotate_gear(gear_number:int, direction:int, gears:list, gear_states:list):
    gear_state_after_rotate = rotate(direction, gear_states[gear_number])
    
    left_diffusion(gear_number, -direction, gears, gear_states)
    right_diffusion(gear_number, -direction, gears, gear_states)
    
    gear_states[gear_number] = gear_state_after_rotate
    return

def get_answer(gears:list, gear_states:list):
    answer = 0
    for i in range(4):
        answer += gears[i][gear_states[i]]*(2**i)
    return answer

gears, rotation_count, rotations = get_input()

for i in range(rotation_count):
    rotate_gear(rotations[i][0]-1, rotations[i][1], gears, gear_states)

print(get_answer(gears, gear_states))