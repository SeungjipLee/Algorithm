from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []

    for c in course:
        comb_count = Counter()
        for order in orders:
            # 주문을 정렬하여 일관된 조합 생성
            sorted_order = sorted(order)
            # 현재 주문에서 코스 크기에 해당하는 모든 조합 생성
            combs = combinations(sorted_order, c)
            # 조합의 빈도 계산
            comb_count.update(combs)

        # 해당 코스 크기에서 가장 많이 주문된 횟수 찾기
        max_count = 0
        if comb_count:
            max_count = max(comb_count.values())

        # 최소 두 번 이상 주문되고, 가장 많이 주문된 조합 선택
        for comb, count in comb_count.items():
            if count >= 2 and count == max_count:
                answer.append(''.join(comb))

    # 결과를 사전순으로 정렬하여 반환
    return sorted(answer)


# 예시 테스트 케이스 적용
orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
courses = [2, 3, 4]
result = solution(orders, courses)
print(result)  # 출력: ['AC', 'ACDE', 'BCFG', 'CDE']
