"""
1. 1칸을 움직이는 경우의 수 : 1가지 (1)
2. 2칸을 움직이는 경우의 수 : 2가지 (11 / 2)
3. 3칸을 움직이는 경우의 수 : 3가지 (111 / 12 / 21)
4. 4칸을 움직이는 경우의 수 : 5가지(1111 / 121 / 211 / 112 / 22)
"""

n = 40
if n <= 2:
    print(n)
else:
    arr = [0] * (n + 1)
    arr[1] = 1
    arr[2] = 2

    for i in range(3, n + 1):
        arr[i] = arr[i-1] + arr[i-2]
    print(arr[n]%1234567)

