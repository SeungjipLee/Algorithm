n, m = map(int, input().split())
dots = sorted(list(map(int, input().split())))


def binary(target):
    start, end = 0, n-1
    while start <= end:
        mid = (start + end) // 2
        if dots[mid] < target:
            start = mid + 1
        elif dots[mid] == target:
            if target == a:
                end = mid - 1
            else:
                start = mid + 1
        else:
            end = mid - 1

    return end


for _ in range(m):
    a, b = map(int, input().split())
    print(binary(b) - binary(a))