from sys import stdin
from collections import deque
input = stdin.readline

def find_max_length(tower_list):
    ans = 0
    stack = []
    for i in range(len(tower_list)):
        if not stack or stack[-1][0] < tower_list[i]:
            stack.append([tower_list[i], i])
            continue
        
        if stack[-1][0] == tower_list[i]:
            continue
        while stack and stack[-1][0] > tower_list[i]:
            info = stack.pop()
            ans = max(ans, info[0] * (i - info[1]))
            ans = max(ans, tower_list[i] * (i - info[1]+1))
        info[0] = tower_list[i]
        stack.append(info)
    
    while stack:
        info = stack.pop()
        ans = max(ans, info[0] * (len(tower_list) - info[1]))
    return ans
def main():
    while True:
        str = input().strip()
        if str == "0":
            break
        tower_list = list(map(int, str.split()))
        print(find_max_length(tower_list[1:]))
    return
if __name__ == "__main__":
    main()