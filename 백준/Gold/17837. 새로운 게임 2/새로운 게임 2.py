from sys import stdin
input = stdin.readline

def get_input():
    scale, unit_count = map(int, input().split(" "))
    board = [[[0, -1] for _ in range(scale)] for __ in range(scale)]
    unit_list = []
    for i in range(scale) :
        row = list(map(int, input().split(" ")))
        for j in range(scale):
            if row[j] == 1:
                board[i][j][0] = 1
                continue
            if row[j] == 2:
                board[i][j][0] = 2
    for i in range(unit_count): 
        y, x, direction = map(int, input().split(" "))
        if direction == 1:
            unit_list.append([-1, -1, [y-1, x-1, 2]])
        if direction == 2:
            unit_list.append([-1, -1, [y-1, x-1, 0]])
        if direction == 3:
            unit_list.append([-1, -1, [y-1, x-1, 1]])
        if direction == 4:
            unit_list.append([-1, -1, [y-1, x-1, 3]])
        board[y-1][x-1][1] = i
    return scale, board, unit_count, unit_list

def reverse_units(unit_list: list, unit_number: int):
    units = 0
    cursor = unit_number
    first_unit = unit_number
    while cursor >= 0:
        parent = unit_list[cursor][0]
        child = unit_list[cursor][1]
        unit_list[cursor][0] = child
        unit_list[cursor][1] = parent
        first_unit = cursor
        cursor = child
        units += 1
    return first_unit, units
def count_units(unit_list: list, first_unit: int):
    units = 0
    cursor = first_unit
    while cursor >= 0:
        cursor = unit_list[cursor][1]
        units += 1
    return units
def get_last_unit(unit_list: list, unit_number: int):
    units = 0
    cursor = unit_number
    last_unit = unit_number
    while cursor >= 0:
        child = unit_list[cursor][1]
        if child >= 0:
            last_unit = child
        cursor = child
        units += 1
    return last_unit, units
def move_propagate(patent_number: int, unit_number: int, unit_list: list, y: int, x: int):
    unit_list[unit_number][0] = patent_number
    if(patent_number >= 0):
        unit_list[patent_number][1] = unit_number
    cursor = unit_number
    while cursor >= 0:
        unit_list[cursor][2][0] = y
        unit_list[cursor][2][1] = x
        cursor = unit_list[cursor][1]
    return False
def move_to_next_position(unit_list: list, unit_number: int, before_y: int, before_x: int, y: int, x: int, board: list):
    parent_no = unit_list[unit_number][0]
    units = 0
    first_unit = unit_number
    if parent_no != -1:
        unit_list[parent_no][1] = -1
        unit_list[unit_number][0] = -1
    else:
        board[before_y][before_x][1] = -1
    if board[y][x][0] == 1:
        first_unit, units = reverse_units(unit_list, first_unit)
    else:
        units = count_units(unit_list, first_unit)

    if board[y][x][1] == -1:
        board[y][x][1] = first_unit
        return move_propagate(-1, first_unit, unit_list, y, x)
    last_unit, original_units = get_last_unit(unit_list, board[y][x][1])
    if original_units + units > 3:
        return True
    return move_propagate(last_unit, first_unit, unit_list, y, x)

def move_to_blue(scale: int, unit_list: list, unit_number: int, y: int, x: int, direction: int, board: list):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    next_y = y + dy[direction]
    next_x = x + dx[direction]
    if(next_y < 0 or scale-1 < next_y
        or next_x < 0 or scale-1 < next_x
        or board[next_y][next_x][0] == 2):
        return False
    
    return move_to_next_position(unit_list, unit_number, unit_list[unit_number][2][0],
                                    unit_list[unit_number][2][1], next_y, next_x, board)

def move_unit(scale: int, unit_number: int, board: list, unit_list: list):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    next_y = unit_list[unit_number][2][0] + dy[unit_list[unit_number][2][2]]
    next_x = unit_list[unit_number][2][1] + dx[unit_list[unit_number][2][2]]
    if(next_y < 0 or scale-1 < next_y
        or next_x < 0 or scale-1 < next_x
        or board[next_y][next_x][0] == 2):
        unit_list[unit_number][2][2] = (unit_list[unit_number][2][2]+2) % 4
        return move_to_blue(scale, unit_list, unit_number, unit_list[unit_number][2][0], unit_list[unit_number][2][1], unit_list[unit_number][2][2], board)
    
    return move_to_next_position(unit_list, unit_number, unit_list[unit_number][2][0],
                                    unit_list[unit_number][2][1], next_y, next_x, board)

def get_answer(scale:int, board:list, unit_count:int, unit_list:list):
    for turn in range(1000):
        for unit_number in range(unit_count):
            if move_unit(scale, unit_number, board, unit_list):
                return turn+1
    return -1

scale, board, unit_count, unit_list = get_input()
print(get_answer(scale, board, unit_count, unit_list))