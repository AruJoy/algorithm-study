from sys import stdin
input = stdin.readline

def main():
    n_number = int(input().strip())
    number_list = list(map(int, input().split()))
    MAX = max(number_list)
    exist = [False for _ in range(MAX + 1)]
    
    for n in number_list:
        exist[n] = True
    
    score_board = [0 for i in range(MAX + 1)]
    
    for a in number_list:
        multi = a * 2
        while multi <= MAX:
            if exist[multi]:
                score_board[multi] -= 1
                score_board[a] += 1
            multi += a
    
    print(*[score_board[a] for a in number_list])
    return

if __name__ == "__main__":
    main()