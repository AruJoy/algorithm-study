from sys import stdin
input = stdin.readline

def get_input():
    y, x, target = map(int, input().split(' '))

    matrix = list()
    for _ in range(3):
        row = list(map(int, input().split(" ")))
        matrix.append(row)
    return matrix, y - 1, x - 1, target

def judge_satisfying(matrix:list, y:int, x:int, target:list):
    if len(matrix) -1 >= y :
        if len(matrix[y]) -1 >= x:
            return matrix[y][x] == target
    return False
def row_cal(matrix: list):
    max_length = 0
    for i in range(len(matrix)):
        matrix[i].sort()
        value = -1
        count = 0
        new_items = []
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                continue
            if value == matrix[i][j]:
                count += 1
                continue
            if value == -1:
                value = matrix[i][j]
                count += 1
                continue
            new_items.append((count, value))
            value = matrix[i][j]
            count = 1
        new_items.append((count, value))
        new_items.sort()
        new_row = []
        for count, value in new_items:
            new_row.append(value)
            new_row.append(count)
        
        matrix[i] = new_row
        max_length = max(max_length, len(new_row))
        
    target_length = min(max_length, 100)
    for i in range(len(matrix)):
        if len(matrix[i]) > 100:
            matrix = matrix[0:100]
            continue
        if len(matrix[i]) < target_length:
            matrix[i] = matrix[i] + [0 for _ in range(target_length - len(matrix[i]))]
    return matrix

def column_cal(matrix: list):
    max_length = 0
    new_matrix = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]

    for i in range(len(new_matrix)):
        new_matrix[i].sort()
        value = 0
        count = 0
        new_items = []
        for j in range(len(new_matrix[i])):
            if new_matrix[i][j] == 0:
                continue
            if value == new_matrix[i][j]:
                count += 1
                continue
            if value == 0:
                value = new_matrix[i][j]
                count += 1
                continue
            new_items.append((count, value))
            value = new_matrix[i][j]
            count = 1
        new_items.append((count, value))
        new_items.sort()
        new_row = []
        for count, value in new_items:
            new_row.append(value)
            new_row.append(count)
        new_items.append((count, value))
        new_matrix[i] = new_row
        max_length = max(max_length, len(new_row))
        
    target_length = min(max_length, 100)
    for i in range(len(new_matrix)):
        if len(new_matrix[i]) > 100:
            new_matrix = new_matrix[0:100]
            continue
        if len(new_matrix[i]) < target_length:
            new_matrix[i] = new_matrix[i] + [0 for _ in range(target_length - len(new_matrix[i]))]
    return [[new_matrix[i][j] for i in range(len(new_matrix))] for j in range(len(new_matrix[0]))]
def simulate_matrix_cal(matrix: list):
    if len(matrix) >= len(matrix[0]):
        return row_cal(matrix)
    return column_cal(matrix)

def get_answer(matrix: list, y: int, x: int, target: int):
    control_matrix = matrix
    for time in range(100):
        if judge_satisfying(control_matrix, y, x, target):
            return time
        control_matrix = simulate_matrix_cal(control_matrix)
    if judge_satisfying(control_matrix, y, x, target):
        return 100
    return -1
matrix, y, x, target = get_input()

print(get_answer(matrix, y, x, target))