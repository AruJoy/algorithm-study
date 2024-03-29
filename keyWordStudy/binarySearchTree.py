class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def setRoot(self, val):
        self.root = Node(val)
    def find(self, val):
        return self.findNode(self.root, val) is not None
    def findNode(self, currentNode, val):
        if (currentNode is None):
            return None
        elif (val == currentNode.val):
            return currentNode
        elif (val < currentNode.val):
            return self.findNode(currentNode.leftChild, val)
        else:
            return self.findNode(currentNode.rightChild, val)
    def insert(self, val):
        if (self.root is None):
            self.setRoot(val)
        else:
            self.insertNode(self.root, val)
    def insertNode(self, currentNode, val):
        if(val <= currentNode.val):
            if(currentNode.leftChild):
                self.insertNode(currentNode.leftChild, val)
            else:
                currentNode.leftChild = Node(val)
        elif (val > currentNode.val):
            if (currentNode.rightChild):
                self.insertNode(currentNode.rightChild, val)
            else:
                currentNode.rightChild = Node(val)
    def delete(self, val):
        if self.root is None:
            return False
        
        is_searched = False
        self.current_node = self.root
        self.parent = None
        
        # 노드 찾기
        while self.current_node:
            if self.current_node.val == val:
                is_searched = True
                break
            elif val < self.current_node.val:
                self.parent = self.current_node
                self.current_node = self.current_node.leftChild
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.rightChild
                
        if not is_searched:
            return False
        
        # 자식 노드가 없는 경우
        if self.current_node.leftChild is None and self.current_node.rightChild is None:
            if self.parent is None:
                self.root = None
            elif val < self.parent.val:
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        
        # 자식 노드가 한 개 있는 경우
        elif self.current_node.leftChild is None:
            if val < self.parent.val:
                self.parent.leftChild = self.current_node.rightChild
            else:
                self.parent.rightChild = self.current_node.rightChild
        elif self.current_node.rightChild is None:
            if val < self.parent.val:
                self.parent.leftChild = self.current_node.leftChild
            else:
                self.parent.rightChild = self.current_node.leftChild
                
        # 자식 노드가 두 개 있는 경우
        else:
            # 후임자 노드 찾기
            successor_parent = self.current_node
            successor = self.current_node.rightChild
            while successor.leftChild:
                successor_parent = successor
                successor = successor.leftChild
            
            # 후임자 노드의 값을 현재 노드로 대체
            self.current_node.val = successor.val
            
            # 후임자 노드의 부모 노드와 후임자 노드를 연결
            if successor_parent.leftChild == successor:
                successor_parent.leftChild = successor.rightChild
            else:
                successor_parent.rightChild = successor.rightChild
                
        return True
    