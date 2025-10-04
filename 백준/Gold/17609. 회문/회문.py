from sys import stdin
input = stdin.readline
from collections import deque
def judge(string):
    if len(string) == 1: return 0
    judge_range = (len(string)+1)//2
    lft = 0
    for i in range(judge_range):
        if string[i+lft] != string[-i-1]:
            if lft != 0:
                lft = 2
                break
            if string[i+lft+1] == string[-i-1]:
                lft += 1
                continue
            lft = 2
            break
    if lft == 0:
        return 0
    if lft == 1:
        return 1
    rgt = 0
    for i in range(judge_range):
        if string[i] != string[-i-1-rgt]:
            if rgt != 0:
                rgt = 2
                break
            if string[i] == string[-i-2-rgt]:
                rgt += 1
                continue
            rgt = 2
            break
    if rgt == 0:
        return 0
    if rgt == 1:
        return 1
    return 2
def main():
    t_count = int(input().strip())
    for _ in range(t_count):
        string = input().strip()
        print(judge(string))
    return
if __name__ == "__main__":
    main()