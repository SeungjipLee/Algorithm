import sys
input = sys.stdin.readline

n = int(input())
popul = list(map(int, input().split()))
arr = [[] for _ in range(n+1)]

for i in range(n):
    a = list(map(int, input().split()))
    arr[i+1].extend(a[1:])

print(arr)