from collections import Counter


def solution(N, stages):
    M = len(stages)
    li = Counter(stages)
    ans = []

    for i in range(1, N + 1):
        if M > 0:
            ans.append((li.get(i, 0) / M, i))
            M -= li.get(i, 0)
        else:
            ans.append((0, i))

    answer = sorted(ans, key=lambda x: (-x[0], x[1]))

    return [i[1] for i in answer]