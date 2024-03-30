# https://velog.io/@ceusun0815/%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-B-Tree-%EA%B5%AC%ED%98%84 참고
class BTreeNode:
    def __init__(self):
        self.values = [] #노드에 저장된 값
        self.children = [] #자식노드

# 각 레벨의 노드와 해당 노드의 값을 출력
def print_tree(node, level = 0):
    if node is not None:
        print(f'Level {level}: {node.values}')
        for child in node.children:
            print_tree(child, level + 1)

# B-Tree
class Btree:
    def __init__(self):
        self.root = BTreeNode()
    def insert(self, value):
        self.insert_value(self.root, value)
    def insert_value(self, node, value):
        # 현재 노드의 children 리스트가 비어있는지를 확인
        if not node.children:  # 현재 노드가 리프 노드인 경우 -> 값 삽입
            node.values.append(value) # 삽입
            node.values.sort() # 정렬

            if len(node.values) > 4:  # 노드가 가득 찼을 경우 -> 분할
                left_node = BTreeNode() # 좌측 자식 노드
                right_node = BTreeNode() # 우측 자식 노드
                left_node.values = node.values[:2] # 중간값을 기준으로 분할
                right_node.values = node.values[3:]
                node.values = [node.values[2]] # 중간값으로 값 갱신
                node.children = [left_node, right_node] # 자식 노드
            else: # 현재 노드가 부모 노드인 경우 자식 노드로 이동
                i = 0
                while i < len(node.values): # value와 현재 노드의 values 리스트를 비교
                    # value가 현재 노드의 values[i] 값보다 작다면, 
                    # 삽입할 value는 현재 노드의 values[i] 값보다 왼쪽에 있어야 함을 의미
                    # 이 경우, while 루프를 탈출하고 i는 삽입할 value가 들어가야 하는 인덱스가 된다.              
                    if value < node.values[i]:
                        break
                    i += 1
                self.insert_value(node.children[i], value) # value를 자식 노드 중 i 인덱스에 해당하는 자식 노드로 이동
    def get(self, value):
        return self.get_value(self.root, value)
    def get_value(self, node, value):
        if not node.children:  # 현재 노드가 리프 노드인 경우 
            return value in node.values
        else:  # 현재 노드가 부모 노드인 경우 자식 노드로 이동
            i = 0
            while i < len(node.values):
                if value == node.values[i]:
                    return True
                if value < node.values[i]:
                    return self.get_value(node.children[i], value)
                i += 1
            return self.get_value(node.children[i], value)






    #=================이하 삭제 함수(gtp생성)->  심심할 때 볼 것
    def remove(self, value):
        self.remove_value(self.root, value)

    def remove_value(self, node, value):
        if not node:
            return False

        # 해당 값을 노드에서 찾음
        for i, val in enumerate(node.values):
            if val == value:
                node.values.pop(i)
                return True

        # 해당 값이 현재 노드에 없으므로 자식 노드를 탐색
        for i, val in enumerate(node.values):
            if value < val:
                # 왼쪽 자식 노드에서 재귀적으로 삭제 시도
                if self.remove_value(node.children[i], value):
                    # 자식 노드의 삭제로 인해 노드가 공백이 되면 병합을 시도
                    if len(node.children[i].values) == 0:
                        self.merge_nodes(node, i)
                    return True
                break
        else:
            # 오른쪽 자식 노드에서 재귀적으로 삭제 시도
            if self.remove_value(node.children[-1], value):
                # 자식 노드의 삭제로 인해 노드가 공백이 되면 병합을 시도
                if len(node.children[-1].values) == 0:
                    self.merge_nodes(node, -1)
                return True
        return False

    def merge_nodes(self, parent, child_index):
        # 왼쪽 형제 노드를 확인하고 병합
        if child_index > 0 and len(parent.children[child_index - 1].values) > 1:
            left_sibling = parent.children[child_index - 1]
            child = parent.children[child_index]
            left_sibling.values.append(parent.values[child_index - 1])
            left_sibling.values.extend(child.values)
            left_sibling.children.extend(child.children)
            parent.values.pop(child_index - 1)
            parent.children.pop(child_index)
        # 오른쪽 형제 노드를 확인하고 병합
        elif child_index < len(parent.children) - 1 and len(parent.children[child_index + 1].values) > 1:
            right_sibling = parent.children[child_index + 1]
            child = parent.children[child_index]
            child.values.append(parent.values[child_index])
            child.values.extend(right_sibling.values)
            child.children.extend(right_sibling.children)
            parent.values.pop(child_index)
            parent.children.pop(child_index + 1)
        # 왼쪽 형제 노드와 병합
        elif child_index > 0:
            left_sibling = parent.children.pop(child_index - 1)
            child = parent.children.pop(child_index - 1)
            left_sibling.values.append(parent.values.pop(child_index - 1))
            left_sibling.values.extend(child.values)
            left_sibling.children.extend(child.children)
        # 오른쪽 형제 노드와 병합
        else:
            child = parent.children.pop(child_index)
            right_sibling = parent.children.pop(child_index)
            child.values.append(parent.values.pop(child_index))
            child.values.extend(right_sibling.values)
            child.children.extend(right_sibling.children)