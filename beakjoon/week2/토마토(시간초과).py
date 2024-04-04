from sys import stdin
from collections import deque
from heapq import heappop, heappush
# dx = [0,0,-1,0,1,0]
# dy = [0,0,0,-1,0,1]
# dz = [1,-1,0,0,0,0]

# x,y,z = 1,1,1
# for i in range(6):
#     nx = x + dx[i]
#     ny = y + dy[i]
#     nz = z + dz[i]
#     print(nx, ny ,nz)

def find_min_ripe_year(unripe_apple):
    ripe_apple_list = list()
    for x in range(rows):
        for y in range(columns):
            for z in range(height):
                if apple_case[z][y][x] == 0:
                    if 0 < z:
                        if is_make_ripe[z-1][y][x] == True:
                            apple_case[z][y][x] = 1
                            ripe_apple_list.append([z, y, x])
                            unripe_apple-=1
                            continue
                    if z < height - 1:
                        if is_make_ripe[z+1][y][x] == True:
                            apple_case[z][y][x] = 1
                            ripe_apple_list.append([z, y, x])
                            unripe_apple-=1
                            continue
                    if 0 < y:
                        if is_make_ripe[z][y-1][x] == True:
                            apple_case[z][y][x] = 1
                            ripe_apple_list.append([z, y, x])
                            unripe_apple-=1
                            continue
                    if y < columns - 1:
                        if is_make_ripe[z][y+1][x] == True:
                            apple_case[z][y][x] = 1
                            ripe_apple_list.append([z, y, x])
                            unripe_apple-=1
                            continue
                    if 0 < x:
                        if is_make_ripe[z][y][x-1] == True:
                            apple_case[z][y][x] = 1
                            ripe_apple_list.append([z, y, x])
                            unripe_apple-=1
                            continue
                    if x < rows - 1:
                        if is_make_ripe[z][y][x+1] == True:
                            apple_case[z][y][x] = 1
                            ripe_apple_list.append([z, y, x])
                            unripe_apple-=1
                            continue
    for z,y,x in ripe_apple_list:
        is_make_ripe[z][y][x] = True
    return unripe_apple
rows, columns, height = map(int, stdin.readline().split())
is_make_ripe = [[[False for i in range(rows)] for i in range(columns)]for i in range(height)]
apple_case = list()
unripe_apple = 0
for B in range(height):
    apple_board = list()
    for L in range(columns):
        line = list(map(int, stdin.readline().split(' ')))
        for P in range(len(line)):
            if line[P] == 1:
                is_make_ripe[B][L][P] = True
            elif line[P] == 0:
                unripe_apple += 1
        apple_board.append(line)
    apple_case.append(apple_board)
    
before_unripe_apple = unripe_apple
year = 0
while True:
    unripe_apple = find_min_ripe_year(unripe_apple)
    year += 1
    if before_unripe_apple == unripe_apple:
        print(-1)
        break
    if unripe_apple > 0:
        before_unripe_apple = unripe_apple
        continue
    print(year)
    break