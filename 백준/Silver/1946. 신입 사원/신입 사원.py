from sys import stdin
from heapq import heapify, heappop

def recruit(n_applicant):
    applicant_list = list()
    for applicant in range(n_applicant):
        i, j = map(int, stdin.readline().split(' '))
        applicant_list.append([i,j])
    
    heapify(applicant_list)
    recruit_count = 0
    end_condition = n_applicant
    for i in range(n_applicant):
        applicant = heappop(applicant_list)
        if applicant[1] <= end_condition:
            recruit_count += 1
            end_condition = applicant[1]
    return recruit_count

test_trials = int(stdin.readline())
for test in range(test_trials):
    n_applicant = int(stdin.readline())
    print(recruit(n_applicant))