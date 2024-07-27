"""
f(0) = 0
f(1) = 1
f(n) = f(n-1) + f(n-2) (n>=2)
"""
arr = [0] * 100001
arr[0] = 0
arr[1] = 1
n = 100

for i in range(2, n + 1):
    if arr[i] == 0:
        arr[i] = arr[i-1] + arr[i-2]

print(arr[n])