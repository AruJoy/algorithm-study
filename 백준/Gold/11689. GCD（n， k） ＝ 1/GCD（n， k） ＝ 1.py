from sys import stdin
input = stdin.readline
def main():
    number = int(input().strip())
    MAX = int(number**(1/2)) + 1
    c_body = [True for _ in range(MAX)]
    prime_list = list()
    
    for i in range(2, MAX):
        if not c_body[i]:
            continue
        prime_list.append(i)
        multi = i ** 2
        while multi < MAX:
            c_body[multi] = False
            multi += i
    
    ans = 1
    cur_number = number
    for prime in prime_list:
        if cur_number % prime == 0:
            cur_ans = prime-1
            cur_number //= prime
            while cur_number % prime == 0:
                cur_ans *= prime
                cur_number //= prime
            ans *= cur_ans
    if cur_number != 1:
        ans *= (cur_number-1)
    print(ans)
    return

if __name__ == "__main__":
    main()