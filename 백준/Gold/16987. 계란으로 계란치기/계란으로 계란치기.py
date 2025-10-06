from sys import stdin
input = stdin.readline

INF = float("inf")
def break_egg(n_egg, egg_list, left):
    if left == n_egg:
        return 0
    ans = 0
    if egg_list[left][0] < 1:
        return break_egg(n_egg, egg_list, left+1)
    for i in range(n_egg):
        if i == left:
            continue
        if egg_list[i][0] < 1:
            continue
        left_w = egg_list[left][1]
        right_w = egg_list[i][1]
        egg_list[left][0] -= right_w
        egg_list[i][0] -= left_w
        cur_broken = 0
        if egg_list[left][0] < 1:
            cur_broken += 1
        if egg_list[i][0] < 1:
            cur_broken += 1
        ans = max(ans, cur_broken + break_egg(n_egg, egg_list, left+1))
        egg_list[left][0] += right_w
        egg_list[i][0] += left_w
    return ans

def main():
    n_egg = int(input().strip())
    egg_list = list()
    for _ in range(n_egg):
        egg_list.append(list(map(int, input().split())))
    print(break_egg(n_egg, egg_list, 0))
    return
if __name__ == "__main__":
    main()