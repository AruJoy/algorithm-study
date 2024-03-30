nodes = int(input())
# tree = [[0, 1, 2], [1, 3, -1], [2, 4, 5], [3, -1, -1], [4, -1, -1], [5, -1, 6], [6, -1, -1], [-1, -1, -1]]
tree = []
for _ in range(nodes + 1):
    tree.append([-1, -1, -1])
for i in range(nodes):
    list = input().split(" ")
    adjlist = [-1, -1, -1]
    for j in range(3):
        if list[j] == "." : continue
        else: adjlist[j] = ord(list[j]) - 65
    # print(adjlist)
    tree[adjlist[0]] = (adjlist)
# print(tree)
def travel(adjlist):
    global tree, preorder, inorder, postorder
    if adjlist[0] == -1: return
    char = chr(adjlist[0] + 65)
    preorder.append(char)
    left_child = adjlist[1]
    right_child = adjlist[2]
    travel(tree[left_child])
    inorder.append(char)
    travel(tree[right_child])
    postorder.append(char)
    return
preorder = []
inorder = []
postorder = []
travel(tree[0])
print("".join(preorder))
print("".join(inorder))
print("".join(postorder))





