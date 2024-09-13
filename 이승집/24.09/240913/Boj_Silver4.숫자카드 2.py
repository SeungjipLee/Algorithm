"""
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10
"""
N = int(input())
display = list(map(int, input().split()))

M = int(input())
nums = list(map(int, input().split()))

# display 배열을 정렬
display.sort()


# 이진 탐색으로 특정 숫자의 시작 인덱스 찾기
def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


# 이진 탐색으로 특정 숫자의 끝 인덱스 찾기
def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left


# 각 num이 display에 몇 번 등장하는지 출력
for num in nums:
    left = lower_bound(display, num)
    right = upper_bound(display, num)
    count = right - left
    print(count, end=" ")
