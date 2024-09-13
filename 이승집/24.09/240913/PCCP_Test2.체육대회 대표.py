from itertools import permutations


def solution(ability):
    N = len(ability)
    M = len(ability[0])
    answer = 0
    for i in permutations(range(N), M):
        S = 0
        for j in range(M):
            S += ability[i[j]][j]
        if S > answer:
            answer = S
    return answer