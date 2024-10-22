import sys
input = sys.stdin.readline

n, m = map(int, input().split())
balloons = list(map(int, input().split()))


def binary_search(start, end, target):
    res = m * max(balloons)
    while start <= end:
        mid = (start+end) // 2
        num = get_balloon_num(mid)

        if num >= target:
            res = min(res, mid)
            end = mid - 1
        else:
            start = mid + 1

    return res


def get_balloon_num(num):
    cnt = 0
    for balloon in balloons:
        cnt += num // balloon

    return cnt


amount = binary_search(1, m * max(balloons), m)
print(amount)