from sys import stdin
input = stdin.readline

def get_input():
    max_gen = 0
    curve_count = int(input())
    curve_infos = []
    for _ in range(curve_count):
        x, y, direction, gen = map(int, input().split(" "))
        max_gen = max(gen, max_gen)
        curve_infos.append([y, x, direction, gen])
    
    return curve_count, curve_infos, max_gen

def generate_curves(max_gen: int):
    dragon_curves = []
    dragon_curves.append([[0,0],[0,1]])
    
    for gen in range(max_gen):
        before_gen = dragon_curves[gen]
        current_gen = [coordinate for coordinate in before_gen]
        for i in range(len(before_gen)-1):
            current_coordinate = before_gen[len(before_gen) -1 - i]
            before_coordinate = before_gen[len(before_gen) -2 - i]
            delta_y = before_coordinate[1] - current_coordinate[1]
            delta_x = current_coordinate[0] - before_coordinate[0]
            new_coordinate = [current_gen[-1][0] + delta_y, current_gen[-1][1] + delta_x]
            current_gen.append(new_coordinate)
        dragon_curves.append(current_gen)
    return dragon_curves

def mark_dots(dragon_curves: list, curve_infos:list):
    dot_map = [[False for _ in range(101)] for __ in range(101)]
    for curve in curve_infos:
        dragon_curve = dragon_curves[curve[3]]
        for dote_coordination in dragon_curve:
            if curve[2] == 0:
                dot_map[curve[0] + dote_coordination[0]][curve[1] + dote_coordination[1]] = True
            if curve[2] == 1:
                dot_map[curve[0] - dote_coordination[1]][curve[1] + dote_coordination[0]] = True
            if curve[2] == 2:
                dot_map[curve[0] - dote_coordination[0]][curve[1] - dote_coordination[1]] = True
            if curve[2] == 3:
                dot_map[curve[0] + dote_coordination[1]][curve[1] - dote_coordination[0]] = True
    return dot_map
def get_answer(dot_map: list):
    answer = 0
    dx = [0, 1, 0, 1]
    dy = [0, 0, 1, 1]
    for i in range(100):
        for j in range(100):
            is_square = True
            for k in range(4):
                if not dot_map[i + dy[k]][j + dx[k]]:
                    is_square = False
                    break
            if is_square:
                answer += 1
    return answer
curve_count, curve_infos, max_gen = get_input()
dragon_curves = generate_curves(max_gen)

dot_map = mark_dots(dragon_curves, curve_infos)
print(get_answer(dot_map))