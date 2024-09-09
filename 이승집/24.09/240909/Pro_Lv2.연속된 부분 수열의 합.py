from collections import deque


sequence = [2, 2, 2, 2, 2]
N = len(sequence)
k = 6

answer = []

for idx in range(N):
    Q = deque([sequence[idx]])
    nxt = idx + 1
    while sum(Q) < k:
        if nxt < N:
            Q.append(sequence[nxt])
            nxt += 1
        else:
            break
    if sum(Q) == k:
        answer.append((nxt-idx, idx, nxt-1))

    print(Q)

answer.sort()
print([answer[0][1], answer[0][2]])


"""
크기가 너무 커서 시간 초과 O(N)으로 풀어야 한다.
"""


def solution(sequence, k):
    N = len(sequence)
    answer = []
    left, right = 0, 0
    current_sum = sequence[0]

    while right < N:
        if current_sum == k:
            answer.append((right - left + 1, left, right))
            current_sum -= sequence[left]
            left += 1
        elif current_sum < k:
            right += 1
            if right < N:
                current_sum += sequence[right]
        else:  # current_sum > k
            current_sum -= sequence[left]
            left += 1

    answer.sort()
    return [answer[0][1], answer[0][2]]


print(solution(sequence, k))