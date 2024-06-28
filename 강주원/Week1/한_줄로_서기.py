n = int(input())
ls = [0] + list(map(int, input().split()))
res = [n+1] * (n+1)

for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if cnt == ls[i] and res[j] == n+1:
            res[j] = i
            break
        if res[j] > i:
            cnt += 1
            

print(*res[1::])