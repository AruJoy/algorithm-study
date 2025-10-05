from sys import stdin
input = stdin.readline
from collections import deque
INF = float("inf")

def simulate(lab, visited_list, n_empty, scale, cur_virus, min_answer):
    for i in range(scale):
        for j in range(scale):
            visited_list[i][j] = False
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    que = deque()
    cur_time = 0
    cur_empty = n_empty
    for y, x in cur_virus:
        visited_list[y][x] = True
        que.append((y, x, 0))
        cur_empty -= 1
    contamination = set()
    while que and cur_empty != 0:
        while que:
            if que[0][2] != cur_time:
                break
            cur_y, cur_x, cur_t = que.popleft()
            for i in range(4):
                y, x = cur_y + dy[i], cur_x + dx[i]
                if (0 <= y < scale and 0 <= x < scale
                    and lab[y][x] == 0
                    and not visited_list[y][x]
                    and not (y,x) in contamination):
                    contamination.add((y, x))
                    que.append((y, x, cur_t+1))
        cur_time += 1
        if cur_time >= min_answer[0] :
            return INF
        for y, x in contamination:
            visited_list[y][x] = True
            cur_empty -= 1
        if cur_empty == 0:
            return cur_time
        contamination.clear()
    return INF
def place_virus(lab, visited_list, place_point, n_empty,
                scale, n_virus, cur_virus, index, min_answer):
    answer = INF
    
    if len(cur_virus) == n_virus:
        return simulate(lab, visited_list, n_empty, scale, cur_virus, min_answer)
    
    for i in range(index, len(place_point)):
        if len(place_point) - i < n_virus - len(cur_virus):
            break
        
        cur_virus.append(place_point[i])
        answer = min(answer, place_virus(lab, visited_list, place_point,
                                n_empty, scale, n_virus, cur_virus, i+1, min_answer))
        min_answer[0] = min(min_answer[0], answer)
        cur_virus.pop()
    
    return answer

def main():
    scale, n_virus = map(int, input().split())
    lab = list()
    place_point = list()
    n_empty = 0
    for i in range(scale):
        row = list(map(int, input().split()))
        for j in range(scale):
            if row[j] == 2:
                place_point.append((i, j))
                row[j] = 0
                n_empty += 1
                continue
            if row[j] == 0:
                n_empty += 1
                continue
        lab.append(row)
    if n_empty == 0 or n_empty == n_virus:
        print(0)
        return
    visited_list = [[False for _ in range(scale)] for __ in range(scale)]
    min_answer = [INF]
    answer = place_virus(lab, visited_list, place_point, n_empty, scale, n_virus, list(), 0, min_answer)
    print(-1 if answer == INF else answer)
    return
if __name__ == "__main__":
    main()