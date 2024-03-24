from sys import stdin
input = int(stdin.readline())

def rank(point):
    if point >= 90:
        return print('A')
    if point >= 80:
        return print('B')
    if point >= 70:
        return print('C')
    if point >= 60:
        return print('D')
    return print('F')
    
rank(input)