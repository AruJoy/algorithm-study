from sys import stdin
input = stdin.readline

def get_input():
    scale = int(input().strip())
    matrix = [[0 for _ in range(scale)]for __ in range(scale) ]
    sign_count = (scale**2 - scale)//2 +scale
    sign_list = list(input().strip())
    y = 0
    x = scale
    z = scale
    for i in range(sign_count):
        matrix[y][scale-x] = sign_list[i]
        if x == 1:
            z -= 1
            x = z
            y += 1
            continue
        x -= 1
    return scale, matrix, sign_count
def check_number_list(matrix, number_list, depth):
    check_count = (depth**2 - depth)//2 +depth
    x = 0
    y = 0
    j = 0
    num_sum = 0
    for i in range(check_count):
        num_sum += number_list[x]
        if num_sum > 0 and matrix[y][x] != "+":
            return False
        if num_sum < 0 and matrix[y][x] != "-":
            return False
        if num_sum == 0 and matrix[y][x] != "0":
            return False
        if x == depth-1:
            j += 1
            x = j
            y += 1
            num_sum = 0
            continue
        x += 1
    return True
def find_number_list(scale, matrix, sign_count, number_list, depth):
    for i in range(0, 11):
        number_list.append(i)
        if check_number_list(matrix, number_list, depth):
            if depth == scale: return True
            if find_number_list(scale, matrix, sign_count, number_list, depth+1):
                return True
        number_list.pop()
        if i > 0:
            number_list.append(-i)
            if check_number_list(matrix, number_list, depth):
                if depth == scale: return True
                if find_number_list(scale, matrix, sign_count, number_list, depth+1):
                    return True
            number_list.pop()
    return False
def get_solution(scale, matrix, sign_count):
    number_list = []
    find_number_list(scale, matrix, sign_count, number_list, 1)
    print(*number_list)
    return
scale, matrix, sign_count = get_input()
get_solution(scale, matrix, sign_count)