n = int(input())
ls = list(map(int, input().split()))
cnt = 1
for i in range(n-1):
  if ls[i] <= ls[i+1]:
    cnt += 1

print(cnt)