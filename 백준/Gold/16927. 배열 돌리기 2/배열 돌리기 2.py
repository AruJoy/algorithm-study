from sys import stdin
input = stdin.readline
def rotate(rows, columns, layers, matrix, move):
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    layer_list = []
    for r in range(layers):
        new_layer = []
        count = 2*(rows-2*r) + 2*(columns-2*r) - 4
        y = r
        x = r
        direction = 0
        for _ in range(count):
            new_layer.append([y,x])
            y, x = y + dy[direction], x+dx[direction]
            if r == y or rows - 1 - r == y:
                if r == x or columns - 1 - r == x:
                    direction = (direction + 1)%4
                    continue
        layer_list.append(new_layer)
    c_layer_list = [row[:] for row in layer_list]
    c_matrix = [row[:] for row in matrix]
    
    for i in range(layers):
        now_move = move % len(layer_list[i])
        layer_list[i] = layer_list[i][now_move:]+layer_list[i][:now_move]
        
    for i in range(layers):
        for j in range(len(layer_list[i])):
            matrix[c_layer_list[i][j][0]][c_layer_list[i][j][1]] = c_matrix[layer_list[i][j][0]][layer_list[i][j][1]]
    return matrix
def main():
    rows, columns, count = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(rows)]
    layers = min(rows, columns)//2
    matrix = rotate(rows, columns, layers, matrix, count)
    print('\n'.join(' '.join(map(str, row)) for row in matrix))
if __name__ == "__main__":
    main()