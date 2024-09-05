from itertools import permutations
from math import sqrt


def is_prime(n):
    if n == 1 or n == 0:
        return False

    if n == 2:
        return True

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


answer = set()
numbers = "17"

arr = list(numbers)

for l in range(1, len(numbers) + 1):
    for i in permutations(arr, l):
        mid = int("".join(i))
        if is_prime(mid):
            answer.add(mid)

print(answer)