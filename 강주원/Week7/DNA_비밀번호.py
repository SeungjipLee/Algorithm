import sys
input = sys.stdin.readline

s, p = map(int, input().split())
ls = list(input().rstrip())
A, C, G, T = map(int, input().split())
required = {'A': A, 'C': C, 'G': G, 'T': T}
current = {i:0 for i in "ACGT"}
res = 0


def check():
    if all(current[char] >= required[char] for char in "ACGT"):
        return True
    
    return False


for i in range(p):
    current[ls[i]] += 1

if check():
    res += 1

for i in range(p,s):
    left_idx = ls[i-p]
    right_idx = ls[i]
    current[left_idx] -= 1
    current[right_idx] += 1

    if check():
        res += 1

print(res)