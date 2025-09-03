from sys import stdin
input = stdin.readline

def get_input():
    test_count = int(input())
    handel_list = []
    for i in range(test_count):
        handel_count = input().strip()
        new_handel = list(map(list, input().strip().split(" ")))
        handel_list.append(new_handel)
    return test_count, handel_list

def generate_cube():
    #----0
    U = [["w" for _ in range(3)] for __ in range(3)]
    #----1
    D = [["y" for _ in range(3)] for __ in range(3)]
    #----2
    F = [["r" for _ in range(3)] for __ in range(3)]
    #----3
    B = [["o" for _ in range(3)] for __ in range(3)]
    #----4
    L = [["g" for _ in range(3)] for __ in range(3)]
    #----5
    R = [["b" for _ in range(3)] for __ in range(3)]
    cube = [U, D, F, B, L, R]
    return cube

def rotate_space(surface: list ,direction: str):
    if direction == '+':
        rotated = [[surface[2-j][i] for j in range(3)] for i in range(3)]
    else:
        rotated = [[surface[j][2-i] for j in range(3)] for i in range(3)]
    for i in range(3):
        for j in range(3):
            surface[i][j] = rotated[i][j]

def rotate_upper_related_space(cube:list, direction: str):
    front = cube[2][0][:]
    right = cube[5][0][:]
    back = cube[3][0][:]
    left = cube[4][0][:]
    if direction == '+':
        cube[2][0] = right
        cube[5][0] = back
        cube[3][0] = left
        cube[4][0] = front
        return
    cube[2][0] = left
    cube[5][0] = front
    cube[3][0] = right
    cube[4][0] = back
    return
def rotate_down_related_space(cube:list, direction: str):
    front = cube[2][2][:]
    right = cube[5][2][:]
    back = cube[3][2][:]
    left = cube[4][2][:]
    if direction == '+':
        cube[2][2] = left
        cube[5][2] = front
        cube[3][2] = right
        cube[4][2] = back
        return
    cube[2][2] = right
    cube[5][2] = back
    cube[3][2] = left
    cube[4][2] = front
    return
def rotate_left_related_space(cube:list, direction: str):
    up = [cube[0][0][0],cube[0][1][0],cube[0][2][0]]
    front = [cube[2][0][0],cube[2][1][0],cube[2][2][0]]
    down = [cube[1][0][0],cube[1][1][0],cube[1][2][0]]
    back = [cube[3][2][2],cube[3][1][2],cube[3][0][2]]
    if direction == '+':
        for i in range(3):
            cube[0][i][0] = back[i]
            cube[2][i][0] = up[i]
            cube[1][i][0] = front[i]
            cube[3][i][2] = down[2-i]
        return
    for i in range(3):
        cube[0][i][0] = front[i]
        cube[2][i][0] = down[i]
        cube[1][i][0] = back[i]
        cube[3][i][2] = up[2-i]
    return
def rotate_right_related_space(cube:list, direction: str):
    up = [cube[0][0][2],cube[0][1][2],cube[0][2][2]]
    front = [cube[2][0][2],cube[2][1][2],cube[2][2][2]]
    down = [cube[1][0][2],cube[1][1][2],cube[1][2][2]]
    back = [cube[3][2][0],cube[3][1][0],cube[3][0][0]]
    if direction == '+':
        for i in range(3):
            cube[0][i][2] = front[i]
            cube[2][i][2] = down[i]
            cube[1][i][2] = back[i]
            cube[3][i][0] = up[2-i]
        return
    for i in range(3):
        cube[0][i][2] = back[i]
        cube[2][i][2] = up[i]
        cube[1][i][2] = front[i]
        cube[3][i][0] = down[2-i]
    return
def rotate_front_related_space(cube:list, direction: str):
    up = cube[0][2][:]
    right = [cube[5][0][0],cube[5][1][0],cube[5][2][0]]
    down = [cube[1][0][2],cube[1][0][1],cube[1][0][0]]
    left = [cube[4][2][2],cube[4][1][2],cube[4][0][2]]
    if direction == '+':
        for i in range(3):
            cube[0][2][i] = left[i]
            cube[4][i][2] = down[2-i]
            cube[1][0][i] = right[2-i]
            cube[5][i][0] = up[i]
        return
    for i in range(3):
        cube[0][2][i] = right[i]
        cube[4][i][2] = up[2-i]
        cube[1][0][i] = left[2-i]
        cube[5][i][0] = down[i]
    return
def rotate_back_related_space(cube:list, direction: str):
    up = cube[0][0][:]
    right = [cube[5][0][2],cube[5][1][2],cube[5][2][2]]
    down = [cube[1][2][2],cube[1][2][1],cube[1][2][0]]
    left = [cube[4][2][0],cube[4][1][0],cube[4][0][0]]
    if direction == '+':
        for i in range(3):
            cube[0][0][i] = right[i]
            cube[4][i][0] = up[2-i]
            cube[1][2][i] = left[2-i]
            cube[5][i][2] = down[i]
        return
    for i in range(3):
        cube[0][0][i] = left[i]
        cube[4][i][0] = down[2-i]
        cube[1][2][i] = right[2-i]
        cube[5][i][2] = up[i]
    return
def rotate(surface:str, direction:str, cube:list):
    if surface == "U":
        rotate_space(cube[0], direction)
        rotate_upper_related_space(cube, direction)
    if surface == "D":
        rotate_space(cube[1], direction)
        rotate_down_related_space(cube, direction)
    if surface == "F":
        rotate_space(cube[2], direction)
        rotate_front_related_space(cube, direction)
    if surface == "B":
        rotate_space(cube[3], direction)
        rotate_back_related_space(cube, direction)
    if surface == "L":
        rotate_space(cube[4], direction)
        rotate_left_related_space(cube, direction)
    if surface == "R":
        rotate_space(cube[5], direction)
        rotate_right_related_space(cube, direction)
    return
test_count, handel_list = get_input()


for test in range(test_count):
    cube = generate_cube()
    handels = handel_list[test]
    for handel in handels:
        rotate(handel[0], handel[1], cube)
    for i in range(3):
        print(''.join(str(cube[0][i][j]) for j in range(3)))