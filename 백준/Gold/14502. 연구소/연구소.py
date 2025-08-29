from sys import stdin
input = stdin.readline
from collections import deque

rows, columns = map(int, input().split(" "))

input_map = []
check_map = [[False for _ in range(columns)]for __ in range(rows)]
z_points = []
z_count = 0
dy = [0, 0, 1, -1]
dx = [-1, 1, 0, 0]
def is_zero(y,x,space):
    global z_count
    if space == 0:
        z_points.append([y,x])
        z_count += 1

def diffusion(i_map, c_map, point):
    que = deque()
    que.append(point)
    contaminations = 0
    while (len(que) != 0):
        new_point = que.popleft()
        for i in range(4):
            if (new_point[0] + dy[i] < 0
                or rows <= new_point[0] + dy[i]
                or new_point[1] + dx[i] < 0
                or columns <= new_point[1] + dx[i]):
                continue
            if i_map[new_point[0] + dy[i]][new_point[1] + dx[i]] == 0:
                i_map[new_point[0] + dy[i]][new_point[1] + dx[i]] = 2
                c_map[new_point[0] + dy[i]][new_point[1] + dx[i]] = True
                contaminations += 1
                que.append([new_point[0] + dy[i],new_point[1] + dx[i]])
    return contaminations

def simulate(i_map, c_map, points):
    contaminations = 0
    for z_point in points:
        i_map[z_point[0]][z_point[1]] = 1
    
    for y in range(rows):
        for x in range(columns):
            if i_map[y][x] == 2 and not c_map[y][x]:
                contaminations += diffusion(i_map, c_map, [y,x])

    return z_count - contaminations - 3

for row in range(rows):
    new_row = list(map(int, input().split(" ")))
    input_map.append(new_row)
    for column in range(columns):
        is_zero(row, column, new_row[column])

answer = 0
for i in range(len(z_points)):
    for j in range(i,len(z_points)):
        for k in range(j,len(z_points)):
            simulation_result = simulate([row[:] for row in input_map], [row[:] for row in check_map], [z_points[i],z_points[j],z_points[k]])
            answer = max(answer, simulation_result)
            

print(answer)