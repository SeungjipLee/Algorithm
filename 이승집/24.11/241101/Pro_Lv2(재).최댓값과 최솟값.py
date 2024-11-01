def solution(s):
    arr = list(s.split())
    arr = [int(i) for i in arr]

    answer = [str(min(arr)), str(max(arr))]
    return " ".join(answer)