from sys import stdin
def get_Lcs_length(string1, string2):
    lcs_table = dict()
    lcs_table[0] = [0 for _ in range(len(string2) + 1)]
    for s1 in range(1, len(string1) + 1):
        before_lcs_condition = lcs_table[s1 -1]
        current_lcs_condition = [0 for _ in range(len(string2) + 1)]
        for s2 in range(1, len(string2) + 1):
            if string1[s1-1] == string2[s2-1]:
                current_lcs_condition[s2] = before_lcs_condition[s2 - 1] + 1
            else: current_lcs_condition[s2] = max(before_lcs_condition[s2], current_lcs_condition[s2-1])
        lcs_table[s1] = current_lcs_condition
    return lcs_table[len(string1)][len(string2)]

string1 = list(stdin.readline().rstrip())
string2 = list(stdin.readline().rstrip())

print(get_Lcs_length(string1, string2))