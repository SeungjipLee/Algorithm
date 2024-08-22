import sys
input = sys.stdin.readline

# 조카의 수, 과자의 수
m, n = map(int, input().split())
# 이분 탐색을 위해 정렬
ls = sorted(list(map(int, input().split())))

def binary():
    l, r, res = 0, max(ls), 0
    while l <= r:
        mid = (l+r) // 2
        if mid == 0:
            break
        cnt = 0
        for i in ls:
            cnt += (i // mid)

        if cnt >= m:
            res = mid
            l = mid + 1
        else:
            r = mid - 1
    
    return res

print(binary())