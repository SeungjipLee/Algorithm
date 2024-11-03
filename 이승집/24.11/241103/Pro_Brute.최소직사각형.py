def solution(sizes):
    first = []
    second = []
    for i in sizes:
        first.append(max(i))
        second.append(min(i))
    return max(first) * max(second)