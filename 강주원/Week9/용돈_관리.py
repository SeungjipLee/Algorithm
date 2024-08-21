import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ls = [int(input()) for _ in range(n)]

l, r = min(ls), sum(ls)

def sol(amount):
    cnt = 1
    now = amount
    for i in range(n):
        if now < ls[i]:
            cnt += 1
            now = amount
        now -= ls[i]
    
    if cnt <= m:
        return True

    return False 

res = r
while l <= r:
    mid = (l+r) // 2
    if sol(mid):
        res = mid
        r = mid - 1
    else:
        l = mid + 1
        

print(res)