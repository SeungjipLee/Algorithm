def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

    temp = []
    for i in reserve:
        if i in lost:
            temp.append(i)

    for i in temp:
        lost.remove(i)
        reserve.remove(i)

    for i in lost:
        if i - 1 in reserve:
            reserve.remove(i - 1)
            continue
        if i + 1 in reserve:
            reserve.remove(i + 1)
            continue
        n -= 1

    return n