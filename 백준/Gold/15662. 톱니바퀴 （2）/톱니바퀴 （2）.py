from sys import stdin
input = stdin.readline
from collections import deque
def rotate(gear, d):
    if d<0:
        k = gear.popleft()
        gear.append(k)
        return
    k = gear.pop()
    gear.appendleft(k)
    return
def rotate_gear(gear_count, gear_index, gear_list, d):
    r = gear_list[gear_index][2]
    l = gear_list[gear_index][6]
    rotate(gear_list[gear_index], d)
    for i in range(gear_index+1,gear_count):
        if r != gear_list[i][6]:
            r = gear_list[i][2]
            if (i - gear_index) % 2 == 1:
                rotate(gear_list[i], -d)
                continue
            rotate(gear_list[i], d)
            continue
        break
    for i in range(gear_index):
        if l != gear_list[gear_index-i-1][2]:
            l = gear_list[gear_index-i-1][6]
            if i % 2 == 1:
                rotate(gear_list[gear_index-i-1], d)
                continue
            rotate(gear_list[gear_index-i-1], -d)
            continue
        break
    return
def main():
    gear_count = int(input().strip())
    gear_list = []
    for i in range(gear_count):
        gear = deque(map(int, input().strip()))
        gear_list.append(gear)
    c_count = int(input().strip())
    for i in range(c_count):
        gear_index, d = map(int, input().split())
        rotate_gear(gear_count, gear_index -1, gear_list, d)
    answer = 0
    for i in range(gear_count):
        answer += gear_list[i][0]
    print(answer)
    return

if __name__ == "__main__":
    main()