from sys import stdin
columns, rows = map(int, stdin.readline().split(' '))
room = list()
for column in range(columns):
    line = list(stdin.readline().rstrip())
    room.append(line)
checked = [[False for i in range(rows)] for i in range(columns)]



def find_number_of_wood_board():
    wood_board = 0
    pointer = [0,0]
    for column in range(columns):
        for row in range(rows):
            if checked[column][row] == False:
                wood_board += 1
                if room[column][row] == '-':
                    pointer = [column, row]
                    checked[column][row] = True
                    while pointer[1] < rows - 1:
                            if room[pointer[0]][pointer[1]+1] == '-':
                                checked[pointer[0]][pointer[1]+1] = True
                                pointer = [pointer[0], pointer[1]+1]
                            else:
                                break
                else:
                    pointer = [column, row]
                    checked[column][row] = True
                    while pointer[0] < columns - 1:
                        if room[pointer[0]+1][pointer[1]] == '|':
                            checked[pointer[0]+1][pointer[1]] = True
                            pointer = [pointer[0]+1, pointer[1]]
                        else:
                            break
    return wood_board


print(find_number_of_wood_board())