from sys import stdin
input = stdin.readline
from collections import deque
INF = float("inf")
def is_union(adj_list, visited_list, selected_list):
    if len(selected_list) == 1:
        return True
    visited_list[selected_list[0]] = True
    que = deque()
    union_count = 1
    que.append(selected_list[0])
    while que:
        cur = que.popleft()
        for nxt in adj_list[cur]:
            if visited_list[nxt]:continue
            if nxt in selected_list:
                visited_list[nxt] = True
                union_count += 1
                if union_count == len(selected_list):
                    return True
                que.append(nxt)
    return False

def left_is_union(n_city, adj_list, visited_list, selected_list):
    if n_city - len(selected_list) == 1:
        return True
    start = -1
    for i in range(n_city):
        if not i in selected_list:
            start = i
            break
    visited_list[start] = True
    que = deque()
    union_count = 1
    que.append(start)
    while que:
        cur = que.popleft()
        for nxt in adj_list[cur]:
            if visited_list[nxt]:continue
            if not nxt in selected_list:
                visited_list[nxt] = True
                union_count += 1
                if union_count == n_city - len(selected_list):
                    return True
                que.append(nxt)
    return False
    
def find_min_diff(n_city, cities, adj_list, visited_list, checked_list, selected_list, total_people, mask):
    bit = 1
    ans = INF
    if len(selected_list) == n_city:
        return INF
    if mask != 0:
        for i in range(n_city):
            visited_list[i] = False
        checked_list[mask] = True
        if (is_union(adj_list, visited_list, selected_list)
            and left_is_union(n_city, adj_list, visited_list, selected_list)):
            cur_count = 0
            for i in selected_list:
                cur_count += cities[i]
            ans = abs(total_people - 2 * cur_count)
            if ans == 1:
                ans = 1
    for i in range(n_city):
        if mask & bit or checked_list[mask | bit]:
            bit = bit << 1
            continue
        selected_list.append(i)
        ans = min(ans, find_min_diff(n_city, cities, adj_list, visited_list, checked_list, selected_list, total_people, mask | bit))
        selected_list.pop()
        bit = bit << 1
    return ans
def main():
    n_city = int(input().strip())
    cities = list(map(int, input().split()))
    adj_list = [set() for _ in range(n_city)]
    checked_list = [False for _ in range((1<<n_city))]
    visited_list = [False for _ in range(n_city)]
    for u in range(n_city):
        city_connection = list(map(int, input().split()))
        if city_connection[0] == 0: continue
        for i in range(city_connection[0]):
            v = city_connection[i+1]
            adj_list[u].add(v-1)
            adj_list[v-1].add(u)
    total_people = sum(cities)
    selected_list = list()
    ans = find_min_diff(n_city, cities, adj_list, visited_list, checked_list, selected_list, total_people, 0)
    print(-1 if ans == INF else ans)
    return

if __name__ == "__main__":
    main()