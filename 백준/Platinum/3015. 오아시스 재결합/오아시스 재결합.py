from sys import stdin
input = stdin.readline
def main():
    n_person = int(input().strip())
    stack = list()
    ans = 0
    for _ in range(n_person):
        person = int(input().strip())
        cur_person = person
        cur_count = 1
        while stack and stack[-1][0] <= person:
            cur_person, cur_count = stack.pop()
            ans += cur_count
            if cur_person == person:
                cur_count += 1
        if stack:
            ans += 1
        if cur_person != person:
            cur_count = 1
        stack.append((person, cur_count))
    print(ans)
    return

if __name__ == "__main__":
    main()