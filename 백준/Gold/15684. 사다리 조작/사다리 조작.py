from sys import stdin
input = stdin.readline

def get_input():
    vertical_lines, default_ladders, horizontal_lines = map(int, input().split(" "))
    ladder_map = [[False for _ in range(vertical_lines-1)] for __ in range(horizontal_lines)]
    
    for _ in range(default_ladders):
        y, x = map(int, input().split(" "))
        ladder_map[y-1][x-1] = True
    
    return vertical_lines, horizontal_lines, ladder_map

def judge_answer(vertical_lines:int, horizontal_lines:int, ladder_map:list):
    dx = [-1, 0]
    for current_x in range(vertical_lines):
        position = current_x
        for y in range(horizontal_lines):
            for i in range(2):
                x = position + dx[i]
                if (x < 0 or vertical_lines - 2 < x):
                    continue
                if ladder_map[y][x] :
                    if i == 0:
                        position -=1
                    else:
                        position += 1
                    break
        if position != current_x:
            return False
    return True
def put_ladder(vertical_lines:int, horizontal_lines:int,ladder_map:list, depth: int, start_y:int, start_x:int ):
    global min_ans
    answer = 4
    dx = [-1, 1]
    if judge_answer(vertical_lines, horizontal_lines, ladder_map):
        return depth
    elif depth == 3 or depth >= min_ans - 1: return 4
    
    for y in range(start_y, horizontal_lines):
        for current_x in range(start_x if y == start_y else 0, vertical_lines-1):
            if ladder_map[y][current_x]:
                continue
            result = True
            for i in range(2):
                x = current_x + dx[i]
                if x < 0 or vertical_lines-2 < x:
                    continue
                if ladder_map[y][x]:
                    result = False
                    break
            if result:
                ladder_map[y][current_x] = True
                answer = min(answer, put_ladder(vertical_lines, horizontal_lines, ladder_map, depth+1, y, current_x))
                min_ans = answer
                ladder_map[y][current_x] = False
                if answer == depth:
                    return answer
    return answer
def get_answer(vertical_lines:int, horizontal_lines:int, ladder_map:list):
    answer = put_ladder(vertical_lines, horizontal_lines, ladder_map, 0, 0, 0)
    return answer if answer < 4 else -1
vertical_lines, horizontal_lines, ladder_map = get_input()
min_ans = 4
print(get_answer(vertical_lines, horizontal_lines, ladder_map))