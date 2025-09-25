from sys import stdin
input = stdin.readline
from collections import deque

def get_input():
    scale = int(input())
    ward_map = []
    total_people = 0
    for _ in range(scale):
        row = list(map(int, input().split(" ")))
        ward_map.append(row)
        total_people += sum(row)
    return scale, ward_map, total_people

def count_sector_1(ward_map:list, start_y:int, start_x:int, d1:int, d2:int):
    people = 0
    for y in range(start_y + d1):
        for x in range(min(start_x + 1, start_x - ((y - start_y)))):
            people+=ward_map[y][x]
    return people

def count_sector_2(ward_map:list, start_y:int, start_x:int, d1:int, d2:int):
    people = 0
    for y in range(start_y+d2+1):
        for x in range(max(start_x+1, start_x + 1 +((y - start_y))), scale):
            people+=ward_map[y][x]
    return people

def count_sector_3(ward_map:list, start_y:int, start_x:int, d1:int, d2:int):
    people = 0
    for y in range(start_y+d1, scale):
        for x in range(min(start_x - d1 + d2, start_x - d1 + d2 - ((start_y + d1 + d2) - y))):
            people+=ward_map[y][x]
    return people

def count_sector_4(ward_map:list, start_y:int, start_x:int, d1:int, d2:int):
    people = 0
    for y in range(start_y + d2 + 1, scale):
        for x in range(max(start_x - d1 + d2, start_x - d1 + d2 + ((start_y + d1 + d2) - y)+1), scale):
            people+=ward_map[y][x]
    return people

def simulate_separation(scale: int, ward_map:list, total_people:int):
    answer = float("inf")
    for y in range (scale-2):
        for x in range(1, scale-1):
            for d1 in range(1,min(x+1, scale - y)):
                for d2 in range(1,min(scale - x, scale - y - d1)):
                    sector_5 = total_people
                    min_people = float("inf")
                    max_people = 0
                    
                    sector = count_sector_1(ward_map, y, x, d1, d2)
                    sector_5 -= sector
                    min_people = min(min_people, sector)
                    max_people = max(max_people, sector)
                    
                    sector = count_sector_2(ward_map, y, x, d1, d2)
                    sector_5 -= sector
                    min_people = min(min_people, sector)
                    max_people = max(max_people, sector)
                    
                    sector = count_sector_3(ward_map, y, x, d1, d2)
                    sector_5 -= sector
                    min_people = min(min_people, sector)
                    max_people = max(max_people, sector)
                    
                    sector = count_sector_4(ward_map, y, x, d1, d2)
                    sector_5 -= sector
                    min_people = min(min_people, sector)
                    max_people = max(max_people, sector)
                    
                    min_people = min(min_people, sector_5)
                    max_people = max(max_people, sector_5)
                    
                    answer = min(answer, max_people - min_people)

    return answer

scale, ward_map, total_people = get_input()
print(simulate_separation(scale, ward_map, total_people))