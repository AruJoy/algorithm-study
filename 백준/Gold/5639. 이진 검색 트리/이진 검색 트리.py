from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)

def preOrderToPostOrder(preOrder):
    if not preOrder:
        return []

    root = preOrder[0]
    left_sub_tree = [node for node in preOrder[1:] if node < root]
    right_sub_tree = [node for node in preOrder[1:] if node >= root]

    postOrder = []

    postOrder.extend(preOrderToPostOrder(left_sub_tree))
    postOrder.extend(preOrderToPostOrder(right_sub_tree))
    postOrder.append(root)  # 루트를 마지막에 추가하여 후위 순회로 변환

    return postOrder

# 후위 순회 출력 함수
def printPostOrder(postOrder):
    for value in postOrder:
        print(value)

preOrder = []
while True:
    line = stdin.readline().strip()
    if line != "":
        preOrder.append(int(line))
    else:
        break



# 전위 순회를 후위 순회로 변환
postOrder = preOrderToPostOrder(preOrder)

# 후위 순회 출력
printPostOrder(postOrder)
