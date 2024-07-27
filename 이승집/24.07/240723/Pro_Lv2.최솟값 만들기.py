A = [1, 4, 2]
B = [5, 4, 4]

A.sort()
B.sort(reverse=True)
n = len(A)

answer = 0

for i in range(n):
    answer += A[i] * B[i]

print(answer)