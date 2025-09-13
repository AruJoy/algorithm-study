from sys import stdin
input = stdin.readline

green_board = [[False for _ in range(4)] for __ in range(6)]
blue_board = [[False for _ in range(4)] for __ in range(6)]

def put_block_on_board(board:list, x:int, height:int, width:int, is_blue:bool = False):
    put_y = 0
    if is_blue:
        x_list = [x - i for i in range(width)]
    else:
        x_list = [x + i for i in range(width)]
    for i in range(6):
        put = True
        for block_x in x_list:
            if board[i][block_x]:
                put = False
        if not put:
            break
        put_y = i
    
    y_list = [put_y - i for i in range(height)]
    
    for block_y in y_list:
        for block_x in x_list:
            board[block_y][block_x] = True
    
    return put_y
def get_score(board:list, put_y: int, height:int, width:int):
    min_y = put_y - height +1
    
    if put_y < 2:
        return 0, min_y
    score = 0
    
    for i in range(height):
        satisfying_score = True
        for x in range(4):
            if not board[min_y + i][x]:
                satisfying_score = False
        if not satisfying_score:
            continue
        score += 1
        for x in range(4):
            board[min_y + i][x] = board[min_y + i - 1][x]
    return score, min_y + score

def push_blocks(board: list, score: int, put_y: int):
    
    max_empty_y = put_y - 2 + score
    
    for i in range(6):
        if max_empty_y-i-score < 0:
            break
        for j in range(4):
            board[max_empty_y-i][j] = board[max_empty_y-i-score][j]
    return

def delete_bottoms(board:list, min_y:int):
    delete_rows = 2 - min_y 
    for _ in range(delete_rows):
        board.pop()
    for _ in range(delete_rows):
        board.insert(0, [False for _ in range(4)])
def move_to_board(board:list, x:int, height:int, width:int, is_blue:bool = False):
    put_y = put_block_on_board(board, x, height, width, is_blue = is_blue)    
    score, min_y = get_score(board, put_y, height, width)    
    if score > 0 :
        push_blocks(board, score, put_y)
    if min_y < 2:
        delete_bottoms(board, min_y)
    return score

def put_block(y: int, x:int, block_type:int, green_board:list, blue_board:list):
    score = 0
    blocks = [[1, 1], [1, 2], [2, 1]]
    green_height = blocks[block_type-1][0]
    green_width = blocks[block_type-1][1]
    score += move_to_board(green_board, x, green_height, green_width)
    score += move_to_board(blue_board, 3 - y, green_width, green_height, is_blue = True)
    return score

turns = int(input().strip())
score = 0
blocks = 0
for _ in range(turns):
    if _ == 6:
        _=6
    type, y, x = map(int, input().split(" "))
    score += put_block(y, x, type, green_board, blue_board)
for i in range(6):
    for j in range(4):
        if blue_board[i][j]:
            blocks += 1
for i in range(6):
    for j in range(4):
        if green_board[i][j]:
            blocks += 1
print(score)
print(blocks)