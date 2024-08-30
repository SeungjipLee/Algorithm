import sys
input = sys.stdin.readline

n = int(input())
ls = sorted(list(map(int, input().split())))

print(sum(ls[:n-1])/2 + ls[-1])