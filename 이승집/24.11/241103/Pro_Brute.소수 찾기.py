from itertools import permutations


def find_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True

    for i in range(2, int(n ** (1 / 2)) + 2):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    arr = list(numbers)
    ans = set()
    for k in range(1, len(arr) + 1):
        for i in permutations(arr, k):
            A = int("".join(i))
            if find_prime(A):
                ans.add(A)
    print(ans)
    return len(ans)