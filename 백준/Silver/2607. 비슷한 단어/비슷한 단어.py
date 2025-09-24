from sys import stdin
input = stdin.readline
def main():
    word_count = int(input().strip())
    original_word = list(input().strip())
    original_word_map = [[],[]]
    answer = 0
    for a in original_word:
        if not a in original_word_map[0]:
            original_word_map[0].append(a)
            original_word_map[1].append(1)
            continue
        t = original_word_map[0].index(a)
        original_word_map[1][t]+=1
    
    for _ in range(word_count-1):
        word = list(input().strip())
        word_map = [[],[]]
        for a in word:
            if not a in word_map[0]:
                word_map[0].append(a)
                word_map[1].append(1)
                continue
            t = word_map[0].index(a)
            word_map[1][t]+=1
        if abs(len(original_word) - len(word)) > 1:
            continue
        add = 0
        sub = 0
        for i in range(len(word_map[0])):
            if not word_map[0][i] in original_word_map[0]:
                add += word_map[1][i]
            else:
                t = original_word_map[0].index(word_map[0][i])
                if original_word_map[1][t] > word_map[1][i]:
                    sub += original_word_map[1][t]-word_map[1][i]
                if original_word_map[1][t] < word_map[1][i]:
                    add += word_map[1][i] - original_word_map[1][t]
        for i in range(len(original_word_map[0])):
            if not original_word_map[0][i] in word_map[0]:
                sub += original_word_map[1][i]
        if sub == 1 and add == 1:
            answer += 1
            continue
        if add + sub > 2:
            continue
        answer += 1
    print(answer)
    return
if __name__ == "__main__":
    main()
