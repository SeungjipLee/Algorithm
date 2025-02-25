"""
중위 순회 결과를 보고 Tree의 구조를 유추하는 문제
"""
import sys

def build_tree(inorder, depth, level_order):
    if not inorder:
        return

    mid = len(inorder) // 2
    level_order[depth].append(inorder[mid])

    build_tree(inorder[:mid], depth + 1, level_order)
    build_tree(inorder[mid + 1:], depth + 1, level_order)

def main():
    input = sys.stdin.readline
    K = int(input())
    inorder = list(map(int, input().split()))

    level_order = [[] for _ in range(K)]

    build_tree(inorder, 0, level_order)

    for level in level_order:
        print(*level)

if __name__ == "__main__":
    main()
