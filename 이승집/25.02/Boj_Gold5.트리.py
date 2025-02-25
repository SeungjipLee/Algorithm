import sys


def main():
    input = sys.stdin.readline
    n = int(input())
    parents = list(map(int, input().split()))
    erase = int(input())

    tree = {i: [] for i in range(n)}
    root = -1

    for child, parent in enumerate(parents):
        if parent == -1:
            root = child
        else:
            tree[parent].append(child)

    if erase in tree:
        tree[erase] = []

    for node in tree:
        if erase in tree[node]:
            tree[node].remove(erase)

    def count_leaf_nodes(tree, root):
        if root == -1:  # 트리가 아예 없는 경우
            return 0

        stack = [root]
        leaf_count = 0

        while stack:
            node = stack.pop()
            if not tree[node]:  # 자식이 없으면 리프 노드
                leaf_count += 1
            else:
                stack.extend(tree[node])  # 자식 노드를 스택에 추가

        return leaf_count

    if root == erase:
        print(0)
    else:
        print(count_leaf_nodes(tree, root))


if __name__ == "__main__":
    main()

"""input
5
-1 0 0 1 1
1
"""