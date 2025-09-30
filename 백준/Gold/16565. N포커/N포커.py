from sys import stdin
input = stdin.readline
MOD = 10007

def comb_mod(n, r):
    if r < 0 or r > n:
        return 0
    num = 1
    den = 1
    for i in range(r):
        num = (num*(n-i))%MOD
        den = (den*(i+1))%MOD
    return (num * pow(den, MOD-2, MOD))% MOD

def main():
    n = int(input().strip())
    ans = 0
    
    for i in range(1, 14):
        if n < 4 * i: break
        
        cur = (comb_mod(13, i) * comb_mod(52-4*i, n-4*i)) % MOD
        if i % 2 == 1:
            ans = (ans + cur) % MOD
            continue
        ans = (ans - cur) % MOD
    print(ans)
    return

if __name__ == "__main__":
    main()
