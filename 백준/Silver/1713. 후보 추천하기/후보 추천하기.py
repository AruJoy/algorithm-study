from sys import stdin
input = stdin.readline
MOD = 1000000007
def main():
    n = int(input().strip())
    p = int(input().strip())
    p_list = list(map(int, input().split()))
    n_list = list()
    for i in range(p):
        add = False
        for j in range(len(n_list)):
            number = n_list[j][2]
            if number == p_list[i]:
                n_list[j][0] += 1
                add = True
                break
        n_list.sort(reverse=True)
        if not add:
            if len(n_list) >= n:
                n_list.pop()
            n_list.append([1, i, p_list[i]])
    answer = [row[2] for row in n_list]
    answer.sort()
    print(*answer)
    return

if __name__ == "__main__":
    main()