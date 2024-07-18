import random

# Function to generate a test case
def generate_test_case():
    N = random.randint(1, 300)   # Number of jewels, for simplicity, set a lower range
    K = random.randint(1, 300)   # Number of bags, for simplicity, set a lower range
    items = []
    bags = []
    
    for _ in range(N):
        M = random.randint(1, 1000)  # Weight of the jewel
        V = random.randint(1, 1000)  # Value of the jewel
        items.append((M, V))
    
    for _ in range(K):
        C = random.randint(1, 1000)  # Capacity of the bag
        bags.append(C)
    
    return N, K, items, bags

# Function to run the algorithm with a given test case
def run_algorithm(N, K, items, bags):
    class AVLNode:
        def __init__(self, key, height=0, left=None, right=None):
            self.key = key
            self.height = height
            self.left = left
            self.right = right

    class AVLTree:
        def __init__(self):
            self.root = None

        def get_height(self, node):
            if not node:
                return 0
            return node.height

        def update_height(self, node):
            if node:
                node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        def get_balance(self, node):
            if not node:
                return 0
            return self.get_height(node.left) - self.get_height(node.right)

        def rotate_right(self, y):
            if not y or not y.left:
                return y
            x = y.left
            T2 = x.right

            x.right = y
            y.left = T2

            self.update_height(y)
            self.update_height(x)

            return x

        def rotate_left(self, x):
            if not x or not x.right:
                return x
            y = x.right
            T2 = y.left

            y.left = x
            x.right = T2

            self.update_height(x)
            self.update_height(y)

            return y

        def insert(self, key):
            self.root = self._insert(self.root, key)

        def _insert(self, node, key):
            if not node:
                return AVLNode(key)
            elif key < node.key:
                node.left = self._insert(node.left, key)
            else:
                node.right = self._insert(node.right, key)

            self.update_height(node)
            balance = self.get_balance(node)

            if balance > 1 and key < node.left.key:
                return self.rotate_right(node)

            if balance < -1 and key > node.right.key:
                return self.rotate_left(node)

            if balance > 1 and key > node.left.key:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)

            if balance < -1 and key < node.right.key:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)

            return node

        def delete(self, key):
            self.root = self._delete(self.root, key)

        def _delete(self, node, key):
            if not node:
                return node
            elif key < node.key:
                node.left = self._delete(node.left, key)
            elif key > node.key:
                node.right = self._delete(node.right, key)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left

                temp = self.get_min_value_node(node.right)
                node.key = temp.key
                node.right = self._delete(node.right, temp.key)

            self.update_height(node)
            balance = self.get_balance(node)

            if balance > 1 and self.get_balance(node.left) >= 0:
                return self.rotate_right(node)

            if balance > 1 and self.get_balance(node.left) < 0:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)

            if balance < -1 and self.get_balance(node.right) <= 0:
                return self.rotate_left(node)

            if balance < -1 and self.get_balance(node.right) > 0:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)

            return node

        def get_min_value_node(self, node):
            current = node
            while current.left is not None:
                current = current.left
            return current

        def search(self, key):
            return self._search(self.root, key)

        def _search(self, node, key):
            if not node or node.key == key:
                return node
            elif key < node.key:
                return self._search(node.left, key)
            else:
                return self._search(node.right, key)

        def find_successor(self, key):
            successor = None
            node = self.root
            while node:
                if key <= node.key:
                    successor = node
                    node = node.left
                else:
                    node = node.right
            return successor

        def in_order(self):
            self._in_order(self.root)

        def _in_order(self, node):
            if not node:
                return
            self._in_order(node.left)
            print(node.key, end=" ")
            self._in_order(node.right)

    items.sort(reverse=True, key=lambda x: x[1])
    answer = 0
    bags_tree = AVLTree()

    for bag in bags:
        bags_tree.insert(bag)

    for item in items:
        if bags_tree.root is None:
            break
        bag = bags_tree.find_successor(item[0])

        if bag is not None:
            answer += item[1]
            bags_tree.delete(bag.key)

    return answer

# Generate 50 test cases
test_cases = [generate_test_case() for _ in range(50)]

# Run the algorithm with each test case and print the results
for i, (N, K, items, bags) in enumerate(test_cases):
    result = run_algorithm(N, K, items, bags)
    print(f"Test Case {i + 1}: N = {N}, K = {K}, Answer = {result}")
