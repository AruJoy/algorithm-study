from sys import stdin
input = stdin.readline
from collections import deque

def simulate(rows, columns, field, key_set, start_point):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    ans = 0
    visited_list = [[False for _ in range(columns)]for __ in range(rows)]
    closed_door = list()
    que = deque()
    for s_y, s_x in start_point:
        s_string = field[s_y][s_x] 
        if s_string == "$":
            ans += 1
            visited_list[s_y][s_x] = True
            que.append((s_y, s_x))
        elif s_string != ".":
            if str.lower(s_string) != s_string:
                if not str.lower(s_string) in key_set:
                    closed_door.append((s_string, s_y, s_x))
                    continue
                visited_list[s_y][s_x] = True
                que.append((s_y, s_x))
            else:
                key_set.add(s_string)
                visited_list[s_y][s_x] = True
                que.append((s_y, s_x))
                continue
        que.append((s_y, s_x))
        visited_list[s_y][s_x] = True
    while que:
        while que:
            cur_y, cur_x = que.popleft()
            for i in range(4):
                y, x = cur_y + dy[i], cur_x + dx[i]
                if not(0 <= y <rows and 0 <= x <columns):
                    continue
                if field[y][x] == "*" or visited_list[y][x]:
                    continue
                if field[y][x] == "$":
                    ans += 1
                    visited_list[y][x] = True
                    que.append((y, x))
                    continue
                if not field[y][x] == ".":
                    if str.lower(field[y][x]) == field[y][x]:
                        key_set.add(field[y][x])
                        visited_list[y][x] = True
                        que.append((y, x))
                        continue
                    if str.lower(field[y][x]) in key_set:
                        visited_list[y][x] = True
                        que.append((y, x))
                        continue
                    closed_door.append((field[y][x], y, x))
                    continue
                visited_list[y][x] = True
                que.append((y, x))
                continue
        pop_indexes = list()
        for i in range(len(closed_door)):
            string, y, x = closed_door[i]
            if str.lower(string) in key_set:
                que.append((y, x))
                visited_list[y][x] = True
                pop_indexes.append(i)
        while pop_indexes:
            closed_door.pop(pop_indexes.pop())
    return ans

def main():
    n_test = int(input().strip())
    for _ in range(n_test):
        rows, columns = map(int, input().split())

        field = list()

        for i in range(rows):
            field.append(list(input().strip()))
        
        key_set = set(input().strip())
        start_point = set()
        for i in range(rows):
            if field[i][0] != "*":
                start_point.add((i, 0))
            if field[i][columns-1] != "*":
                start_point.add((i, columns-1))
        for j in range(columns):
            if field[0][j] !="*":
                start_point.add((0, j))
            if field[rows-1][j] != "*":
                start_point.add((rows-1, j))
        
        print(simulate(rows, columns, field, key_set, start_point))
    return

if __name__ == "__main__":
    main()