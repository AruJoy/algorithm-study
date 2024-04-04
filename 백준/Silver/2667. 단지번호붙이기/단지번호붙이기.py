from sys import stdin
from collections import deque
from heapq import heappop, heappush
columns = int(stdin.readline())
room = list()
for column in range(columns):
    room.append(list(map(int, stdin.readline().rstrip())))
    
checked = [[False for i in range(columns)] for i in range(columns)]

housing_complex = list()
number_of_complex = 0
def find_path():
    global number_of_complex
    for column in range(columns):
        for row in range(columns):
            if checked[column][row] == False and room[column][row] == 1:
                checked[column][row] = True
                start_node = [column,row]
                que = deque([start_node])
                number_of_house = 1
                number_of_complex += 1
                while que:
                    current_coordinate = que.popleft()
                    y = current_coordinate[0]
                    x = current_coordinate[1]
                    if 0 < y:
                        if checked[y-1][x] == False and room[y-1][x] == 1:
                            que.append([y-1,x])
                            checked[y-1][x] = True
                            number_of_house += 1
                    if y < columns-1:
                        if checked[y+1][x] == False and room[y+1][x] == 1:
                            que.append([y+1,x])
                            checked[y+1][x] = True
                            number_of_house += 1
                    if 0 < x:
                        if checked[y][x-1] == False and room[y][x-1] == 1:
                            que.append([y,x-1])
                            checked[y][x-1] = True
                            number_of_house += 1
                    if x < columns-1:
                        if checked[y][x+1] == False and room[y][x+1] == 1:
                            que.append([y,x+1])
                            checked[y][x+1] = True
                            number_of_house += 1
                heappush(housing_complex, number_of_house)

find_path()
print(number_of_complex)
for i in range(len(housing_complex)):
    print(heappop(housing_complex))