import sys
input = sys.stdin.readline

s, c = map(int, input().split())
green_onions = [int(input()) for _ in range(s)]


def binary_search(start, end, target):
    while start <= end:
        mid = (start+end) // 2
        num = get_green_onion_num(mid)

        if num >= target:
            start = mid + 1
        else:
            end = mid - 1

    return end


def get_green_onion_num(num):
    cnt = 0
    for onion in green_onions:
        cnt += onion // num

    return cnt


length = binary_search(1, max(green_onions), c)
res = sum(green_onions) - c*length
print(res)