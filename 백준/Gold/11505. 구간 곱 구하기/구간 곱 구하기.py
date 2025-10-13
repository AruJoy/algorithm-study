from sys import stdin
input = stdin.readline
MOD = 1000000007
def build(seg_tree, num_list, node, start, end):
    if start == end:
        seg_tree[node] = num_list[start]
        return num_list[start]
    mid = (start + end) // 2
    
    cur_val = (build(seg_tree, num_list, node * 2, start, mid)
                * build(seg_tree, num_list, node * 2 + 1, mid + 1, end)) % MOD
    
    seg_tree[node] = cur_val
    
    return cur_val

def update(seg_tree, node, start, end, index, value):
    if index < start or index > end:
        return seg_tree[node]
    if start == end:
        seg_tree[node] = value
        return seg_tree[node]
    
    mid = (start + end) // 2
    
    cur_val = (update(seg_tree, node * 2, start, mid, index, value)
                * update(seg_tree, node * 2 + 1, mid + 1, end, index, value)) % MOD
    
    seg_tree[node] = cur_val
    
    return cur_val

def query(seg_tree, node, start, end, left, right):
    if right < start or left > end:
        return 1
    if left <= start and end <= right:
        return seg_tree[node]
    mid = (start + end)//2
    l_multi = query(seg_tree, node * 2, start, mid, left, right)
    r_multi = query(seg_tree, node * 2 + 1, mid + 1, end, left, right)
    return l_multi * r_multi % MOD

def main():
    n_number, n_commend, n_query = map(int, input().split())
    seg_tree = [1] * (n_number * 4)
    num_list = [1] + [int(input()) for _ in range(n_number)]
    build(seg_tree, num_list, 1, 1, n_number)

    for _ in range(n_commend + n_query):
        a, b, c = map(int, input().split())
        if a == 1:
            update(seg_tree, 1, 1, n_number, b, c)
        else:
            print(query(seg_tree, 1, 1, n_number, b, c))

if __name__ == "__main__":
    main()
