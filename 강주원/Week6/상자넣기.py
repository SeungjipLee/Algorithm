n = int(input())
ls = list(map(int, input().split()))

arr = [ls[0]]

def find(target):
    start, end = 0, len(arr)-1

    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return start 


for i in ls:
    if arr[-1] < i:
        arr.append(i)
    else:
        idx = find(i)
        arr[idx] = i

print(len(arr))