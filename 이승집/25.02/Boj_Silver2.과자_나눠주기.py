import sys

def count_children(snacks, length):
    return sum(snack // length for snack in snacks)

def binary_search(snacks, m):
    left, right = 1, max(snacks)
    result = 0

    while left <= right:
        mid = (left + right) // 2

        if count_children(snacks, mid) >= m:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result

def main():
    input = sys.stdin.readline
    M, N = map(int, input().split())
    snacks = list(map(int, input().split()))

    if M > sum(snacks):
        print(0)
    else:
        print(binary_search(snacks, M))

if __name__ == "__main__":
    main()


"""input
3 10
1 2 3 4 5 6 7 8 9 10
"""