from sys import stdin
from collections import deque
input = stdin.readline
INF = float("INF")
class Node:
    def __init__(self):
        self.children = dict()
        self.is_end = False

    def add_node(self, word):
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Node()
            cur = cur.children[ch]
        cur.is_end = True
    
    def next_node(self, ch):
        if ch not in self.children:
            return None
        return self.children[ch]
    
    def check_status(self):
        return self.is_end, bool(self.children)
def find_word(trie:Node, cube_list, n_cube):
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    score_board = {1:0, 2:0, 3:1, 4:1, 5:2, 6:3, 7:5}
    answer = []
    for i in range(n_cube):
        find_word = set()
        longest = ''
        for j in range(4):
            for k in range(4):
                result = trie.next_node(cube_list[i][j][k])
                if not result:
                    continue
                is_word, _ = result.check_status()
                if is_word:
                    find_word.add(cube_list[i][j][k])
                    if len(longest) == 0:
                        longest = cube_list[i][j][k]
                value = (j*4)+k
                que = deque()
                que.append((j, k, cube_list[i][j][k], 1<<value, result))
                while que:
                    cur_y , cur_x, cur_s, mask, cur_n = que.popleft()
                    for l in range(8):
                        y, x = cur_y + dy[l], cur_x + dx[l]
                        if (y < 0 or 3 < y
                            or x < 0 or 3 < x):
                            continue
                        value = (y*4)+x
                        new_mask = 1<<value
                        if mask & new_mask:
                            continue
                        new_node = cur_n.next_node(cube_list[i][y][x])
                        if not new_node: continue
                        is_word, Continuable = new_node.check_status()
                        if is_word:
                            find_word.add(cur_s+cube_list[i][y][x])
                            if len(longest) < len(cur_s)+1:
                                longest = cur_s+cube_list[i][y][x]
                            if len(longest) == len(cur_s)+1:
                                longest = min(longest, cur_s+cube_list[i][y][x])
                        if Continuable:
                            que.append((y, x, cur_s+cube_list[i][y][x], mask | new_mask, new_node))
        score = 0
        for word in find_word:
            if len(word) > 7:
                score += 11
                continue
            score += score_board[len(word)]
        answer.append([str(score), longest, str(len(find_word))])
    return answer
def main():
    trie = Node()
    words = int(input().strip())
    for _ in range (words):
        trie.add_node(input().strip())
    input()
    cube_list = []
    n_cube = int(input().strip())
    for i in range(n_cube):
        cube_list.append([])
        for _ in range(4):
            cube_list[i].append(list(input().strip()))
        if i != n_cube-1:
            input()
    answer = find_word(trie, cube_list, n_cube)
    for row in answer:
        print(*row)
    return
if __name__ == "__main__":
    main()