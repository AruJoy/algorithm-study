from sys import stdin
input = stdin.readline
from collections import deque
INF = float("inf")
def bfs(cube, visited_list, ans):
    if cube[0][0][0] == 0 or cube[4][4][4] == 0:
        return INF
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    for i in range(5):
        for j in range(5):
            for k in range(5):
                visited_list[i][j][k] = False
    visited_list[0][0][0] = True
    que = deque()
    que.append((0, 0, 0, 0))
    while que:
        cur_z, cur_y, cur_x, cur_move = que.popleft()
        if ans[0] <= cur_move:
            return INF
        for i in range(6):
            z, y, x = cur_z + dz[i], cur_y + dy[i], cur_x + dx[i]
            if (z < 0 or 4 < z
                or y < 0 or 4 < y
                or x < 0 or 4 < x
                or visited_list[z][y][x]
                or cube[z][y][x] == 0):
                continue
            if z == 4 and y == 4 and x == 4:
                return cur_move + 1
            visited_list[z][y][x] = True
            que.append((z, y, x, cur_move + 1))
    return INF
def shuffle(order, depth, cube, visited_list, ans):
    if depth == 5:
        new_cube = [cube[i] for i in order]
        ans[0] = min(ans[0], bfs(new_cube, visited_list, ans))
        return

    for i in range(depth, 5):
        order[depth], order[i] = order[i], order[depth]
        shuffle(order, depth + 1, cube, visited_list, ans)
        order[depth], order[i] = order[i], order[depth]
    return
def solution(cube, visited_list):
    cube_cash = [list() for _ in range(5)]
    for i in range(5):
        for j in range(4):
            if j != 0:
                cube[i] = [[cube[i][4-k][l] for k in range(5)] for l in range(5)]
            cube_cash[i].append(cube[i])
    ans = [INF]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        new_cube = [cube_cash[0][i], cube_cash[1][j], cube_cash[2][k], cube_cash[3][l], cube_cash[4][m]]
                        order = [0, 1, 2, 3, 4]
                        shuffle(order, 0, new_cube, visited_list, ans)
    return -1 if ans[0] == INF else ans[0]
def main():
    cube = list()
    for _ in range(5):
        surface = list()
        for __ in range(5):
            surface.append(list(map(int, input().split())))
        cube.append(surface)
    visited_list = [[[False for _ in range(5)]
                    for __ in range(5)]
                    for ___ in range(5)]
    print(solution(cube, visited_list))

    return
if __name__ == "__main__":
    main()