def solution(id_list, report, k):
    answer = [0] * len(id_list)
    D = {i: set() for i in id_list}
    na = {k: i for i, k in enumerate(id_list)}
    for r in report:
        a, b = r.split()
        D[b].add(a)

    mid = []
    for d in D:
        if len(D[d]) >= k:
            mid.append(d)

    for i in mid:
        for j in D[i]:
            answer[na[j]] += 1
    return answer