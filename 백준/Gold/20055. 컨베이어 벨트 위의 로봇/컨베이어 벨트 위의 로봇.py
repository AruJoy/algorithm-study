from sys import stdin
input = stdin.readline
def get_input():
    length, limit = map(int, input().split(" "))
    conveyor_list = list(map(int, input().split(" ")))
    robot_list = [False for _ in range(length*2)]
    z_points = 0
    for value in conveyor_list:
        if value == 0:
            z_points += 1
    return length, limit, conveyor_list, robot_list, z_points

def move_conveyor(entry_pointer:int, exit_pointer:int, length:int):
    next_entry = entry_pointer
    next_exit = exit_pointer
    
    if next_entry == 0:
        next_entry = 2*length-1
    else: next_entry -= 1
    
    if next_exit == 0:
        next_exit = 2*length-1
    else: next_exit -= 1
    
    return next_entry, next_exit

def check_robot_exit(robot_list:list, exit_pointer:int):
    robot_list[exit_pointer] = False
    return

def move_robots(conveyor_list:list, robot_list:list, length:int, exit_pointer:int):
    additional_z_points = 0
    move_pointer = exit_pointer
    robot_pointer = 2*length-1 if move_pointer == 0 else move_pointer-1
    for _ in range(length-1):
        if robot_list[robot_pointer] and not robot_list[move_pointer]:
            if conveyor_list[move_pointer] > 0:
                if conveyor_list[move_pointer] == 1:
                    additional_z_points += 1
                conveyor_list[move_pointer] -= 1
                robot_list[move_pointer] = True
                robot_list[robot_pointer] = False
        move_pointer = robot_pointer
        robot_pointer = 2*length-1 if move_pointer == 0 else move_pointer-1
    return additional_z_points

def put_robot_on_entry(conveyor_list:list, robot_list:list, entry_pointer:int):
    if conveyor_list[entry_pointer] > 0:
        conveyor_list[entry_pointer] -= 1
        robot_list[entry_pointer] = True
        return 1 if conveyor_list[entry_pointer] < 1 else 0
    return 0

def get_answer(length:int, limit:int, conveyor_list:list, robot_list:list, z_points:int):
    turn = 1
    now_z_points = z_points
    entry_pointer = 0
    exit_pointer = length-1
    while True:
        entry_pointer, exit_pointer = move_conveyor(entry_pointer, exit_pointer, length)
        check_robot_exit(robot_list, exit_pointer)
        now_z_points += move_robots(conveyor_list, robot_list, length, exit_pointer)
        check_robot_exit(robot_list, exit_pointer)
        now_z_points += put_robot_on_entry(conveyor_list, robot_list, entry_pointer)
        if now_z_points >= limit:
            break
        turn += 1
    return turn
length, limit, conveyor_list, robot_list, z_points = get_input()
print(get_answer(length, limit, conveyor_list, robot_list, z_points))