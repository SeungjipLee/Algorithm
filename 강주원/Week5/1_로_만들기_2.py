n = int(input())
dp = [[1]] * 1000001

for i in range(2, n+1):
    candi = [dp[i-1]]
    if i % 2 == 0:
        candi.append(dp[i//2])
    if i % 3 == 0:
        candi.append(dp[i//3])
    
    min_leng = min(candi, key=lambda x:len(x))
    dp[i] = min_leng + [i]

print(len(dp[n]) - 1)
print(*dp[n][::-1])