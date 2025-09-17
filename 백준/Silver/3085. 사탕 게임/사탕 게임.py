from sys import stdin

input = stdin.readline

def get_input():
    scale = int(input().strip())
    game_board = []
    for _ in range(scale):
        row = list(input().strip())
        game_board.append(row)
    return scale, game_board
def get_candy(scale:int,game_board:list,index:int, is_column:bool = False):
    candy = 0
    now_candy = 0
    now = ""
    if is_column:
        for i in range(scale):
            if game_board[i][index] != now:
                now = game_board[i][index]
                now_candy = 1
                continue
            now_candy += 1
            candy = max(candy, now_candy)
        return candy
    for i in range(scale):
        if game_board[index][i] != now:
            now = game_board[index][i]
            now_candy = 1
            continue
        now_candy += 1
        candy = max(candy, now_candy)
    return candy
def get_solution(scale:int,game_board:list):
    candy = 0
    for i in range(scale):
        candy = max(candy, get_candy(scale, game_board, i))
        candy = max(candy, get_candy(scale, game_board, i, is_column=True))
    for i in range(scale):
        for j in range(scale-1):
            if game_board[i][j] == game_board[i][j+1]:
                continue
            candy_1 = game_board[i][j]
            candy_2 = game_board[i][j+1]
            game_board[i][j] = candy_2
            game_board[i][j+1] = candy_1
            now_candy = get_candy(scale, game_board, i)
            candy = max(candy, now_candy)
            now_candy = get_candy(scale, game_board, j, is_column=True)
            candy = max(candy, now_candy)
            now_candy = get_candy(scale, game_board, j+1, is_column=True)
            candy = max(candy, now_candy)
            game_board[i][j] = candy_1
            game_board[i][j+1] = candy_2
    for i in range(scale):
        for j in range(scale-1):
            if game_board[j][i] == game_board[j+1][i]:
                continue
            candy_1 = game_board[j][i]
            candy_2 = game_board[j+1][i]
            game_board[j][i] = candy_2
            game_board[j+1][i] = candy_1
            now_candy = get_candy(scale, game_board, j)
            candy = max(candy, now_candy)
            now_candy = get_candy(scale, game_board, j+1)
            candy = max(candy, now_candy)
            now_candy = get_candy(scale, game_board, i, is_column=True)
            candy = max(candy, now_candy)
            game_board[j][i] = candy_1
            game_board[j+1][i] = candy_2
    return candy
scale, game_board = get_input()

print(get_solution(scale,game_board))
