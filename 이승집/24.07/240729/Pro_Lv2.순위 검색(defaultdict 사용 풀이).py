from collections import defaultdict
from pprint import pprint


def solution(info, query):
    # 조건에 맞는 인덱스 딕셔너리 생성
    data = defaultdict(list)

    for i in info:
        lan, fr_ba, se_ju, food, score = i.split()
        data[(lan, fr_ba, se_ju, food)].append(int(score))

    # 각 조건별로 데이터를 정렬
    for key in data:
        data[key].sort()
    pprint(data)

    def filter_data(conditions, score, data):
        filtered_data = []
        for key, values in data.items():
            if all(c == '-' or c == k for c, k in zip(conditions, key)):
                filtered_data.extend([v for v in values if v >= score])
        return filtered_data

    answer = []

    for q in query:
        fi_lan, fi_fr_ba, fi_se_ju, k = q.split(" and ")
        fi_food, fi_score = k.split()
        fi_score = int(fi_score)

        filtered = filter_data((fi_lan, fi_fr_ba, fi_se_ju, fi_food), fi_score, data)
        answer.append(len(filtered))

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]


print(solution(info, query))


