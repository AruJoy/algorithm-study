from sys import stdin
input = stdin.readline

def get_input():
    rows, columns = map(int, input().split(" "))
    office_map = []
    blind_map = []
    cctv_spots = []
    cctv_counts = 0
    for i in range(rows):
        new_row = list(map(int, input().split(" ")))
        new_blind_row = []
        for j in range(columns):
            if new_row[j] == 6:
                new_blind_row.append(-1)
                continue
            if new_row[j] != 0:
                cctv_spots.append([[i,j], new_row[j]])
                cctv_counts += 1
            new_blind_row.append(0)
        office_map.append(new_row)
        blind_map.append(new_blind_row)
    return rows, columns, blind_map, cctv_spots, cctv_counts

def cctv_1(blind_spot_map: list, direction: int, coordinate: list):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    y, x = coordinate
    
    while (0 <= x
        and x <= columns - 1
        and 0 <= y
        and y <= rows -1):
        if blind_spot_map[y][x] == -1:
            break
        blind_spot_map[y][x] = 1
        x += dx[direction]
        y += dy[direction]
    return
def cctv_2(blind_spot_map: list, direction: int, coordinate: list):
    dx = [1, -1]
    dy = [1, -1]
    
    if direction % 2 == 0:
        for i in range(2):
            y, x = coordinate            
            while( 0 <= x
            and x <= columns - 1):
                if blind_spot_map[y][x] == -1:
                    break
                blind_spot_map[y][x] = 1
                x += dx[i]
        return
    for i in range(2):
        y, x = coordinate        
        while( 0 <= y
        and y <= rows - 1):
            if blind_spot_map[y][x] == -1:
                break
            blind_spot_map[y][x] = 1
            y += dy[i]
    return
def cctv_3(blind_spot_map: list, direction: int, coordinate: list):
    dx = [1, -1, -1, 1]
    dy = [1, 1, -1, -1]
    
    y, x = coordinate
    while (0 <= x
        and x <= columns - 1):
        if blind_spot_map[y][x] == -1:
            break
        blind_spot_map[y][x] = 1
        x += dx[direction]
    y, x = coordinate
    while (0 <= y
        and y <= rows -1):
        if blind_spot_map[y][x] == -1:
            break
        blind_spot_map[y][x] = 1
        y += dy[direction]
    return
def cctv_4(blind_spot_map: list, direction: int, coordinate: list):
    dx = [[1, -1] ,[1, -1], [1], [-1]]
    dy = [[1], [-1], [1, -1], [1, -1]]
    
    for i in range(len(dx[direction])):
        y, x = coordinate        
        while (0 <= x
            and x <= columns - 1):
            if blind_spot_map[y][x] == -1:
                break
            blind_spot_map[y][x] = 1
            x += dx[direction][i]
    for i in range(len(dy[direction])):
        y, x = coordinate        
        while (0 <= y
            and y <= rows - 1):
            if blind_spot_map[y][x] == -1:
                break
            blind_spot_map[y][x] = 1
            y += dy[direction][i]
    return

def put_cctv(blind_spot_map: list, cctv_spots: list, current_cctv: int):
    if current_cctv == cctv_counts:
        answer = 0
        for i in range(rows):
            for j in range(columns):
                if blind_spot_map[i][j] == 0 :
                    answer += 1
        return answer
    answer = 64
    coordinate, cctv_type = cctv_spots[current_cctv]
    if cctv_type == 1:
        for i in range(4):
            new_blind_spot_map = [row[:] for row in blind_spot_map]
            cctv_1(new_blind_spot_map, i, coordinate)
            answer = min(put_cctv(new_blind_spot_map, cctv_spots, current_cctv+1), answer)
    if cctv_type == 2:
        for i in range(2):
            new_blind_spot_map = [row[:] for row in blind_spot_map]
            cctv_2(new_blind_spot_map, i, coordinate)
            answer = min(put_cctv(new_blind_spot_map, cctv_spots, current_cctv+1), answer)
    if cctv_type == 3:
        for i in range(4):
            new_blind_spot_map = [row[:] for row in blind_spot_map]
            cctv_3(new_blind_spot_map, i, coordinate)
            answer = min(put_cctv(new_blind_spot_map, cctv_spots, current_cctv+1), answer)
    if cctv_type == 4:
        for i in range(4):
            new_blind_spot_map = [row[:] for row in blind_spot_map]
            cctv_4(new_blind_spot_map, i, coordinate)
            answer = min(put_cctv(new_blind_spot_map, cctv_spots, current_cctv+1), answer)
    if cctv_type == 5 :
        answer = min(put_cctv(blind_spot_map, cctv_spots, current_cctv+1), answer)
    return answer

def cctv_5(blind_spot_map: list, coordinate: list):
    dx = [1, -1]
    dy = [1, -1]
    
    for i in range(2):
        y, x = coordinate
        while( 0 <= x
        and x <= columns - 1):
            if blind_spot_map[y][x] == -1:
                break
            blind_spot_map[y][x] = 1
            x += dx[i]
    for i in range(2):
        y, x = coordinate
        while( 0 <= y
        and y <= rows - 1):
            if blind_spot_map[y][x] == -1:
                break
            blind_spot_map[y][x] = 1
            y += dy[i]
    return
def get_answer(blind_spot_map: list, cctv_spots: list):
    answer = 64
    for i in range(cctv_counts):
        if cctv_spots[i][1] == 5:
            cctv_5(blind_spot_map, cctv_spots[i][0])
    new_answer = put_cctv(blind_spot_map, cctv_spots, 0)
    answer = min(answer, new_answer)
    return answer

rows, columns, blind_map, cctv_spots, cctv_counts = get_input()

print(get_answer(blind_map, cctv_spots))