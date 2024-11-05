n = int(input())
stores = list(map(int, input().split()))

num, cnt = 0, 0
for store in stores:
    if store == num:
        cnt += 1
        num += 1
        num %= 3
    
print(cnt)