from sys import stdin
input = stdin.readline
INF = float("inf")

def move_pipe(scale, room):
    require_empty = [[(0, 1)], [(1, 0)], [(1, 0), (0, 1), (1, 1)]]
    dx = [1, 0, 1]
    dy = [0, 1, 1]
    dp = [[[0, 0, 0] for _ in range(scale)] for __ in range(scale)]
    directions = [(True, False, True), (False, True, True), (True, True, True)]
    dp[0][1][0] = 1
    for cur_y in range(scale):
        for cur_x in range(scale):
            for direction in range(3):
                if dp[cur_y][cur_x][direction] == 0:
                    continue
                for i in range(3):
                    if not directions[direction][i]:
                        continue
                    y, x = cur_y + dy[i], cur_x + dx[i]
                    if not(0 <= x < scale and 0 <= y < scale):
                        continue
                    blocked = False
                    for d_y, d_x in require_empty[i]:
                        if room[cur_y + d_y][cur_x + d_x] == 1:
                            blocked = True
                            break
                    if blocked: continue
                    dp[y][x][i] += dp[cur_y][cur_x][direction]
    return sum(dp[scale-1][scale-1])

def main():
    scale = int(input().strip())
    room = list()
    for _ in range(scale):
        room.append(list(map(int, input().split())))
    print(move_pipe(scale, room))
    return

if __name__ == "__main__":
    main()