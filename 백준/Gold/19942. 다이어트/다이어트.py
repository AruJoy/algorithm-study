from sys import stdin
INF = 10 ** 9
input = stdin.readline
def diet(count, f_list, dp, min_val, cur_val, mask, end):
    a, b, c, d = cur_val
    min_a, min_b, min_c, min_d = min_val
    bit = 0
    if dp[0][mask] != -1:
        return dp[0][mask], dp[1][mask]
    
    if (min_a <= a and min_b <= b and min_c <= c and min_d <= d):
        return 0, mask
    
    if mask == end:
        return INF, mask
    min_cost = INF
    
    for i in range(count):
        if 1 << i & mask: continue
        a1, b1, c1, d1, price = f_list[i]
        cost, comb = diet(count, f_list, dp, min_val,
                    (a + a1, b + b1, c + c1, d + d1), mask | 1<<i, end)
        total_cost = price + cost
        if min_cost > total_cost:
            bit = comb | (1 << i)
            min_cost = total_cost
    dp[0][mask] = min_cost
    dp[1][mask] = bit
    return min_cost, bit
def main():
    count = int(input().strip())
    f_list = []
    min_a, min_b, min_c, min_d = map(int, input().split())
    for i in range(count):
        a, b, c, d, price = map(int, input().split())
        f_list.append((a, b, c, d, price))
    dp = [[-1 for _ in range(1<<count)],[-1 for _ in range(1<<count)]]
    min_cost, bit = diet(count, f_list, dp, (min_a, min_b, min_c, min_d), (0, 0, 0, 0), 0, 1<<(count) -1)
    if min_cost == INF:
        print(-1)
        return
    answer_list = []
    k = 1
    f = 1
    for _ in range(count):
        if bit & k :
            answer_list.append(f)
        k = k << 1
        f += 1
    print(min_cost)
    print(*answer_list)
    return
if __name__ == "__main__":
    main()