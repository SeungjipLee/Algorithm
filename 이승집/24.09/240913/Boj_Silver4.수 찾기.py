"""
input
5
4 1 5 2 3
5
1 3 7 9 5
"""

N = int(input())
display = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

display.sort()

def is_contained(n):
    left, right = 0, len(display) - 1

    while left <= right:
        mid = (left + right)//2

        if display[mid] == n:
            return True
        elif display[mid] > n:
            right = mid - 1
        else:
            left = mid + 1

    return False


for num in nums:
    if is_contained(num):
        print(1)
    else:
        print(0)