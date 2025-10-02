from sys import stdin
input = stdin.readline
MOD = 1000000007
from collections import deque
def is_adjacent(mask):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    coord_set = set()
    bit = 1
    for i in range(25):
        if mask & bit:
            y, x = i // 5, i % 5
            coord_set.add((y,x))
        bit = bit << 1
    que = deque()
    que.append(coord_set.pop())
    while que:
        cur_y, cur_x = que.popleft()
        for i in range(4):
            y, x = cur_y + dy[i], cur_x + dx[i]
            if(0 <= y < 5 and 0 <= x < 5
                and (y,x) in coord_set):
                coord_set.remove((y,x))
                que.append((y,x))
    return len(coord_set) == 0

def union(class_room, found_list, bit, mask, count, y_count):
    ans = 0
    if count == 7:
        if found_list[mask]:
            return 0
        found_list[mask] = True
        return 1 if is_adjacent(mask) else 0
    for i in range(bit, 25):
        y, x = i//5, i%5
        nxt_count = y_count + (1 if class_room[y][x] == "Y" else 0)
        if nxt_count >= 4:
            continue
        ans += union(class_room, found_list, i+1, mask | 1<<i, count + 1, nxt_count)
    return ans
def main():
    class_room = list()
    ans = 0
    found_list = [False for i in range((1<<25)-1)]
    for _ in range(5):
        class_room.append(list(input().strip()))
    print(union(class_room, found_list, 0, 0, 0, 0))
    return
if __name__ == "__main__":
    main()
    