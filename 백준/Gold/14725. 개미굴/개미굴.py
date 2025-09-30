from sys import stdin
input = stdin.readline

def find_feed(ant_map):
    stack = list()
    stack.append((0, "", ant_map))
    while(stack):
        cur_floor, feed, cur_room = stack.pop()
        if cur_floor > 0:
            string = ""
            for _ in range((cur_floor-1)*2):
                string = string+"-"
            print(string + feed)
        key_list = list(cur_room.keys())
        key_list.sort(reverse=True)
        for key in key_list:
            stack.append((cur_floor+1, key, cur_room[key]))
    return

def main():
    ant_count = int(input().strip())
    ant_map = dict()
    for _ in range(ant_count):
        result = list(input().split())
        r_count = int(result[0])
        before_room = ant_map
        for i in range(1, r_count+1):
            if not result[i] in before_room:
                before_room[result[i]] = dict()
                before_room = before_room[result[i]]
                continue
            before_room = before_room[result[i]]
    find_feed(ant_map)
    return

if __name__ == "__main__":
    main()
