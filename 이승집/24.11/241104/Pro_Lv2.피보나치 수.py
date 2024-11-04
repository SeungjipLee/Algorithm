def solution(n):
    arr = [1, 1] + [0] * (n-1)
    for i in range(2, n + 1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[n-1]%1234567