from sys import stdin
input = stdin.readline
MOD = 1000000007
def main():
    n = int(input().strip())
    num_list = list(map(int, input().split()))
    num_list.sort()
    ans = 0
    for i in range(n-1, -1, -1):
        if i != 0:
            ans += ((2**i)-1)*num_list[i]
        if i+1 != n:
            ans -= ((2**(n-i-1))-1)*num_list[i]
        ans = ans % MOD
    print(ans)
    return

if __name__ == "__main__":
    main()
