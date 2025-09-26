from sys import stdin
input = stdin.readline
from collections import deque
import math

def get_input():
    plate_count, number_count, move_count = map(int, input().split(" "))
    plate_list = []
    total_sum = 0
    for _ in range(plate_count):
        plate = list(map(int, input().split(" ")))
        for i in range(number_count):
            total_sum += plate[i]
        plate_list.append(plate)
    return  plate_count, number_count, move_count, plate_list, total_sum

def rotate_plate(plate:int, direction:int, count:int, number_count:int, plate_list:list):
    if direction == 0:
        plate_list[plate] = (plate_list[plate][number_count - count : number_count] +
                                                plate_list[plate][0: number_count - count])
    else:
        plate_list[plate] = (plate_list[plate][count : number_count] +
                                                plate_list[plate][0 : count])

def rotate(plate_count:int, plate_number: int, direction: int, count: int,
                    number_count: int, plate_list: list):
    repeat = math.floor(plate_count / plate_number)
    
    for i in range(repeat):
        plate = ((i + 1) * plate_number) - 1
        rotate_plate(plate, direction, count, number_count, plate_list)
    return

def delete_adj_number_in_first_index(plate_count: int, number_count: int, plate_list: list):
    dy = [-1, 1]
    remove_set = set()
    for i in range(plate_count):
        for j in range(number_count):
            adj_number = j - 1
            if plate_list[i][j] == plate_list[i][adj_number] and plate_list[i][j] >= 0:
                remove_set.add((i, j))
                if adj_number == -1:
                    remove_set.add((i, number_count-1))
                else:
                    remove_set.add((i, adj_number))
            for k in range(2):
                y = i + dy[k]
                if y < 0 or plate_count - 1 < y or plate_list[i][j] < 0:
                    continue
                if plate_list[y][j] == plate_list[i][j]:
                    remove_set.add((y,j))
                    remove_set.add((i,j))
    return remove_set

def remove_target(remove_set:set, plate_list:list):
    remove_numbers = 0
    remove_count = 0
    for y, x in remove_set:
        remove_numbers += plate_list[y][x]
        remove_count += 1
        plate_list[y][x] = -1
    return remove_numbers, remove_count
    
def adjust_numbers(plate_list: list, total_sum: int, total_count:int, plate_count:int, number_count:int):
    current_sum = total_sum
    avg = total_sum/total_count
    for i in range(plate_count):
        for j in range(number_count):
            if plate_list[i][j] < 0 or plate_list[i][j] == avg:
                continue
            if plate_list[i][j] < avg:
                current_sum += 1
                plate_list[i][j] += 1
                continue
            current_sum -= 1
            plate_list[i][j] -= 1
    return current_sum

plate_count, number_count, move_count, plate_list, total_sum = get_input()
total_count = plate_count*number_count
for i in range(move_count):
    remove_set = set()
    plate_number, direction, count = map(int, input().split(" "))
    rotate(plate_count, plate_number, direction, count, number_count, plate_list)
    remove_set = remove_set | delete_adj_number_in_first_index(plate_count, number_count, plate_list)
    if len(remove_set) == 0:
        total_sum = adjust_numbers(plate_list, total_sum, total_count, plate_count, number_count)
        continue
    remove_numbers, remove_count = remove_target(remove_set, plate_list)
    total_sum -= remove_numbers
    total_count -= remove_count
    if total_count == 0 or total_sum == 0:
        break
print(total_sum)