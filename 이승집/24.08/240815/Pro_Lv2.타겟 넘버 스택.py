from itertools import product

numbers = [4, 1, 2, 1]
target = 4
answer = 0

A = [[-1, 1] for _ in range(len(numbers))]
for i in product(*A):
    mid = 0
    for j in range(len(numbers)):
        mid += i[j] * numbers[j]
    if mid == target:
        answer += 1

print(answer)