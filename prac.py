from sys import stdin

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preOrder(n):
    if n!= None:
        print(n.value, end='')
        if n.left:
            preOrder(n.left)
        if n.right:
            preOrder(n.right)
def postOrder(n):
    if n!= None:
        if n.left:
            postOrder(n.left)
        if n.right:
            postOrder(n.right)
        print(n.value, end='')
def inOrder(n):
    if n!= None:
        if n.left:
            inOrder(n.left)
        print(n.value, end='')
        if n.right:
            inOrder(n.right)
root = None
nodeList = list()
inputSize = int(input())
for i in range(inputSize):
    if i == 0:
        nodes = input().strip()
        nodes = nodes.split(' ')
        root= Node(nodes[0])
        nodeList.append(root)
        if nodes[1] != '.':
            root.left = Node(nodes[1])
            nodeList.append(root.left)
        if nodes[2] != '.':
            root.right = Node(nodes[2])
            nodeList.append(root.right)
    else:
        nodes = input().strip()
        nodes = nodes.split(' ')
        for i in nodeList:
            if i.value == nodes[0]:
                if nodes[1] != '.':
                    i.left = Node(nodes[1])
                    nodeList.append(i.left)
                if nodes[2] != '.':
                    i.right = Node(nodes[2])
                    nodeList.append(i.right)


preOrder(root)
print()
inOrder(root)
print()
postOrder(root)
print()