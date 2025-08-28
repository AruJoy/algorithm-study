from sys import stdin

rows, columns = map(int, stdin.readline().split())

paper = []
for _ in range(rows):
    line = list(map(int, stdin.readline().split()))
    paper.append(line)

tet_matrix = [
    [[1,1,1,1]],
    [[1,1],[1,1]],
    [[0,0,1],[1,1,1]],
    [[1,1,0],[0,1,1]],
    [[0,1,0],[1,1,1]]
]

def cover_paper(matrix):
    max_value = 0
    matrix_height = len(matrix)
    matrix_width = len(matrix[0])
    for y in range(rows - matrix_height + 1):
        for x in range(columns - matrix_width + 1):
            value = 0
            for tet_y in range(matrix_height):
                for tet_x in range(matrix_width):
                    if matrix[tet_y][tet_x] == 1:
                        value += paper[y + tet_y][x + tet_x]
            max_value = max(max_value, value)
    return max_value

def rotate_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    rotated = []
    for x in range(cols):
        new_row = []
        for y in range(rows):
            new_row.append(matrix[rows - 1 - y][x])
        rotated.append(new_row)
    return rotated

def flip_matrix(matrix):
    return [row[::-1] for row in matrix]

answer = 0
symmetric_pieces = [2, 3, 4]

for i in range(5):
    current_matrix = [row[:] for row in tet_matrix[i]]
    for rotation in range(4):
        answer = max(answer, cover_paper(current_matrix))
        current_matrix = rotate_matrix(current_matrix)
    if i in symmetric_pieces:
        flipped_matrix = flip_matrix(tet_matrix[i])
        for rotation in range(4):
            answer = max(answer, cover_paper(flipped_matrix))
            flipped_matrix = rotate_matrix(flipped_matrix)

print(answer)