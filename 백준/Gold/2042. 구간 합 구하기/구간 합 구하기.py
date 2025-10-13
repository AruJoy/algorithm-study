from sys import stdin
input = stdin.readline

def build(seg_tree, num_list, node, start, end):
    if start == end:
        seg_tree[node] = num_list[start]
        return num_list[start]
    mid = (start + end) // 2
    cur_result = (build(seg_tree, num_list, node * 2, start, mid)
                  + build(seg_tree, num_list, node * 2 + 1, mid + 1, end))
    seg_tree[node] = cur_result
    return cur_result

def update(seg_tree, node, start, end, index, value):
    if index < start or index > end:
        return seg_tree[node]
    if start == end:
        seg_tree[node] = value
        return seg_tree[node]
    mid = (start + end) // 2
    left = update(seg_tree, node * 2, start, mid, index, value)
    right = update(seg_tree, node * 2 + 1, mid + 1, end, index, value)
    seg_tree[node] = left + right
    return seg_tree[node]

def query(seg_tree, node, start, end, left, right):
    if right < start or left > end:
        return 0
    if left <= start and end <= right:
        return seg_tree[node]
    mid = (start + end) // 2
    l_sum = query(seg_tree, node * 2, start, mid, left, right)
    r_sum = query(seg_tree, node * 2 + 1, mid + 1, end, left, right)
    return l_sum + r_sum

def main():
    n_number, n_change, n_query = map(int, input().split())
    seg_tree = [0 for _ in range(4*n_number)]
    num_list = [0]
    for _ in range(n_number):
        num_list.append(int(input().strip()))
    build(seg_tree, num_list, 1, 1, n_number)
    for _ in range(n_change + n_query):
        commend, x, y = map(int, input().split())
        if commend == 1:
            update(seg_tree, 1, 1, n_number, x, y)
            num_list[x] = y
            continue
        print(query(seg_tree, 1, 1, n_number, x, y))

if __name__ == "__main__":
    main()
