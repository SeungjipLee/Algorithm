import sys
input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))

# 30 50 30 30 30 30 30 50 30 30 30 50
# 50 30 20 70
max_val = max(ls)
print(sum(ls) + (len(ls)-2)*max_val)