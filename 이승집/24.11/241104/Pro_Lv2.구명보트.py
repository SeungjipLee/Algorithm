def solution(people, limit):
    people.sort()
    n = len(people)
    s, e = 0, n - 1
    cnt = 0
    while s <= e:
        if people[s] + people[e] <= limit:
            s += 1
            e -= 1
            cnt += 1
        else:
            e -= 1
            cnt += 1
    return cnt