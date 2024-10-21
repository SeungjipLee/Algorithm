import sys
input = sys.stdin.readline

n, k = map(int, input().split())
makgeollies = [int(input()) for _ in range(n)]


def binary_search(start, end, target):
    while start <= end:
        mid = (start+end) // 2
        num = get_makgeolli_num(mid)

        if num >= target:
            start = mid + 1
        else:
            end = mid - 1

    return end


def get_makgeolli_num(num):
    cnt = 0
    for makgeolli in makgeollies:
        cnt += makgeolli // num

    return cnt


amount = binary_search(1, max(makgeollies), k)
print(amount)