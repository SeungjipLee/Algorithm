import sys
input = sys.stdin.readline

n = int(input())
colors = input().rstrip()
r = [i for i in colors.split("B") if i]
b = [i for i in colors.split("R") if i]

print(min(len(r), len(b)) + 1)