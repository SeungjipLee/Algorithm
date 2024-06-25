import sys
input = sys.stdin.readline

class Node(object):
    def __init__(self, has_end=False):
        self.has_end = has_end
        self.children = dict()


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    
    def insert(self, num):
        curr_node = self.head

        for d in num:
            if curr_node.children.get(d) is None:
                curr_node.children[d] = Node()

            curr_node = curr_node.children[d]
        
        curr_node.has_end = True

    
    def search(self, num):
        curr_node = self.head

        for d in num:
            if curr_node.children.get(d) is None:
                return True
            curr_node = curr_node.children[d]
            if curr_node.has_end:
                return False
        return True


t = int(input())
for tc in range(t):
    n = int(input())
    ls = [input().rstrip() for _ in range(n)]
    ls.sort(key = lambda x:len(x))

    data = Trie()

    for num in ls:
        if data.search(num) == False:
            print('NO')
            break

        data.insert(num)
    else:
        print('YES')