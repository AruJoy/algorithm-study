from sys import stdin
input = stdin.readline

def main():
    n = int(input().strip())
    arr = list(map(int, input().split()))

    i, j = 0, n - 1
    best_sum = abs(arr[i] + arr[j])
    a, b = arr[i], arr[j]

    while i < j:
        cur_sum = arr[i] + arr[j]
        if abs(cur_sum) < best_sum:
            best_sum = abs(cur_sum)
            a, b = arr[i], arr[j]

        if cur_sum > 0:
            j -= 1

        elif cur_sum < 0:
            i += 1
        else:
            break

    print(a, b)

if __name__ == "__main__":
    main()
