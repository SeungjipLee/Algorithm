import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

arr = []
while 1:
    try:
        arr.append(int(input()))
    except:
        break


def sol(arr):
    if len(arr) == 0:
        return
    
    mid = arr[0]
    right = []
    for i in range(1, len(arr)):
        if arr[i] > mid:
            left = arr[1:i]
            right = arr[i:]
            break
    
    else:
        left = arr[1:]

    sol(left)
    sol(right)
    print(mid)

sol(arr)