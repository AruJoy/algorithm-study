from sys import stdin
input = stdin.readline
from collections import deque
def act_1(scale, matrix, s_scale):
    new_matrix = [row[:] for row in matrix]
    for i in range(scale//s_scale):
        for j in range(scale//s_scale):
            start_y, end_y = i*s_scale, (i+1)*s_scale
            start_x, end_x = j*s_scale, (j+1)*s_scale
            for dy in range(s_scale):
                for dx in range(s_scale):
                    new_matrix[start_y+dy][start_x+dx] = matrix[end_y-dy-1][start_x+dx]
    return new_matrix
def act_2(scale, matrix, s_scale):
    new_matrix = [row[:] for row in matrix]
    for i in range(scale//s_scale):
        for j in range(scale//s_scale):
            start_y, end_y = i*s_scale, (i+1)*s_scale
            start_x, end_x = j*s_scale, (j+1)*s_scale
            for dy in range(s_scale):
                for dx in range(s_scale):
                    new_matrix[start_y+dy][start_x+dx] = matrix[start_y+dy][end_x-dx-1]
    return new_matrix
def act_3(scale, matrix, s_scale):
    new_matrix = [row[:] for row in matrix]
    for i in range(scale//s_scale):
        for j in range(scale//s_scale):
            start_y, end_y = i*s_scale, (i+1)*s_scale
            start_x, end_x = j*s_scale, (j+1)*s_scale
            for dy in range(s_scale):
                for dx in range(s_scale):
                    new_matrix[start_y+dy][start_x+dx] = matrix[end_y-dx-1][start_x+dy]
    return new_matrix
def act_4(scale, matrix, s_scale):
    new_matrix = [row[:] for row in matrix]
    for i in range(scale//s_scale):
        for j in range(scale//s_scale):
            start_y, end_y = i*s_scale, (i+1)*s_scale
            start_x, end_x = j*s_scale, (j+1)*s_scale
            for dy in range(s_scale):
                for dx in range(s_scale):
                    new_matrix[start_y+dy][start_x+dx] = matrix[start_y+dx][end_x-dy-1]
    return new_matrix
def act_5(scale, matrix, s_scale):
    new_matrix = [row[:] for row in matrix]
    repeat = scale//s_scale
    for i in range(repeat):
        for j in range(repeat):
            for dy in range(s_scale):
                for dx in range(s_scale):
                    new_matrix[i*s_scale+dy][j*s_scale+dx] = matrix[(repeat-1-i)*s_scale+dy][j*s_scale+dx]
    return new_matrix
def act_6(scale, matrix, s_scale):
    new_matrix = [row[:] for row in matrix]
    repeat = scale//s_scale
    for i in range(repeat):
        for j in range(repeat):
            for dy in range(s_scale):
                for dx in range(s_scale):
                    new_matrix[i*s_scale+dy][j*s_scale+dx] = matrix[i*s_scale+dy][(repeat-1-j)*s_scale+dx]
    return new_matrix
def act_7(scale, matrix, s_scale):
    new_matrix = [row[:] for row in matrix]
    repeat = scale//s_scale
    for i in range(repeat):
        for j in range(repeat):
            for dy in range(s_scale):
                for dx in range(s_scale):
                    new_matrix[i*s_scale+dy][j*s_scale+dx] = matrix[(repeat-1-j)*s_scale+dy][i*s_scale+dx]
    return new_matrix
def act_8(scale, matrix, s_scale):
    new_matrix = [row[:] for row in matrix]
    repeat = scale//s_scale
    for i in range(repeat):
        for j in range(repeat):
            for dy in range(s_scale):
                for dx in range(s_scale):
                    new_matrix[i*s_scale+dy][j*s_scale+dx] = matrix[j*s_scale+dy][(repeat-1-i)*s_scale+dx]
    return new_matrix
def commend(scale, matrix, s_scale, c):
    commend_map = {1: act_1, 2: act_2, 3: act_3, 4: act_4,
                    5: act_5, 6: act_6, 7: act_7, 8: act_8}
    return commend_map[c](scale, matrix, s_scale)
def main():
    power, c_count = map(int, input().split())
    matrix = []
    scale = 2**power
    for _ in range(scale):
        matrix.append(list(map(int, input().split())))
    for _ in range(c_count):
        c, s_power = map(int, input().split())
        s_scale = 2**s_power
        matrix = commend(scale, matrix, s_scale, c)

    print("\n".join(" ".join(map(str, row))for row in matrix))
    return
if __name__ == "__main__":
    main()
