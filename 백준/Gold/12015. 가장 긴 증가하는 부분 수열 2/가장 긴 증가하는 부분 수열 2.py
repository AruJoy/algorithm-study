from sys import stdin
input = stdin.readline

def find_length(sequence):
    longest = [sequence[0]]
    for i in range(1,len(sequence)):
        cur = sequence[i]
        if longest[-1] < cur:
            longest.append(cur)
            continue
        lo = 0
        hi = len(longest) - 1
        ans = 0
        while lo <= hi:
            mid = (lo + hi)//2
            if longest[mid] == cur:
                ans = mid
                break
            if longest[mid] > cur:
                hi = mid - 1
                ans = mid
                continue
            lo = mid + 1
        longest[ans] = cur
    return len(longest)

def main():
    length = int(input().strip())
    sequence = list(map(int, input().split()))
    print(find_length(sequence))
    return

if __name__ == "__main__":
    main()
