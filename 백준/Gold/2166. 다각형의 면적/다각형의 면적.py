from sys import stdin
input = stdin.readline
INF = float('INF')
import math
z_point = 10^5

def main():
    n_dot = int(input().strip())
    a,b = map(int, input().split())
    s_a, s_b = a, b
    sum_1, sum_2 = 0, 0
    for _ in range(n_dot-1):
        cur_a, cur_b = map(int, input().split())
        sum_1 += (s_a - cur_a) * (s_b - b)
        sum_2 += (s_b - cur_b) * (s_a - a)
        a, b = cur_a, cur_b
    # sum_1 += a * s_b
    # sum_2 += b * s_a
    ans = abs(sum_1-sum_2)/2
    print(round(ans+0.0000000001, 1))

    return

if __name__ == "__main__":
    main()
