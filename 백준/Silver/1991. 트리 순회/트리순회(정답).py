import sys
count = int(sys.stdin.readline().strip())
tree = {}

for n in range(count):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]

#전위 root > 왼쪽 자식 > 오른쪽 자식
def preorder(root):
    if root != '.': # 더 이상 자식 있어~?
        print(root, end='')
        preorder(tree[root][0]) #부모값 root를 받았으니 그의 자식 0, 1번인덱스로 계속 재귀타고 들어가라.
        preorder(tree[root][1]) # 0-왼, 1-오

#중위 왼쪽 자식 > root > 오른쪽 자식
def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

#후위 왼쪽 자식 > 오른쪽 자식 > root
def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

#재귀 스타트 초깃값은 루트A
preorder('A')
print()
inorder('A')
print()
postorder('A')