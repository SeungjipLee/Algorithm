import sys
input = sys.stdin.readline
n,d,k,c = map(int, input().split())
ls = [int(input()) for _ in range(n)]

window = [0] * (d+1)
current_kind = 0
for i in range(k):
    if window[ls[i]] == 0:
        current_kind += 1
    window[ls[i]] += 1

if window[c] == 0:
    current_kind += 1
    window[c] += 1

res = current_kind
for i in range(1,n):
    left_idx = ls[i-1]
    window[left_idx] -= 1
    if window[left_idx] == 0:
        current_kind -= 1
        
    right_idx = ls[(i+k-1)%n]
    if window[right_idx] == 0:
        current_kind += 1
    window[right_idx] += 1

    if window[c] == 0:
        res = max(res, current_kind + 1)
    else:
        res = max(res, current_kind)

print(res)