import sys
input = sys.stdin.readline

n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]


def check(answer):
    cnt = 0
    for a, b, c in ls:
        strike, ball = 0, 0
        a = str(a)
        for i in range(3):
            if a[i] == answer[i]:
                strike += 1
            else:
                if answer[i] in a:
                    ball += 1
        
        if strike == b and ball == c:
            cnt += 1

    if cnt == n:
        return True
    
    return False

res = 0
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or j == k or k == i:
                continue
            num = str(i) + str(j) + str(k)
            if check(num):
                res += 1

print(res)