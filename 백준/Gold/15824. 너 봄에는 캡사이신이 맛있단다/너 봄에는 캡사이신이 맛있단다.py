from sys import stdin
input = stdin.readline
MOD = 1000000007
def main():
    n = int(input().strip())
    num_list = list(map(int, input().split()))
    num_list.sort()
    ans = 0
    pow_list = [1 for _ in range(n)]
    for i in range(1,n):
        pow_list[i] = (pow_list[i-1]*2)% MOD
    for i in range(n-1, -1, -1):
        ans += num_list[i] * (((pow_list[i]-1) - pow_list[-i-1]+1))
        ans = ans % MOD
    print(ans)
    return

if __name__ == "__main__":
    main()
