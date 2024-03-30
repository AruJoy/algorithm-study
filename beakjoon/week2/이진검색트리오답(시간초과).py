from sys import stdin, setrecursionlimit
setrecursionlimit(500000)
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
root = None
def insert(node, value):
    if node.value > value:
        if node.left == None:
            node.left = Node(value)
        else:
            insert(node.left, value)
    else:
        if node.right == None:
            node.right = Node(value)
        else:
            insert(node.right, value)
def postOrder(n):
    if n!= None:
        if n.left:
            postOrder(n.left)
        if n.right:
            postOrder(n.right)
        print(n.value)
nodes = list()

while True:
    line = stdin.readline().strip()
    if line != "":
        nodes.append(int(line))
    else:
        break
    
for i in range(len(nodes)):
    if i == 0:
        root = Node(nodes[i])
    else:
        insert(root, nodes[i])

postOrder(root)