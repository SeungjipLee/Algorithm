import sys
from collections import defaultdict

input = sys.stdin.readline
n, k = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
count = defaultdict(int)
max_length = 0

for right in range(n):
    count[arr[right]] += 1

    while count[arr[right]] > k:
        count[arr[left]] -= 1
        left += 1

    max_length = max(max_length, right - left + 1)

print(max_length)
