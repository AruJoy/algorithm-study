from sys import stdin
input = stdin.readline

def get_input():
    board_size = int(input())
    board = []
    max_value = 0
    for i in range(board_size):
        row = list(map(int, input().split(" ")))
        board.append(row)
        for j in range(board_size):
            max_value = max(row[j], max_value)
    return board_size, board, max_value

def move_line(direction:int, line:list, board_size:int):
    answer = 0
    line = [x for x in line if x != 0]
    if direction == 0 or direction == 1:
        for i in range(len(line) - 1):
            if line[i] == line[i+1]:
                line[i] = 2*line[i]
                line[i+1] = 0
                answer = max(line[i], answer)
        line = [x for x in line if x != 0]
        zero_needed = board_size - len(line)
        line = line + [0 for _ in range(zero_needed)]
        return line, answer
    for i in range(len(line) - 1):
        if line[-(i+1)] == line[-(i+2)]:
            line[-(i+1)] = 2*line[-(i+1)]
            line[-(i+2)] = 0
            answer = max(line[-(i+1)], answer)
    line = [x for x in line if x != 0]
    zero_needed = board_size - len(line)
    line = [0 for _ in range(zero_needed)] + line
    return line, answer

def move_board(direction:int, board_size:int, board:list):
    new_board = [row[:] for row in board]
    answer = 0
    for i in range(board_size):
        if(direction % 2 == 0):
            new_line, new_answer = move_line(direction, new_board[i], board_size)
            answer = max(answer, new_answer)
            new_board[i] = new_line
            continue
        
        new_line, new_answer = move_line(direction, [new_board[j][i] for j in range(board_size)], board_size)
        answer = max(answer, new_answer)
        for j in range(board_size):
            new_board[j][i] = new_line[j]

    return new_board, answer

def get_answer(board_size:int, board:list, repeat:int, max_value:int):
    answer = max_value
    for i in range(4):
        new_board, new_answer = move_board(i, board_size, board)
        answer = max(answer, new_answer)
        if repeat == 5:
            continue
        new_answer = get_answer(board_size, new_board, repeat+1, max_value)
        answer = max(answer, new_answer)
    return answer

board_size, board, max_value = get_input()

print(get_answer(board_size, board, 1, max_value))