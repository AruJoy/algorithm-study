from sys import stdin
input = stdin.readline
from collections import deque
def roll(dice_position, direction):
    new_position = [i for i in dice_position]
    if direction == 0:
        new_position[2] = dice_position[0]
        new_position[1] = dice_position[2]
        new_position[3] = dice_position[1]
        new_position[0] = dice_position[3]
    if direction == 1:
        new_position[3] = dice_position[0]
        new_position[1] = dice_position[3]
        new_position[2] = dice_position[1]
        new_position[0] = dice_position[2]
    if direction == 2:
        new_position[5] = dice_position[0]
        new_position[1] = dice_position[5]
        new_position[4] = dice_position[1]
        new_position[0] = dice_position[4]
    if direction == 3:
        new_position[4] = dice_position[0]
        new_position[1] = dice_position[4]
        new_position[5] = dice_position[1]
        new_position[0] = dice_position[5]
    return new_position
def roll_dice(dice, i, j):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    count = 1
    dice_map = [False for _ in range(6)]
    dice_position = [i for i in range(6)]
    # 상 하 좌 우 앞 뒤
    que = deque()
    dice_map[dice_position[1]] = True
    que.append((i,j, dice_position))
    while que:
        current_y, current_x, current_p = que.popleft()
        for i in range(4):
            y = current_y + dy[i]
            x = current_x + dx[i]
            if (y < 0 or 5 < y
                or x < 0 or 5 < x):
                continue
            if dice[y][x] == 1:
                new_position = roll(current_p, i)
                if dice_map[new_position[1]]:
                    continue
                dice_map[new_position[1]] = True
                que.append((y, x, new_position))
                count += 1
    return count == 6
    
def judge():
    dice = []
    for _ in range(6):
        dice.append(list(map(int, input().split())))
    for i in range(6):
        for j in range(6):
            if dice[i][j] == 1:
                if roll_dice(dice, i, j):
                    print("yes")
                    return
                print("no")
                return
    return
def main():
    for _ in range(3):
        judge()
    return
if __name__ == "__main__":
    main()
