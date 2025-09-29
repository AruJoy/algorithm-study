from sys import stdin
input = stdin.readline
INF = float('INF')
def find(root_table, index):
    cur = index
    while cur != root_table[cur]:
        cur = root_table[cur]
    return cur

def union(root_table, a, b):
    if root_table[a] == -1:
        root_table[a] = a
    if root_table[b] != -1:
        a_root, b_root = find(root_table, a), find(root_table, b)
        if a_root > b_root: 
            root_table[a_root] = b_root
            return
        root_table[b_root] = a_root
        return
    root_table[b] = a
    return

def cycle(n_turn, root_table, dot_list):
    for i in range(n_turn):  
        a, b = dot_list[i]
        if (root_table[a] != -1 and root_table[b] != -1
            and find(root_table, a) == find(root_table, b)):
            return i+1
        union(root_table, a, b)
    return 0

def main():
    n_dot, n_turn = map(int, input().split())
    root_table = [-1 for i in range(n_dot)]
    dot_list = []
    for _ in range(n_turn):
        a, b = map(int, input().split())
        a, b = min(a, b), max(a, b)
        dot_list.append((a, b))
    print(cycle(n_turn, root_table, dot_list))
    return

if __name__ == "__main__":
    main()
