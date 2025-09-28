from sys import stdin
input = stdin.readline
from collections import deque

def get_n(n, p, q, dp):
    if n == 0: return 1
    
    p1 = n // p
    ans1 = -1
    if p1 in dp:
        ans1 = dp[p1]
    else:
        ans1 = get_n(p1, p, q, dp)
        dp[p1] = ans1
    
    q1 = n // q
    ans2 = -1
    if q1 in dp:
        ans2 = dp[q1]
    else:
        ans2 = get_n(q1, p, q, dp)
        dp[q1] = ans2
    return ans1 + ans2
    
def main():
    n, p, q = map(int, input().split())
    dp = dict()
    dp[0] = 1
    print(get_n(n, p, q, dp))
    return
if __name__ == "__main__":
    main()