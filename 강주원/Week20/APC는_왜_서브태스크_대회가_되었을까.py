import sys
input = sys.stdin.readline

n, l, k = map(int, input().split())
score = 0
difficulties = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x:x[1])
cnt = 0
for a, b in difficulties:
    if cnt == k:
        break
    
    if b <= l:
        score += 140
        cnt += 1
    elif a <= l:
        score += 100
        cnt += 1
        
print(score)