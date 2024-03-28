#노드 클래스
class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None
#트리 구현체
class BinaryTree():
    def __init__(self):
        self.root = None
#전위 순회
    def preOrder(self, n):
        if n!= None:
            print(n.item, '', end='')
            if n.left:
                self.preOrder(n.left)
            if n.right:
                self.preOrder(n.right)
#후위순회
    def postOrder(self, n):
        if n!= None:
            if n.left:
                self.postOrder(n.left)
            if n.right:
                self.postOrder(n.right)
            print(n.item, '',end = '')
#중위 순회
    def inOrder(self, n):
        if n!= None:
            if n.left:
                self.inOrder(n.left)
            print(n.item, '',end='')
            if n.right:
                self.inOrder(n.right)
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)
n6 = Node(60)
n7 = Node(70)
n8 = Node(80)

tree = BinaryTree()
# 노드 연결 방식
tree.root = n1
n1.left = n2
n1.right = n3
n2.right = n5
n2.left = n4
n3.left = n6
n3.right = n7
n4.left = n8
