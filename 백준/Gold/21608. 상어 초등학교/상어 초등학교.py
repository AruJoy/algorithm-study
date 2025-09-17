from sys import stdin

input = stdin.readline

def get_input():
    scale = int(input().strip())
    student_list = [[-1,-1,[]] for i in range(scale**2)]
    student_order = []
    for i in range(scale**2):
        student = list(map(int, input().split(" ")))
        for j in range(4):
            student_list[student[0]-1][2].append(student[j+1]-1)
        student_order.append(student[0]-1)
    return scale, student_list, student_order
def find_favorite_position(class_map:list, student:list,
                            student_list:list, scale:int, dx:list, dy:list):
    favorite_position = []
    for i in range(4):
        favorite_student = student[2][i]
        if student_list[favorite_student][0] == -1:
            continue
        student_y = student_list[favorite_student][0]
        student_x = student_list[favorite_student][1]
        for j in range(4):
            y = student_y + dy[j]
            x = student_x + dx[j]
            if (y < 0 or scale-1 < y
                or x < 0 or scale-1 < x
                or class_map[y][x]>=0):
                continue
            already_exist = False
            for k in range(len(favorite_position)):
                if y == favorite_position[k][1] and x == favorite_position[k][2]:
                    favorite_position[k][0] += 1
                    already_exist = True
                    break
            if already_exist: continue
            favorite_position.append([1, y, x])
    favorite_position.sort(reverse=True)
    return favorite_position
def empty_case(class_map:list, scale:int, dx:int, dy:int):
    position_y = -1
    position_x = -1
    adjacent_count = -1
    for i in range(scale):
        for j in range(scale):
            current_y = scale-1-i
            current_x = scale-1-j
            if class_map[current_y][current_x] >= 0:
                continue
            count = 0
            for k in range(4):
                y = current_y + dy[k]
                x = current_x + dx[k]
                if (y < 0 or scale-1 < y
                    or x < 0 or scale-1 < x
                    or class_map[y][x]>=0):
                    continue
                count += 1
            if adjacent_count < count:
                position_y = current_y
                position_x = current_x
                adjacent_count = count
            if adjacent_count == 4:
                return position_y, position_x
    return position_y, position_x
def position(class_map:list, student:list, index:int, position_y:int, position_x:int):
    class_map[position_y][position_x] = index
    student[0] = position_y
    student[1] = position_x
    return
def get_position(class_map:list, favorite_position:list, scale:int, dx:list, dy:list):
    position_y = -1
    position_x = -1
    empty_count = -1
    favorite_count = -1
    for i in range(len(favorite_position)):
        p = favorite_position[i]
        if favorite_count > p[0]: break
        count = 0
        for i in range(4):
            y = p[1] + dy[i]
            x = p[2] + dx[i]
            if (y < 0 or scale-1 < y
                or x < 0 or scale-1 < x
                or class_map[y][x] >= 0):
                continue
            count += 1
        if i == 0:
            empty_count = count
            position_y = p[1]
            position_x = p[2]
            favorite_count = p[0]
            continue
        if empty_count < count:
            favorite_count = p[0]
            position_y = p[1]
            position_x = p[2]
            empty_count = count
        if empty_count == 4:
            return position_y, position_x
    return position_y, position_x
def student_get_position(class_map:list, student:list, index:int, student_list:list, scale:int):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    favorite_position = find_favorite_position(class_map, student,
                                                student_list, scale, dx, dy)
    if len(favorite_position) == 0:
        position_y, position_x = empty_case(class_map, scale, dx, dy)
        position(class_map, student, index, position_y, position_x)
        return
    position_y, position_x = get_position(class_map, favorite_position, scale, dx, dy)
    position(class_map, student, index, position_y, position_x)
    return
def get_satisfaction(scale:int, student_list:list, class_map:list):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    satisfaction = 0
    for i in range(scale):
        for j in range(scale):
            s = 0
            student = class_map[i][j]
            for k in range(4):
                y = i+dy[k]
                x = j+dx[k]
                if (y < 0 or scale-1 < y
                    or x <0 or scale-1 < x):
                    continue
                st = class_map[y][x]
                if st in student_list[student][2]:
                    s += 1
            if s == 4:
                satisfaction += 1000
                continue
            if s == 3:
                satisfaction += 100
                continue
            if s == 2:
                satisfaction += 10
                continue
            if s == 1:
                satisfaction += 1
                continue
    return satisfaction
def solution(scale, student_list, student_order):
    class_map = [[-1 for _ in range(scale)]for __ in range(scale)]
    for i in range(scale**2):
        student_get_position(class_map, student_list[student_order[i]], student_order[i], student_list, scale)
    return get_satisfaction(scale, student_list, class_map)
scale, student_list, student_order = get_input()
print(solution(scale, student_list, student_order))