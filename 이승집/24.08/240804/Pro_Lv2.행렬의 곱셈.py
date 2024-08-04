arr1 = [[1, 2], [2, 1]]
arr2 = [[1, 1, 1, 1], [2, 2, 2, 2]]


"""
1 4    1 2  =  13 18  
3 2    3 4      9 14
4 1             7 12
5 2            11 18


1 2  1 1 1 1 = 5
2 1  2 2 2 2
"""

n, l, m = len(arr1), len(arr2), len(arr2[0])
print(n, l, m)


answer = [[0] * m for _ in range(n)]
print(answer)

for i in range(n):
    for j in range(m):
        # 곱해야할 행 / 곱해야할 열
        A = arr1[i]
        B = [arr2[k][j] for k in range(l)]
        mid = 0
        for p in range(l):
            mid += A[p] * B[p]
        answer[i][j] = mid


print(answer)