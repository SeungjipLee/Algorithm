# 트리의 맨 왼쪽이 제일 작은 수
# 트리의 맨 오른쪽이 제일 큰 수

class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right
    
class BST:
    def __init__(self, head) -> None:
        self.head = head # node
    
    # insert
    def insert(self, value):
        if not self.head:
            self.head = Node(value)
            print('노드 생성')
            return True
        
        self.cn = self.head # current_node
        
        while self.cn:
            if value < self.cn.value:
                if self.cn.left:
                    self.cn = self.cn.left
                else:
                    self.cn.left = Node(value)
                    print('왼쪽 노드 생성')
                    return True
            else:
                if self.cn.right:
                    self.cn = self.cn.right
                else:
                    self.cn.right = Node(value)
                    print('오른쪽 노드 생성')
                    return True
    
    # delete
    def delete_max(self):
        if not self.head:
            return 'empty'
       
        if not self.head.left and not self.head.right:
            self.head = None
            return True

        if self.head.left and not self.head.right:
            self.head = self.head.left
            return True
        
        # delete end of right
        self.p = self.head
        self.cn = self.head
        
        while self.cn.right:
            self.p = self.cn
            self.cn = self.cn.right
        
        if not self.cn.left:
            self.p.right = None
            print('맨 오른쪽 노드 삭제')
            return True
        elif self.cn.left:
            self.p.right = self.cn.left
            print('오른쪽 삭제 후 왼쪽 노드 올림')
            return True
    
    def delete_min(self):
        if not self.head:
            return 'empty'
        
        if not self.head.left and not self.head.right:
            self.head = None
            return True
        
        if not self.head.left and self.head.right:
            self.head = self.head.right
            return True
        
        # delete end of left
        self.p = self.head
        self.cn = self.head
        
        while self.cn.left:
            self.p = self.cn
            self.cn = self.cn.left
            
        if not self.cn.right:
            self.p.left = None
            print('맨 왼쪽 노드 삭제')
            return True
        else:
            self.p.left = self.cn.right
            print('왼쪽 삭제 후 오른쪽 노드 올림')
            return True
        
    
    def search(self):
        
        max_min = [0, 0]
        if not self.head:
            return max_min
        
        self.p = self.head
        self.cn = self.head

        while self.cn.left:
            self.p = self.cn
            self.cn = self.cn.left
        
        max_min[1] = self.cn.value
        
        self.p = self.head
        self.cn = self.head

        while self.cn.right:
            self.p = self.cn
            self.cn = self.cn.right
        
        max_min[0] = self.cn.value
        
        return max_min
    
def solution(operations):
    bst = BST(None)
    
    for o in operations:
        cmd, num = o.split()
        
        if cmd == "I":
            bst.insert(int(num))
        else:
            if num == "1":
                bst.delete_max()
            else:
                bst.delete_min()
    answer = bst.search()
    return answer