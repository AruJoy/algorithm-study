from sys import stdin
input = stdin.readline

def get_input():
    scale = int(input().strip())
    matrix = [[0 for _ in range(scale)]for __ in range(scale) ]
    sign_count = (scale**2 - scale)//2 +scale
    sign_list = list(input().strip())
    y = 0
    x = 0
    z = 0
    for i in range(sign_count):
        matrix[y][x] = sign_list[i]
        if x == scale-1:
            z += 1
            x = z
            y += 1
            continue
        x += 1
    return scale, matrix, sign_count
def check_number_list(matrix, number_list, dp, depth):
    for i in range(depth):
        num_sum = dp[i] + number_list[depth-1]
        if num_sum > 0 and matrix[i][depth-1] != "+":
            return False
        if num_sum < 0 and matrix[i][depth-1] != "-":
            return False
        if num_sum == 0 and matrix[i][depth-1] != "0":
            return False
        dp[i] = num_sum
    return True
def find_number_list(scale, matrix, sign_count, number_list, dp, depth):
    for i in range(0, 11):
        number_list.append(i)
        back_up_list = [j for j in dp]
        if check_number_list(matrix, number_list, dp, depth):
            if depth == scale: return True
            if find_number_list(scale, matrix, sign_count, number_list, dp, depth+1):
                return True
        for j in range(scale):
            dp[j] = back_up_list[j]
        number_list.pop()
        if i > 0:
            number_list.append(-i)
            back_up_list = [j for j in dp]
            if check_number_list(matrix, number_list, dp, depth):
                if depth == scale: return True
                if find_number_list(scale, matrix, sign_count, number_list, dp, depth+1):
                    return True
            for j in range(scale):
                dp[j] = back_up_list[j]
            number_list.pop()
    return False
def get_solution(scale, matrix, sign_count):
    number_list = []
    dp = [0 for i in range(scale)]
    find_number_list(scale, matrix, sign_count, number_list, dp, 1)
    print(*number_list)
    return
scale, matrix, sign_count = get_input()
get_solution(scale, matrix, sign_count)