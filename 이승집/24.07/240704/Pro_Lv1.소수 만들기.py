from itertools import combinations

nums = [1, 2, 7, 6, 4]
answer = 0


def is_prime(n):
    mid = 2
    for i in range(2, int(n**(1/2) + 1)):
        if n % i == 0:
            return False
    return True


for i in combinations(nums, 3):
    if is_prime(sum(i)):
        answer += 1

print(answer)