from sys import stdin
input = stdin.readline

board_map = []
for i in range(20):
    if i == 4: 
        board_map.append(((i+1)*2, 20, i+1))
        continue
    if i == 9: 
        board_map.append(((i+1)*2, 26, i+1))
        continue
    if i == 14: 
        board_map.append(((i+1)*2, 23, i+1))
        continue
    if i == 19:
        board_map.append(((i+1)*2, -1, -1))
        continue
    board_map.append(((i+1)*2, -1, i+1))
for i in range(3):
    if i == 2:
        board_map.append((10 + (i+1)*3, -1, 28))
        continue
    board_map.append((10 + (i+1)*3, -1, 21+i))
for i in range(3):
    if i == 2:
        board_map.append((28-i, -1, 28))
        continue
    board_map.append((28-i, -1, 24+i))
board_map.append((22, -1, 27))
board_map.append((24, -1, 28))
board_map.append((25, -1, 29))
board_map.append((30, -1, 30))
board_map.append((35, -1, 19))

def move_unit(board_map, unit_list, unit_index, move_count):
    if move_count == 0:
        return 2
    if board_map[unit_list[unit_index]][1] != -1:
        unit_list[unit_index] = board_map[unit_list[unit_index]][1]
    elif board_map[unit_list[unit_index]][2] == -1 :
        unit_list[unit_index] = -2
        return 0
    else:
        unit_list[unit_index] = board_map[unit_list[unit_index]][2]
    
    for _ in range(move_count-1):
        if board_map[unit_list[unit_index]][2] == -1:
            unit_list[unit_index] = -2
            return 0
        unit_list[unit_index] = board_map[unit_list[unit_index]][2]
    return board_map[unit_list[unit_index]][0]


def select_unit(board_map: list, dice_list: list, unit_list: list, dice: int):
    max_result = 0
    for i in range(4):
        if unit_list[i] == -2:
            continue
        if unit_list[i] == -1:
            unit_list[i] = 0
            value = move_unit(board_map, unit_list, i, dice_list[dice]-1)
            invalid = False
            for j in range(4):
                if i == j:
                    continue
                if unit_list[i] == unit_list[j] != -2:
                    invalid = True
            if invalid:
                unit_list[i] = -1
                continue
            if dice == 9:
                max_result = max(max_result, value)
                unit_list[i] = -1
                continue
            value += select_unit(board_map, dice_list, unit_list, dice + 1)
            unit_list[i] = -1
            max_result = max(max_result, value)
            continue
        original_coordinate = unit_list[i]
        value = move_unit(board_map, unit_list, i, dice_list[dice])
        invalid = False
        for j in range(4):
            if i == j:
                continue
            if unit_list[i] == unit_list[j] != -2:
                invalid = True
        if invalid:
            unit_list[i] = original_coordinate
            continue
        if dice == 9:
            max_result = max(max_result, value)
            unit_list[i] = original_coordinate
            continue
        value += select_unit(board_map, dice_list, unit_list, dice + 1)
        unit_list[i] = original_coordinate
        max_result = max(max_result, value)
    return max_result

def get_answer(board_map:list, dice_list:list):
    unit_list = [-1 for _ in range(4)]
    
    return select_unit(board_map, dice_list, unit_list, 0)

dice_list = list(map(int, input().split(" ")))

print(get_answer(board_map, dice_list))