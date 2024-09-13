from collections import Counter


def solution(input_string):
    Cnt = Counter(input_string)
    ans = []
    for i in Cnt:
        if i * Cnt[i] not in input_string:
            ans.append(i)

    if ans:
        ans.sort()
    else:
        return "N"

    answer = "".join(ans)
    return answer