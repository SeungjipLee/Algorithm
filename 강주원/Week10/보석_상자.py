import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ls = [int(input()) for _ in range(m)]


def binary(target):
    l, r = 1, max(ls)
    res = 0
    while l <= r:
        cnt = 0
        mid = (l+r) // 2
        for i in ls:
            if i % mid == 0:
                cnt += i // mid
            else:
                cnt += i // mid + 1
        
        if cnt > target:
            l = mid + 1
        else:
            r = mid - 1
            res = mid
    
    return res

print(binary(n))