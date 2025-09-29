from sys import stdin
input = stdin.readline
INF = float('INF')

def get_prime(number):
    table = [True for _ in range(number+1)]
    prime_list = []
    for i in range(2, number+1):
        if not table[i]:continue
        prime_list.append(i)
        cur = i
        while cur <= number:
            table[cur] = False
            cur += i
    
    return prime_list

def get_count(prime_list, number):
    length = len(prime_list)
    sum_list = [0]
    for i in range(length):
        sum_list.append(sum_list[i] + prime_list[i])
    ans = 0
    i, j = 0, 1
    while i < j and j <= length:
        cur = sum_list[j] - sum_list[i]
        if cur == number:
            ans += 1
            j += 1
            continue
        if cur < number:
            j += 1
            continue
        if cur > number:
            i += 1
    return ans
def main():
    number = int(input().strip())
    prime_list = get_prime(number)
    print(get_count(prime_list, number))
    return

if __name__ == "__main__":
    main()
