from sys import stdin
from collections import deque
def find_lighter_than_middle(lighter_list, middle_condition):
    expired_balls = 0
    for ball in lighter_list:
        lighter_balls = 0
        stack = deque()
        checked_ball = [False for i in range(balls+1)]
        for i in ball:
            if not checked_ball[i]:
                stack.append(i)
                lighter_balls += 1
                checked_ball[i] = True
        while stack:
            inner_ball = stack.pop()
            for i in lighter_list[inner_ball]:
                if not checked_ball[i]:
                    stack.append(i)
                    lighter_balls += 1
                    checked_ball[i] = True
        if lighter_balls >= middle_condition:
            expired_balls += 1
    return expired_balls

def find_heavier_than_middle(heavier_list, middle_condition):
    expired_balls = 0
    for ball in heavier_list:
        heavier_balls = 0
        stack = deque()
        checked_ball = [False for i in range(balls+1)]
        for i in ball:
            if not checked_ball[i]:
                stack.append(i)
                heavier_balls += 1
                checked_ball[i] = True
        while stack:
            inner_ball = stack.pop()
            for i in heavier_list[inner_ball]:
                if not checked_ball[i]:
                    stack.append(i)
                    heavier_balls += 1
                    checked_ball[i] = True
        if heavier_balls >= middle_condition:
            expired_balls += 1
    return expired_balls


balls, edges = map(int, stdin.readline().split(' '))
heavier_list = [list() for i in range(balls + 1)]
lighter_list = [list() for i in range(balls + 1)]
middle_condition = (balls+1) // 2 
for i in range(edges):
    heavier, lighter = map(int, stdin.readline().split(' '))
    heavier_list[lighter].append(heavier)
    lighter_list[heavier].append(lighter)

result = 0
result += find_lighter_than_middle(lighter_list, middle_condition)
result += find_heavier_than_middle(heavier_list, middle_condition)

print(result)