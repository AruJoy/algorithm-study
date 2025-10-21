from sys import stdin
input = stdin.readline


def find(root_table, a):
    if root_table[a] == a:
        return a
    root_table[a] = find(root_table, root_table[a])
    return root_table[a]


def main():
    n_gate = int(input().strip())
    n_plane = int(input().strip())
    root_table = [i for i in range(n_gate + 1)]
    ans = 0
    for _ in range(n_plane):
        a = int(input().strip())
        if a > n_gate:
            break
        a_root = find(root_table, a)
        if a_root == 0:
            break
        b_root = find(root_table, a_root - 1)
        root_table[a_root] = b_root
        ans += 1
    print(ans)
    return


if __name__ == "__main__":
    main()
