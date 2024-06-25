from itertools import combinations

numbers = [-2, 3, 0, 2, -5]
answer = 0

for i in combinations(numbers, 3):
    if sum(i) == 0:
        answer += 1

print(answer)