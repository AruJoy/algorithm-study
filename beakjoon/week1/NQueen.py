from sys import stdin
numberOfQueens = int(stdin.readline())
checkerBoard = [[0 for i in range(numberOfQueens)] for i in range(numberOfQueens)]
def setAttackRange(r,c):
    for i in range(numberOfQueens):
        if 0 <= r-i < numberOfQueens and 0<= i+c < numberOfQueens:
            checkerBoard[r-i][i+c] = 1
        if 0 <= r-i < numberOfQueens and 0 <= c-i < numberOfQueens:
            checkerBoard[r-i][c-i] = 1
        checkerBoard[i][c] = 1
        checkerBoard[r][i] = 1


def adjustQueen(line, queens, case):
    global checkerBoard
    if line < queens:
        return case
    if queens == 0 :
        return case+1
    
    for i in range(numberOfQueens):
        if checkerBoard[line-1][i] == 0:
            temp_board = [row[:] for row in checkerBoard]
            setAttackRange(line-1, i)
            case = adjustQueen(line-1, queens-1, case)
            checkerBoard = temp_board
    return case

print(adjustQueen(numberOfQueens, numberOfQueens, 0))
print(type(checkerBoard))