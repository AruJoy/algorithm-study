from sys import stdin

def sudden_attack_3(n_player):
    if n_player == 1:
        print('Yes')
        return
    player_list = list(map(int, stdin.readline().split(' ')))
    joonwon = player_list.pop(0)
    
    player_list.sort(reverse= True)
    
    while player_list:
        if(joonwon <= player_list[len(player_list)-1]):
            print('No')
            return
        joonwon += player_list.pop()
    
    print('Yes')
    return

n_player = int(stdin.readline())
sudden_attack_3(n_player)