from sys import stdin
input = stdin.readline

def get_input():
    length, alpha_count = map(int, input().split(" "))
    alpha_list = list(input().strip().split())
    alpha_list.sort()
    return length, alpha_count, alpha_list
def combination(length, alpha_count, alpha_list, m_list,
                pass_word, depth, cursor, m_count, s_count):
    if depth == length:
        print("".join(map(str, pass_word)))
    left_space = length - depth
    for i in range(cursor, alpha_count):
        is_m = alpha_list[i] in m_list
        if is_m:
            if 2 - s_count >= left_space:
                continue
        else:
            if 1 - m_count >= left_space:
                continue
        pass_word.append(alpha_list[i])
        if is_m:
            combination(length, alpha_count, alpha_list, m_list,
                        pass_word, depth+1, i+1, m_count+1, s_count)
        else:
            combination(length, alpha_count, alpha_list, m_list,
                        pass_word, depth+1, i+1, m_count, s_count+1)
        pass_word.pop()
m_list = ["a", "e", "i", "o", "u"]
length, alpha_count, alpha_list,  = get_input()

combination(length, alpha_count, alpha_list, m_list,
                [], 0, 0, 0, 0)