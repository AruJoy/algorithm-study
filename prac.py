from sys import stdin

def multi_tab(appliances, holes, uses):
    start = holes
    before_multi_tab = appliances[0:holes]
    current_multi_tab = list()
    count = 0
    while start < uses:
        if start + holes < uses:
            current_multi_tab = appliances[start : start + holes]
            start = start + holes
        else:
            current_multi_tab = appliances[start : uses]
            start = uses + holes
        
        count_change = len(current_multi_tab)
        for i in range(len(current_multi_tab)):
            if current_multi_tab[i] in before_multi_tab:
                count_change -= 1
        count += count_change
        before_multi_tab = current_multi_tab
    return count

holes, uses = map(int, stdin.readline().split(' '))
appliances = list(map(int, stdin.readline().split(' ')))
delete_list = list()
for i in range(1, len(appliances)):
    if appliances[i] == appliances[i-1]:
        delete_list.append(i)
for i in delete_list:
    del appliances[i]
uses = len(appliances)

print(multi_tab(appliances, holes, uses))