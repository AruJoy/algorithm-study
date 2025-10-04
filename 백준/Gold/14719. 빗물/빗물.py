from sys import stdin
input = stdin.readline
from collections import deque
def main():
    rows, columns = map(int, input().split())
    rain_container = list(map(int, input().split()))
    if columns < 3: 
        print(0)
        return
    ans = 0
    part_ans = 0
    left_high = 0
    left_index = 0
    for i in range(columns-1):
        if left_high <= rain_container[i]:
            left_high = rain_container[i]
            ans += part_ans
            part_ans = 0
            left_index = i
            continue
        part_ans += left_high - rain_container[i]
    right_high = 0
    right_index = columns-1
    part_ans = 0
    for i in range(columns-1, left_index, -1):
        if right_high <= rain_container[i]:
            right_high = rain_container[i]
            ans += part_ans
            part_ans = 0
            right_index = i
            continue
        part_ans += right_high - rain_container[i]
    if rain_container[left_index] < rain_container[right_index]:
        part_ans -= (rain_container[right_index] - rain_container[left_index]) * (right_index - 1 - left_index)
    ans += part_ans
    print(ans)
    return
if __name__ == "__main__":
    main()