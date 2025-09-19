from sys import stdin
input = stdin.readline

def init():
    rows, columns, _ = map(int, input().split(" "))
    m = []
    for _ in range(rows):
        row = list(map(int, input().split(" ")))
        m.append(row)
    c_list = list(map(int, input().split(" ")))
    return rows, columns, m, c_list
def act_1(rows, columns, m):
    new_m = [row[:] for row in m]
    for i in range(rows):
        new_m[rows-i-1] = m[i]
    return new_m
def act_2(rows, columns, m):
    new_m = [row[:] for row in m]
    for i in range(rows):
        for j in range(columns):
            new_m[i][columns - j - 1] = m[i][j]
    return new_m
def act_3(rows, columns, m):
    new_m = [[0 for _ in range(rows)] for _ in range(columns)]
    for i in range(rows):
        for j in range(columns):
            new_m[j][rows - i - 1] = m[i][j]
    return new_m
def act_4(rows, columns, m):
    new_m = [[0 for _ in range(rows)] for _ in range(columns)]
    for i in range(rows):
        for j in range(columns):
            new_m[columns - j - 1][i] = m[i][j]
    return new_m
def act_5(rows, columns, m):
    new_m = [row[:] for row in m]
    middle_y, middle_x = rows//2, columns//2
    start_list = [[0, 0], [0, middle_x], [middle_y, middle_x], [middle_y, 0]]
    end_list = [[0, middle_x], [middle_y, middle_x], [middle_y, 0], [0, 0]]
    for i in range(4):
        start = start_list[i]
        end = end_list[i]
        for j in range(middle_y):
            for k in range(middle_x):
                new_m[end[0] + j][end[1] + k] = m[start[0] + j][start[1] + k]
    return new_m
def act_6(rows, columns, m):
    new_m = [row[:] for row in m]
    middle_y, middle_x = rows//2, columns//2
    start_list = [[0, 0], [middle_y, 0], [middle_y, middle_x], [0, middle_x]]
    end_list = [[middle_y, 0], [middle_y, middle_x], [0, middle_x], [0, 0]]
    for i in range(4):
        start = start_list[i]
        end = end_list[i]
        for j in range(middle_y):
            for k in range(middle_x):
                new_m[end[0] + j][end[1] + k] = m[start[0] + j][start[1] + k]
    return new_m
def solution(r, c, m, c_list):
    matrix = m
    columns = c
    rows = r
    for c in c_list:
        if c == 1:
            matrix = act_1(rows, columns, matrix)
        if c == 2:
            matrix = act_2(rows, columns, matrix)
        if c == 3:
            matrix = act_3(rows, columns, matrix)
            columns, rows = rows, columns
        if c == 4:
            matrix = act_4(rows, columns, matrix)
            columns, rows = rows, columns
        if c == 5:
            matrix = act_5(rows, columns, matrix)
        if c == 6:
            matrix = act_6(rows, columns, matrix)
    for row in matrix:
        print(*row)
    return
rows, columns, m, c_list = init()

solution(rows, columns, m, c_list)