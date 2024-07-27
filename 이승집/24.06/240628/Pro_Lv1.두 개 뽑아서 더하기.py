from itertools import combinations

numbers = [2, 1, 3, 4, 1]
comb = set()

for i in combinations(numbers, 2):
    comb.add(sum(i))

answer = list(comb)
answer.sort()

print(answer)