import pprint
from collections import defaultdict
from itertools import combinations
import bisect

def solution(info, query):
    data = defaultdict(list)

    # 모든 조건 조합을 포함하는 키 생성 및 사전 구축
    for i in info:
        lan, fr_ba, se_ju, food, score = i.split()
        score = int(score)
        keys = [lan, fr_ba, se_ju, food]
        for j in range(5):
            for comb in combinations(range(4), j):
                temp_key = keys[:]
                for index in comb:
                    temp_key[index] = '-'
                data[tuple(temp_key)].append(score)

    pprint.pprint(data)
    # 각 조건 조합별로 점수 리스트 정렬
    for key in data:
        data[key].sort()

    answer = []

    for q in query:
        fi_lan, fi_fr_ba, fi_se_ju, k = q.split(" and ")
        fi_food, fi_score = k.split()
        fi_score = int(fi_score)
        key = (fi_lan, fi_fr_ba, fi_se_ju, fi_food)

        # 해당 키의 리스트에서 fi_score 이상인 값의 개수 찾기
        if key in data:
            scores = data[key]
            idx = bisect.bisect_left(scores, fi_score)
            answer.append(len(scores) - idx)
        else:
            answer.append(0)

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]


print(solution(info, query))
