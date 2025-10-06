from sys import stdin
input = stdin.readline
from collections import deque
import sys
sys.setrecursionlimit(1003)

INF = float("inf")

def main():
    n_sensor = int(input().strip())
    n_router = int(input().strip())
    sensor_list = list(map(int, input().split()))

    sensor_list.sort()
    sensor_diff = list()
    sensor_diff.append(0)
    total_sum = 0
    for i in range(1, n_sensor):
        cur_range = sensor_list[i] - sensor_list[i-1]
        total_sum += cur_range
        sensor_diff.append(cur_range)
    sensor_diff.sort()
    for _ in range(min(n_router - 1, len(sensor_diff))):
        total_sum -= sensor_diff.pop()
    print(total_sum)
    return
if __name__ == "__main__":
    main()