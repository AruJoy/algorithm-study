from sys import stdin
input = stdin.readline
from collections import deque

def get_coordinate_tuple(info :str):
    if int(info) == 0:
        return [-1, -1, -1]
    return [-2, -2, -2]
def get_input():
    scale, passengers, fuel = map(int, input().split(" "))
    taxi_map = []
    for _ in range(scale):
        row = list(map(get_coordinate_tuple, input().split(" ")))
        taxi_map.append(row)
    taxi_y, taxi_x = map(int, input().split(" "))
    for i in range(passengers):
        passenger_y, passenger_x, destination_y, destination_x = map(int, input().split(" "))
        taxi_map[passenger_y-1][passenger_x-1][0] = i
        taxi_map[passenger_y-1][passenger_x-1][1] = destination_y - 1
        taxi_map[passenger_y-1][passenger_x-1][2] = destination_x - 1
    return scale, passengers, fuel, taxi_map, taxi_y-1, taxi_x-1

def get_destination(scale:int, taxi_map:list, destination_y:int,
                            destination_x:int, taxi_y:int, taxi_x:int):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    if taxi_y == destination_y and taxi_x == destination_x:
        return 0
    visited_map = [[False for _ in range(scale)] for __ in range(scale)]
    distance = 0
    que = deque()
    que.append((taxi_y, taxi_x, 0))
    visited_map[taxi_y][taxi_x] = True
    while que:
        now_y, now_x, distance = que.popleft()
        for i in range(4):
            y = now_y + dy[i]
            x = now_x + dx[i]
            if (y < 0 or scale-1 < y
                or x < 0 or scale-1 < x
                or taxi_map[y][x][0] == -2
                or visited_map[y][x]):
                continue
            if y == destination_y and x == destination_x:
                return distance + 1
            visited_map[y][x] = True
            que.append((y, x, distance + 1))
    return -1

def get_shortest_passenger(scale:int, taxi_map:list, taxi_y:int, taxi_x:int):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited_map = [[False for _ in range(scale)] for __ in range(scale)]
    passenger_column = float("INF")
    passenger_row = float("INF")
    destination_y = -1
    destination_x = -1
    now_y = -1
    now_x = -1
    distance = float("INF")
    now_distance = -1
    visited_map[taxi_y][taxi_x] = True
    if taxi_map[taxi_y][taxi_x][0] >= 0:
        taxi_map[taxi_y][taxi_x][0] = -1
        return 0, taxi_y, taxi_x, taxi_map[taxi_y][taxi_x][1], taxi_map[taxi_y][taxi_x][2]
    que = deque()
    que.append((taxi_y, taxi_x, 0))
    
    while que:
        current_y, current_x, now_distance = que.popleft()
        if now_distance >= distance:
            break
        for i in range(4):
            y = current_y + dy[i]
            x = current_x + dx[i]
            if (y < 0 or scale-1 < y
                or x < 0 or scale-1 < x
                or taxi_map[y][x][0] == -2
                or visited_map[y][x]):
                continue
            if taxi_map[y][x][0] >= 0:
                if y > passenger_row:
                    visited_map[y][x] = True
                    continue
                if y == passenger_row and x > passenger_column:
                    visited_map[y][x] = True
                    continue
                passenger_row = y
                passenger_column = x
                destination_y = taxi_map[y][x][1]
                destination_x = taxi_map[y][x][2]
                now_y = y
                now_x = x
                distance = now_distance + 1
                visited_map[y][x] = True
                continue
            visited_map[y][x] = True
            que.append((y, x, now_distance + 1))
    taxi_map[now_y][now_x][0] = -1
    return distance, now_y, now_x, destination_y, destination_x

def get_answer(scale: int, passengers: int, fuel: int, taxi_map:list, taxi_y:int, taxi_x:int):
    remain_fuel = fuel
    now_y = taxi_y
    now_x = taxi_x
    for i in range(passengers):
        distance, now_y, now_x, destination_y, destination_x = get_shortest_passenger(scale, taxi_map, now_y, now_x)
        if remain_fuel < distance or distance < 0:
            return -1
        remain_fuel -= distance
        distance_to_destination =  get_destination(scale, taxi_map, destination_y, destination_x, now_y, now_x)
        if distance_to_destination < 0 or remain_fuel < distance_to_destination:
            return -1
        remain_fuel += distance_to_destination
        now_y = destination_y
        now_x = destination_x
    return remain_fuel
scale, passengers, fuel, taxi_map, taxi_y, taxi_x = get_input()
print(get_answer(scale, passengers, fuel, taxi_map, taxi_y, taxi_x))