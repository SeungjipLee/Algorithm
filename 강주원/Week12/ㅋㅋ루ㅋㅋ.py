import sys
input = sys.stdin.readline

s = input().rstrip()
res = s.count('R')
# 좌우 R 제거
s = s.strip('R')
l = len(s)
R = [0]
i, j = 0, l-1

while i <= j:
    if s[i] == 'K' and s[j] == 'K':
        R.append(0)
        i += 1
        j -= 1
    else:
        if s[i] == 'R':
            i += 1
            R[-1] += 1
        elif s[j] == 'R':
            j -= 1
            R[-1] += 1

    
for r in range(len(R)-1, 0, -1):
    if R[r]:
        res = max(res, R[r] + r*2)

    R[r-1] += R[r]


print(res)