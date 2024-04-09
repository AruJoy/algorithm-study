from sys import stdin

def recruit(n_applicant):
    applicant_list = [[False for i in range(n_applicant)]for j in range(n_applicant)]
    for applicant in range(n_applicant):
        i, j = map(int, stdin.readline().split(' '))
        applicant_list[i-1][j-1] = True
    
    recruit_count = 0
    end_condition = n_applicant - 1
    for i in range(n_applicant):
        for j in range(n_applicant):
            if applicant_list[i][j] == True:
                end_condition = j
                recruit_count += 1
                break
            elif j == end_condition:
                break
    return recruit_count

test_trials = int(stdin.readline())
for test in range(test_trials):
    n_applicant = int(stdin.readline())
    print(recruit(n_applicant))