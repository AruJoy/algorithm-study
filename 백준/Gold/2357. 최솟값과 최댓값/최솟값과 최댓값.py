from sys import stdin
input = stdin.readline
MOD = 1000000007
MIN = -float("inf")
MAX = float("inf")

def max_build(seg_tree, num_list, node, start, end):
    if start == end:
        seg_tree[node] = num_list[start]
        return seg_tree[node]
    mid = (start + end)//2
    cur_val = max(max_build(seg_tree, num_list, node * 2, start, mid),
                    max_build(seg_tree, num_list, node * 2 + 1, mid + 1, end))
    seg_tree[node] = cur_val
    return cur_val

def min_build(seg_tree, num_list, node, start, end):
    if start == end:
        seg_tree[node] = num_list[start]
        return seg_tree[node]
    mid = (start + end)//2
    cur_val = min(min_build(seg_tree, num_list, node * 2, start, mid),
                    min_build(seg_tree, num_list, node * 2 + 1, mid + 1, end))
    seg_tree[node] = cur_val
    return cur_val

def max_query(seg_tree, node, start, end, left, right):
    if right < start or left > end:
        return MIN
    if left <= start and right >= end:
        return seg_tree[node]
    
    mid = (start + end) // 2
    
    cur_val = max(max_query(seg_tree, node * 2, start, mid, left, right),
                    max_query(seg_tree, node * 2 + 1, mid + 1, end, left, right))
    
    return cur_val
def min_query(seg_tree, node, start, end, left, right):
    if right < start or left > end:
        return MAX
    if left <= start and right >= end:
        return seg_tree[node]
    
    mid = (start + end) // 2
    
    cur_val = min(min_query(seg_tree, node * 2, start, mid, left, right),
                    min_query(seg_tree, node * 2 + 1, mid + 1, end, left, right))
    
    return cur_val
def main():
    n_number, n_commend = map(int, input().split())
    max_seg = [0] * (n_number * 4)
    min_seg = [0] * (n_number * 4)
    num_list = [0] + [int(input()) for _ in range(n_number)]
    max_build(max_seg, num_list, 1, 1, n_number)
    min_build(min_seg, num_list, 1, 1, n_number)
    
    for _ in range(n_commend):
        a, b = map(int, input().split())
        print(min_query(min_seg, 1, 1, n_number, a, b), max_query(max_seg, 1, 1, n_number, a, b))

if __name__ == "__main__":
    main()
