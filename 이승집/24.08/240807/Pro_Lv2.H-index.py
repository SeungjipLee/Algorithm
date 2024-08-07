citations = [3, 0, 6, 1, 5]
"""
5개의 논문을 썼는데

k번 이상 인용된 논문의 개수가 k여야한다.

k = 1 -> 5개라서 모순
k = 2 -> 3개라서 모순
k = 3 -> 3개(O)
k = 4 -> 2(X)

"""

citations.reverse()
answer = 0


for standard in range(max(citations) + 1):
    cnt = 0
    for i in citations:
        if i >= standard:
            cnt += 1
            if cnt >= standard:
                answer = standard

print(answer)

"""다른 사람 풀이
def solution(citations):
    citations.sort()
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0
"""