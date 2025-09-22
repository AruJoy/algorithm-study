MOD = 1000000007

def k_c_n(k, n):
    c1 = 1
    n1 = min(k-n, n)
    for i in range(n1):
        c1 = c1 * (k - i) % MOD
        c1 = c1 * pow(i+1, MOD-2, MOD) % MOD
    return c1

def main():
    k, n = map(int, input().split())
    print(k_c_n(k, n))

if __name__ == "__main__":
    main()
