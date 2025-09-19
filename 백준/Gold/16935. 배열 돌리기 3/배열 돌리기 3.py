from sys import stdin
input = stdin.readline

def act_1(m): return m[::-1]
def act_2(m): return [row[::-1] for row in m]
def act_3(m): return [list(row) for row in zip(*m[::-1])]
def act_4(m): return [list(row) for row in zip(*m)][::-1]

def split_quadrants(m):
    r, c = len(m), len(m[0]); r2, c2 = r//2, c//2
    A = [row[:c2] for row in m[:r2]]
    B = [row[c2:] for row in m[:r2]]
    C = [row[c2:] for row in m[r2:]]
    D = [row[:c2] for row in m[r2:]]
    return A, B, C, D

def merge_quadrants(A, B, C, D):
    return [a+b for a,b in zip(A,B)] + [d+c for d,c in zip(D,C)]

def act_5(m):
    A,B,C,D = split_quadrants(m)
    return merge_quadrants(D,A,B,C)

def act_6(m):
    A,B,C,D = split_quadrants(m)
    return merge_quadrants(B,C,D,A)

def main():
    rows, cols, _ = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(rows)]
    ops = list(map(int, input().split()))
    ops_map = {1:act_1, 2:act_2, 3:act_3, 4:act_4, 5:act_5, 6:act_6}
    for op in ops:
        m = ops_map[op](m)
    print('\n'.join(' '.join(map(str, row)) for row in m))

if __name__ == "__main__":
    main()
